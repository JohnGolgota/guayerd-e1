# Notebooks Jupyter - Tienda Aurelion

Esta carpeta contiene todos los notebooks Jupyter (.ipynb) para el análisis de datos del proyecto **Tienda Aurelion**.

## 📊 Contexto del Proyecto

El proyecto analiza las ventas de una tienda minorista mediante cuatro tablas relacionales:
- **productos.xlsx** - Catálogo maestro (100 registros)
- **clientes.xlsx** - Base de clientes registrados (100 registros)  
- **ventas.xlsx** - Transacciones principales (120 registros)
- **detalle_ventas.xlsx** - Desglose por producto (343 registros)

## 📁 Notebooks Disponibles

```
notebooks/
├── 01_exploracion_datos.ipynb      # Exploración inicial de los datasets
├── 02_analisis_productos.ipynb     # Análisis de productos y categorías
├── 03_analisis_clientes.ipynb      # Segmentación y análisis de clientes
├── 04_analisis_ventas.ipynb        # Análisis de ventas y tendencias
└── README.md                       # Este archivo
```

## 🎯 Objetivos de Análisis

Los notebooks están diseñados para resolver los siguientes problemas:

### Análisis de Productos
- Identificar productos más/menos vendidos
- Analizar rendimiento por categorías
- Optimización de inventario y precios

### Análisis de Clientes
- Segmentar clientes por ciudad y comportamiento
- Identificar clientes más valiosos
- Análisis de distribución geográfica

### Análisis de Ventas
- Patrones de pago y tendencias temporales
- Análisis de rendimiento por período
- Identificación de oportunidades de crecimiento

## 🛠️ Configuración del Entorno

### Instalación de Dependencias

```bash
# Instalar Jupyter
pip install jupyter

# O si prefieres JupyterLab
pip install jupyterlab

# Dependencias para análisis de datos
pip install pandas numpy matplotlib seaborn plotly
```

### Ejecutar Notebooks

```bash
# Desde la raíz del proyecto
jupyter notebook notebooks/

# O con JupyterLab
jupyter lab notebooks/
```

## 📋 Descripción de Notebooks

### 01_exploracion_datos.ipynb
- **Propósito**: Exploración inicial y limpieza de datos
- **Contenido**:
  - Inspección de datasets (productos, clientes, ventas, detalle_ventas)
  - Limpieza y validación de datos
  - Creación de dataset consolidado
  - Visualizaciones exploratorias (distribución de precios, correlaciones, análisis temporal)
  - Matriz de correlación
- **Output**: Archivo consolidado en `data/processed/datos_consolidados.xlsx`

### 02_analisis_productos.ipynb
- **Propósito**: Análisis visual de productos y categorías
- **Contenido**:
  - Rendimiento por categoría (ingresos, unidades, participación)
  - Top 10 productos por ingresos y unidades
  - Análisis de precios (distribución, boxplot, scatter)
  - Correlación de métricas (precio, unidades, ingresos)
- **Enfoque**: Gráficas visuales y concretas, análisis directo

### 03_analisis_clientes.ipynb
- **Propósito**: Segmentación y comportamiento de clientes
- **Contenido**:
  - Segmentación RFM (VIP, Potencial, Nuevo, Regular)
  - Distribución geográfica por ciudad
  - Análisis de medios de pago
  - Top 10 clientes por ingresos
- **Enfoque**: Visualizaciones profesionales, segmentación estratégica

### 04_analisis_ventas.ipynb
- **Propósito**: Análisis temporal de ventas y tendencias
- **Contenido**:
  - Evolución mensual (ingresos, transacciones, ticket promedio, crecimiento)
  - Tendencias diarias
  - Patrones semanales (por día de la semana)
  - Distribución de tickets
- **Enfoque**: Series temporales, identificación de patrones y estacionalidad

## 🔗 Relaciones de Datos

Los notebooks deben considerar las siguientes relaciones:
- `ventas` ↔ `detalle_ventas` (por id_venta)
- `ventas` ↔ `clientes` (por id_cliente)
- `detalle_ventas` ↔ `productos` (por id_producto)

## 📊 Tipos de Datos

### Variables Nominales
- id_producto, id_cliente, id_venta
- nombre_producto, categoria, nombre_cliente
- email, ciudad, medio_pago

### Variables de Razón
- precio_unitario, cantidad, importe

### Variables de Intervalo
- fecha, fecha_alta

## 🎨 Visualizaciones Recomendadas

- **Gráficos de barras**: Productos más vendidos, ventas por ciudad
- **Gráficos de líneas**: Tendencias temporales de ventas
- **Gráficos circulares**: Distribución por categorías, medios de pago
- **Mapas de calor**: Análisis de correlaciones
- **Dashboards interactivos**: Resúmenes ejecutivos

## 📝 Notas Importantes

- Todos los notebooks deben incluir celdas de markdown con explicaciones
- Usar comentarios en español para mayor claridad
- Incluir celdas de limpieza de datos al inicio
- Exportar visualizaciones en alta resolución para reportes
- Mantener versionado de notebooks importantes

## ✅ Estado del Proyecto

- ✅ Notebook 01: Exploración y limpieza de datos - **COMPLETADO**
- ✅ Notebook 02: Análisis de productos - **COMPLETADO**
- ✅ Notebook 03: Análisis de clientes - **COMPLETADO**
- ✅ Notebook 04: Análisis de ventas - **COMPLETADO**
- ✅ Dataset consolidado generado
- ✅ Visualizaciones implementadas

## 🎯 Características de los Notebooks

Todos los notebooks optimizados siguen estas buenas prácticas:

- **Visuales**: Más gráficas, menos texto descriptivo
- **Concisos**: Solo insights clave y análisis directo
- **Profesionales**: Gráficas imprescindibles para el análisis
- **Buenas prácticas**: Análisis de correlaciones, distribuciones y tendencias
- **Limpios**: Código simple, sin complejidad innecesaria

## 🔄 Flujo de Trabajo Recomendado

1. **Ejecutar 01_exploracion_datos.ipynb** → Genera el dataset consolidado
2. **Ejecutar 02, 03, 04** en cualquier orden → Usan el dataset consolidado
3. Todos los análisis son independientes entre sí

---

**Proyecto**: Tienda Aurelion
**Versión**: 2.0
**Última actualización**: Noviembre 2025
