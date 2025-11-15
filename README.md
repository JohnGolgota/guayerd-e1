# Estadística interactiva sobre los CSV en `db/`

Este repositorio contiene utilidades y notebooks para limpiar y analizar los CSV ubicados en la carpeta `db/`.

## Origen y adaptaciones

Este repositorio se basa en un proyecto de ejemplo que sirvió como punto de partida. En lugar de ocultar esa procedencia, se ha decidido dejar constancia de la fuente y describir las adaptaciones realizadas o planeadas. Si conoces la URL o la referencia exacta del proyecto original, reemplaza el marcador [aurelion_shop](https://drive.google.com/drive/folders/1yQhz-sKzgsVkVXIDGVpCIsl2a16UXW_E?usp=drive_link) por la referencia concreta.

- Fuente original: [aurelion_shop](https://drive.google.com/drive/folders/1yQhz-sKzgsVkVXIDGVpCIsl2a16UXW_E?usp=drive_link) (reemplazar si conoces la URL o el autor).
- Adaptaciones realizadas o previstas:
	- Refactorización y limpieza de código en los módulos de carga y procesamiento de datos (`src/`).
	- Añadido de análisis propio y visualizaciones (por ejemplo, un notebook adicional `notebooks/05_mi_analisis.ipynb`).
	- Ampliación de pruebas unitarias en `tests/` para validar la carga y limpieza de CSVs.
	- Documentación adicional y notas para la entrega (`ENTREGA_NOTA.md`).

Nota sobre licencias: si la fuente original especifica una licencia (por ejemplo MIT, Apache, etc.), respeta sus términos y menciona la licencia aquí. Este reconocimiento es una práctica ética que evita malentendidos y muestra transparencia en la entrega.

Objetivos principales
- Inventariar los ficheros CSV y generar un resumen (`db/inventory.csv`).
- Proveer utilidades de carga y limpieza.
- Notebooks interactivos que muestren estadísticas descriptivas (cuartiles, medias, etc.) y visualizaciones (histograma, boxplot, conteos).

Dependencias
Instala las dependencias listadas en `requirements.txt`. Recomendado usar un virtualenv.

PowerShell (Windows / pwsh):
```powershell
# crear y activar virtualenv (opcional)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependencias
pip install -r requirements.txt
```

Linux / macOS (bash):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Uso rápido

- Generar inventario de CSV (genera `db/inventory.csv`):

```powershell
python src/inventory.py
```

Ejecutar tests

```powershell
# con el virtualenv activado
python -m pytest -q
```

Ejecutar el notebook de ejemplo

```powershell
jupyter lab notebooks/estadistica_basica.ipynb
# o
jupyter notebook notebooks/estadistica_basica.ipynb
```

Notas sobre los nombres de archivos

Algunos CSV en `db/` vienen con doble extensión (por ejemplo `ventas.csv.csv`). Puedes usar los nombres tal cual en las celdas del notebook o normalizarlos renombrando los ficheros. Si quieres, puedo automatizar ese paso y crear copias/respaldos antes de renombrar.

- Abrir el notebook de análisis (cuando exista):

```powershell
jupyter lab notebooks/estadistica_basica.ipynb
# o
jupyter notebook notebooks/estadistica_basica.ipynb
```

Siguientes pasos sugeridos
- Implementar `src/data.py` con utilidades `load_csv`, `summarize_df`, `clean_df`.
- Crear `notebooks/estadistica_basica.ipynb` con ejemplos de limpieza, cuartiles y gráficos.
- Añadir `src/visual.py` para encapsular las funciones de plot.

Notas
- El script `src/inventory.py` intenta leer CSVs con varios separadores y encodings comunes.
- Si tus ficheros están en otros formatos (por ejemplo Excel), instala `openpyxl` y usa `pandas.read_excel`.
# Indice
- [task:](./specs/requirements.md)
- [Documentación del Proyecto](./documentacion.md)
- [Diagrama de flujo](./documentacion.md#8-diagrama-de-flujo-del-sistema)
- [Programa interactivo](./documentacion.ipynb)

## Instrucciones

Recomendado usar vscode con las extensiones mencionadas en /.vscode/extensions.json

### Preparar el entorno

1. Crear un entorno virtual `python3 -m venv .venv`
2. Activar el entorno virtual
- en bash: `source .venv/bin/activate`
- powershell: `./.venv/bin/Activate.ps1`

## Auto referencia

[Repositorio](https://github.com/JohnGolgota/guayerd-e1)