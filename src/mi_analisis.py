"""Análisis corto: RFM y top productos

Este script realiza un análisis RFM (recencia, frecuencia, monetario) por cliente
usando los CSV disponibles en el repositorio. También guarda dos figuras:
- reports/rfm_segment_counts.png
- reports/top_products.png

El script intenta localizar los ficheros comunes (ventas, detalle_ventas, clientes,
productos) en varias rutas del proyecto. Si no encuentra los archivos necesarios,
termina con un mensaje claro.

Uso:
    python src/mi_analisis.py

Salida:
    - reports/rfm_summary.csv
    - reports/rfm_segment_counts.png
    - reports/top_products.png

Requisitos: pandas, matplotlib, seaborn (ver requirements.txt)
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# intentar reutilizar utilidades del paquete si es posible
try:
    from src.data import clean_df
except Exception:
    try:
        from data import clean_df  # type: ignore
    except Exception:
        clean_df = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

SEARCH_PATHS = [
    ROOT / "entrega2" / "data" / "csv" / "origin",
    ROOT / "entrega2" / "data" / "csv",
    ROOT / "db",
    ROOT,
]

Filenames = {
    "ventas": ["ventas.csv", "venta.csv"],
    "detalle": ["detalle_ventas.csv", "detalle.csv"],
    "clientes": ["clientes.csv", "cliente.csv"],
    "productos": ["productos.csv", "producto.csv"],
}


def locate_file(names: list[str]) -> Optional[Path]:
    """Buscar recursivamente en SEARCH_PATHS por alguno de los nombres."""
    for base in SEARCH_PATHS:
        if not base.exists():
            continue
        for name in names:
            p = base / name
            if p.exists():
                return p
        # buscar recursivamente
        for p in base.rglob("*"):
            if p.name in names:
                return p
    return None


def load_df(p: Path) -> pd.DataFrame:
    """Carga un CSV con pandas intentando detectar separador y encoding.
    Usa engine 'python' para mayor robustez en archivos sucios.
    """
    encodings = ["utf-8", "latin1", "cp1252"]
    seps = [",", ";", "\t"]
    last_err = None
    for enc in encodings:
        for sep in seps:
            try:
                return pd.read_csv(p, encoding=enc, sep=sep, engine="python")
            except Exception as e:
                last_err = e
    # fallback a pandas autodetect
    try:
        return pd.read_csv(p, engine="python")
    except Exception:
        raise last_err if last_err is not None else RuntimeError("No se pudo leer")


def find_date_column(df: pd.DataFrame) -> Optional[str]:
    candidates = [
        "fecha",
        "fecha_venta",
        "fechaVenta",
        "date",
        "fecha_factura",
        "fecha_venta",
        "created_at",
        "fecha_hora",
    ]
    cols = [c.lower() for c in df.columns]
    for cand in candidates:
        if cand.lower() in cols:
            return df.columns[cols.index(cand.lower())]
    # intentar detectar dtype datetime-like
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            return c
    # heurístico: columna con 'fecha' en el nombre
    for c in df.columns:
        if "fecha" in c.lower() or "date" in c.lower():
            return c
    return None


def find_customer_col(df: pd.DataFrame) -> Optional[str]:
    candidates = ["cliente_id", "id_cliente", "idcliente", "cliente", "customer_id"]
    cols = [c.lower() for c in df.columns]
    for cand in candidates:
        if cand.lower() in cols:
            return df.columns[cols.index(cand.lower())]
    return None


def find_total_col(df: pd.DataFrame) -> Optional[str]:
    candidates = ["total", "importe", "monto", "total_venta", "valor"]
    cols = [c.lower() for c in df.columns]
    for cand in candidates:
        if cand.lower() in cols:
            return df.columns[cols.index(cand.lower())]
    return None


def compute_rfm(ventas: pd.DataFrame, detalle: Optional[pd.DataFrame], clientes: Optional[pd.DataFrame]) -> pd.DataFrame:
    # localizar columnas
    date_col = find_date_column(ventas)
    cust_col = find_customer_col(ventas)
    total_col = find_total_col(ventas)

    if date_col is None:
        raise RuntimeError("No se pudo localizar la columna de fecha en ventas")
    if cust_col is None:
        raise RuntimeError("No se pudo localizar la columna de cliente en ventas")

    ventas = ventas.copy()
    ventas[date_col] = pd.to_datetime(ventas[date_col], errors="coerce")
    ventas = ventas.dropna(subset=[date_col, cust_col])

    # si hay columna total, usarla, si no intentar reconstruir desde detalle
    if total_col is not None and total_col in ventas.columns:
        ventas["_total"] = pd.to_numeric(ventas[total_col], errors="coerce").fillna(0.0)
    elif detalle is not None:
        # intentar mapear id_venta
        sale_id_cols = [c for c in ventas.columns if "id" in c.lower() and ("venta" in c.lower() or "sale" in c.lower())]
        detail_sale_cols = [c for c in detalle.columns if "id" in c.lower() and ("venta" in c.lower() or "sale" in c.lower())]
        # heurístico: usar primera columna coincidente
        if sale_id_cols and detail_sale_cols:
            scol = sale_id_cols[0]
            dcol = detail_sale_cols[0]
            detalle = detalle.copy()
            # buscar cantidad y precio
            qty_col = None
            price_col = None
            for c in detalle.columns:
                if "cant" in c.lower() or "cantidad" in c.lower():
                    qty_col = c
                if "precio" in c.lower() or "valor" in c.lower() or "price" in c.lower():
                    price_col = c
            if qty_col and price_col:
                detalle["_line_total"] = pd.to_numeric(detalle[qty_col], errors="coerce").fillna(0) * pd.to_numeric(detalle[price_col], errors="coerce").fillna(0)
                sale_totals = detalle.groupby(dcol) ["_line_total"].sum().rename("_total").reset_index()
                ventas = ventas.merge(sale_totals, how="left", left_on=scol, right_on=dcol)
                if "_total" not in ventas.columns:
                    ventas["_total"] = 0.0
            else:
                ventas["_total"] = 0.0
        else:
            ventas["_total"] = 0.0
    else:
        ventas["_total"] = 0.0

    # Agregar columnas necesarias
    ventas["_customer"] = ventas[cust_col].astype(str)
    ventas["_date"] = ventas[date_col]
    ventas["_total"] = pd.to_numeric(ventas["_total"], errors="coerce").fillna(0.0)

    # referencia de recencia
    reference_date = ventas["_date"].max() + pd.Timedelta(days=1)

    # RFM aggregations
    agg = ventas.groupby("_customer").agg(
        recency=("_date", lambda x: (reference_date - x.max()).days),
        frequency=("_date", "count"),
        monetary=("_total", "sum"),
    )
    agg = agg.reset_index()

    # scores por cuartiles (1..4) — recency invertido
    agg["r_score"] = pd.qcut(agg["recency"].rank(method="first"), 4, labels=[4, 3, 2, 1]).astype(int)
    agg["f_score"] = pd.qcut(agg["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
    agg["m_score"] = pd.qcut(agg["monetary"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)

    agg["rfm_score"] = agg["r_score"].astype(str) + agg["f_score"].astype(str) + agg["m_score"].astype(str)

    # etiqueta simple de segmento
    def label_row(row: pd.Series) -> str:
        s = (row["r_score"] + row["f_score"] + row["m_score"]) / 3
        if s >= 3.5:
            return "Champions"
        if s >= 2.5:
            return "Loyal"
        if s >= 1.5:
            return "Needs Attention"
        return "At Risk"

    agg["segment"] = agg.apply(label_row, axis=1)

    # si tenemos clientes, intentar mapear nombre
    if clientes is not None:
        cust_id_col = find_customer_col(clientes) or clientes.columns[0]
        clientes_map = clientes.set_index(cust_id_col).to_dict(orient="index")
        # try to map name field heuristically
        name_col = None
        for c in clientes.columns:
            if "nombre" in c.lower() or "name" in c.lower():
                name_col = c
                break
        if name_col:
            # create a mapping from id to name
            id_to_name = {str(k): v[name_col] for k, v in clientes_map.items() if name_col in v}
            agg["name"] = agg["_customer"].map(id_to_name)

    return agg.sort_values(["monetary"], ascending=False)


def plot_rfm(agg: pd.DataFrame, out_path: Path) -> None:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=agg, y="segment", order=agg["segment"].value_counts().index)
    plt.title("Conteo por segmento RFM")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_top_products(detalle: Optional[pd.DataFrame], productos: Optional[pd.DataFrame], out_path: Path) -> None:
    if detalle is None:
        print("No hay detalle de ventas; se omite top productos")
        return
    # intentar identificar columnas
    prod_col = None
    qty_col = None
    price_col = None
    for c in detalle.columns:
        lc = c.lower()
        if "prod" in lc or "producto" in lc:
            prod_col = c
        if "cant" in lc or "cantidad" in lc:
            qty_col = c
        if "precio" in lc or "valor" in lc:
            price_col = c
    if prod_col is None or qty_col is None:
        print("No se encontraron columnas product/cantidad en detalle; omitiendo top productos")
        return
    detalle = detalle.copy()
    detalle[qty_col] = pd.to_numeric(detalle[qty_col], errors="coerce").fillna(0)
    if price_col is not None:
        detalle[price_col] = pd.to_numeric(detalle[price_col], errors="coerce").fillna(0)
        detalle["line_total"] = detalle[qty_col] * detalle[price_col]
    else:
        detalle["line_total"] = detalle[qty_col]

    top = detalle.groupby(prod_col)["line_total"].sum().nlargest(10)
    df_top = top.reset_index().rename(columns={prod_col: "product", "line_total": "revenue"})

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_top, y="product", x="revenue", palette="viridis")
    plt.title("Top 10 productos por ingreso")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main() -> int:
    print("Buscando archivos de datos...")
    ventas_p = locate_file(Filenames["ventas"])
    detalle_p = locate_file(Filenames["detalle"])
    clientes_p = locate_file(Filenames["clientes"])
    productos_p = locate_file(Filenames["productos"])

    if ventas_p is None:
        print("No se encontró archivo de ventas. Busqué en:")
        for p in SEARCH_PATHS:
            print("  -", p)
        return 2

    print(f"Ventas: {ventas_p}")
    ventas = load_df(ventas_p)
    detalle = load_df(detalle_p) if detalle_p is not None else None
    clientes = load_df(clientes_p) if clientes_p is not None else None
    productos = load_df(productos_p) if productos_p is not None else None

    print("Limpiando datos básicos...")
    if clean_df is not None:
        try:
            ventas = clean_df(ventas)
            if detalle is not None:
                detalle = clean_df(detalle)
            if clientes is not None:
                clientes = clean_df(clientes)
        except Exception:
            # no crítico
            pass

    print("Calculando RFM por cliente...")
    try:
        agg = compute_rfm(ventas, detalle, clientes)
    except Exception as e:
        print("Error calculando RFM:", e)
        return 3

    out_csv = REPORT_DIR / "rfm_summary.csv"
    agg.to_csv(out_csv, index=False)
    print(f"Guardado RFM resumen en: {out_csv}")

    print("Generando gráficos...")
    plot_rfm(agg, REPORT_DIR / "rfm_segment_counts.png")
    plot_top_products(detalle, productos, REPORT_DIR / "top_products.png")

    print("Hecho. Archivos generados en:")
    for p in REPORT_DIR.iterdir():
        print(" -", p.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
