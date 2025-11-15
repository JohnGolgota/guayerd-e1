# Tienda Aurelion

## Tema
Análisis de ventas de una tienda minorista mediante cuatro tablas relacionales: productos, clientes, ventas y detalle de ventas.

## Problema
Sin análisis adecuado, los datos no permiten identificar:
* Productos más/menos vendidos
* Clientes más valiosos y su distribución geográfica
* Patrones de pago y tendencias de ventas
* Oportunidades de optimización de inventario y precios

## Solución
Integrar los datos mediante campos comunes (id_producto, id_venta, id_cliente) para:
* Analizar rendimiento de productos y categorías
* Segmentar clientes por ciudad y comportamiento
* Identificar preferencias de pago
* Crear dashboards visuales para toma de decisiones

--------------------------------------------------------------------------

# Dataset de Referencia

## Fuente
Dataset sintético generado para fines educativos. Formato Excel (.xlsx), datos del año 2023 - 2024.

## Definición
Sistema de información de ventas con 4 tablas relacionales que simulan operaciones de una tienda minorista.

## Estructura

**Tablas:**
* `productos.xlsx` - Catálogo maestro
* `clientes.xlsx` - Base de clientes registrados
* `ventas.xlsx` - Transacciones principales
* `detalle_ventas.xlsx` - Desglose por producto

**Relaciones:**
* ventas ↔ detalle_ventas (por id_venta)
* ventas ↔ clientes (por id_cliente)
* detalle_ventas ↔ productos (por id_producto)

## Tipos y Escalas

**productos.xlsx:**
* id_producto: Entero - Nominal
* nombre_producto: Texto - Nominal
* categoria: Texto - Nominal
* precio_unitario: Decimal - Razón

**clientes.xlsx:**
* id_cliente: Entero - Nominal
* nombre_cliente: Texto - Nominal
* email: Texto - Nominal
* ciudad: Texto - Nominal
* fecha_alta: Fecha - Intervalo

**ventas.xlsx:**
* id_venta: Entero - Nominal
* fecha: Fecha - Intervalo
* id_cliente: Entero - Nominal
* nombre_cliente: Texto - Nominal
* email: Texto - Nominal
* medio_pago: Texto - Nominal

**detalle_ventas.xlsx:**
* id_venta: Entero - Nominal
* id_producto: Entero - Nominal
* nombre_producto: Texto - Nominal
* cantidad: Entero - Razón
* precio_unitario: Decimal - Razón
* importe: Decimal - Razón

## Escala (Volumen)
* Productos: 100 registros
* Clientes: 100 registros
* Ventas: 120 registros
* Detalle_ventas: 343 registros

Base de datos pequeña - mediana, manejable con herramientas estándar.

--------------------------------------------------------------------------

# Análisis de Datos (Notebooks)

## Descripción
Conjunto de 4 notebooks Jupyter optimizados para análisis visual de datos de la tienda.

## Notebooks Disponibles

**01_exploracion_datos.ipynb**
* Exploración inicial y limpieza de datos
* Validación de calidad de datos
* Creación de dataset consolidado
* Visualizaciones exploratorias y matriz de correlación

**02_analisis_productos.ipynb**
* Rendimiento por categoría
* Top 10 productos por ingresos y unidades
* Análisis de precios y correlaciones

**03_analisis_clientes.ipynb**
* Segmentación RFM (VIP, Potencial, Nuevo, Regular)
* Distribución geográfica
* Análisis de medios de pago
* Top 10 clientes

**04_analisis_ventas.ipynb**
* Evolución mensual y tendencias
* Patrones semanales
* Distribución de tickets
* Análisis de crecimiento

## Características
* **Visuales**: Enfoque en gráficas, mínimo texto
* **Concisos**: Solo insights clave
* **Profesionales**: Gráficas imprescindibles
* **Buenas prácticas**: Correlaciones, distribuciones, tendencias

## Ejecución
```bash
# Instalar dependencias
pip install pandas numpy matplotlib seaborn openpyxl

# Ejecutar notebooks
jupyter notebook notebooks/
```

--------------------------------------------------------------------------

# Programa de Consulta de Documentación

## Información
Aplicación CLI en Python que permite navegar interactivamente el archivo `documentation.md` mediante un menú con opciones predefinidas.

**Funcionalidades:**
* Carga y parseo automático del archivo MD
* Menú interactivo con 6 opciones
* Navegación por secciones H1 y H2
* Visualización selectiva o completa
* Información de notebooks de análisis de datos
* Manejo de errores

## Pseudocódigo

```
INICIO
  archivo = "documentacion.md"
  
  // Cargar
  INTENTAR abrir archivo con UTF-8
    SI error: mostrar mensaje y terminar
  lineas = leer todo el archivo
  
  // Parsear
  secciones = []
  PARA CADA linea:
    SI empieza con "# ": crear nueva sección H1
    SI empieza con "## ": crear nueva subsección H2
    SINO: agregar a contenido actual
  
  SI secciones vacío: error y terminar
  
  // Indexar
  primera_seccion = secciones[0]
  seccion_estructura = buscar("Estructura")
  subseccion_escala = buscar("Escala")
  
  // Loop principal
  MIENTRAS verdadero:
    mostrar_menu()
    opcion = leer_entrada()
    
    SI opcion = 0 O Ctrl+C: salir
    SI opcion = 1: mostrar Tema/Problema/Solución
    SI opcion = 2: mostrar Estructura completa
    SI opcion = 3: mostrar Escala
    SI opcion = 4: mostrar todo
    SINO: opción inválida
FIN
```

# Sugerencias con Copilot

## Aceptadas

**1. Codificación UTF-8 explícita**
```python
with open(ruta, "r", encoding = "utf-8") as f:
```
Compatibilidad con acentos y eñes

**2. Manejo de interrupciones**
```python
except (EOFError, KeyboardInterrupt):
```
Salida controlada con Ctrl+C/D

**3. Búsqueda case-insensitive**
```python
titulo.lower().startswith(prefijo.lower())
```
Mayor flexibilidad para el usuario

**4. Separadores dinámicos**
```python
"-" * len(titulo)
```
Mejor presentación visual