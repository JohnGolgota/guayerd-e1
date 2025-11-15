# Tienda Aurelion - Análisis de Datos de Ventas

## Estructura del Proyecto

```
aurelion_shop/
├── documentacion.md                       # Documentación del proyecto
│
├── interactive_menu/                      # Módulo de menú interactivo
│   ├── main.py                            # Visor de documentación
|   ├── docs/
|   |   └── flowchart.mmd
|   |
│   └── utils/                             # Utilidades del menú
│       ├── __init__.py
│       ├── colors.py                      # Configuración de colores ANSI
│       └── markdown_formatter.py          # Formato de Markdown
│
├── notebooks/                             # Análisis de datos
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_analisis_productos.ipynb
│   ├── 03_analisis_clientes.ipynb
│   ├── 04_analisis_ventas.ipynb
│   └── README.md
│
└── data/                                  # Datasets
    ├── clientes.xlsx
    ├── detalle_ventas.xlsx
    ├── productos.xlsx
    └── ventas.xlsx
    └── processed/                         # Datos procesados
        └── datos_consolidados.xlsx
```

## Uso Rápido

### Ver la documentación interactivamente:

```bash
cd interactive_menu
python main.py
```

## Módulos

### `interactive_menu/`
Menú interactivo CLI para consultar la documentación del proyecto.

**Características:**
- Navegación por secciones H1 y H2
- Renderizado de Markdown con colores
- Interfaz limpia y fácil de usar
- Información sobre notebooks de análisis de datos (Opción 6)

**Archivos:**
- `main.py` - Punto de entrada del visor
- `docs/flowchart.mmd` - Diagrama de Flujo
- `utils/colors.py` - Colores ANSI para terminal
- `utils/markdown_formatter.py` - Formato de Markdown

## Documentación

La documentación completa del proyecto está en `documentation.md` y puede consultarse mediante el menú interactivo.

## Requisitos

- Python 3.12+
- Terminal con soporte de colores ANSI

## Personalización

Para personalizar colores o mensajes, edita:
- `interactive_menu/utils/colors.py` - Códigos de color
- `interactive_menu/main.py` - Mensajes y opciones del menú