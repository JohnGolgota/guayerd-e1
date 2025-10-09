class SistemaGestionVentas:
    def __init__(self):
        self.documentacion = {
            'tema': "Sistema de Gestión de Ventas para E-commerce - Plataforma integral para administrar operaciones comerciales digitales",
            'problema': """
Problemáticas identificadas en la gestión manual del e-commerce:
• Errores en transacciones por cálculo manual de precios y cantidades
• Duplicación o pérdida de información de clientes
• Errores en precios y cantidades de productos
• Dificultades para obtener reportes sobre ventas y medios de pago
• Poca trazabilidad en el historial de compras de los clientes

Estas dificultades afectan la eficiencia, experiencia del cliente y toma de decisiones estratégicas.
            """,
            'solucion': """
Solución: Sistema Relacional Integrado que centraliza y automatiza:

Cliente → Ventas → Detalle_Ventas → Productos
    ↓
Analytics & Reporting

Beneficios implementados:
• Generación automática de reportes
• Trazabilidad completa del customer journey
• Centralización de información de clientes, productos y ventas
• Mejor precisión y consistencia de datos
• Optimización de la toma de decisiones
            """,
            'tablas': """
Tablas disponibles en el sistema:
1. ventas (120 registros)
2. productos (100 registros) 
3. detalle_ventas (343 registros)
4. clientes (100 registros)

Relaciones principales:
• Clientes 1:N Ventas
• Ventas 1:N Detalle_Ventas  
• Productos 1:N Detalle_Ventas
            """,
            'metricas': """
Métricas del sistema basadas en la documentación:
• Total clientes: 100 registros
• Total productos: 100 registros  
• Total ventas: 120 transacciones
• Detalles de venta: 343 registros
• Densidad productos/venta: 2.85 promedio
• Medios de pago: tarjeta, qr, transferencia, efectivo
            """
        }

    def mostrar_menu(self):
        print("\n" + "=" * 60)
        print("       SISTEMA DE GESTIÓN DE VENTAS - E-COMMERCE")
        print("=" * 60)
        print("1. 📋 Ver documentación completa del proyecto")
        print("2. 🔍 Consultar estructura detallada de tablas")
        print("3. 📊 Ver métricas y estadísticas del sistema")
        print("4. 🔄 Diagrama de flujo y relaciones")
        print("5. 💡 Sugerencias de Copilot implementadas")
        print("6. 🚪 Salir del sistema")
        print("=" * 60)

    def mostrar_documentacion(self):
        print("\n" + "📋 DOCUMENTACIÓN COMPLETA DEL PROYECTO")
        print("=" * 60)
        for key, value in self.documentacion.items():
            print(f"\n{key.upper()}:\n{value}")
            print("-" * 40)

    def mostrar_estructura_tablas(self):
        print("\n" + "🔍 ESTRUCTURA DETALLADA DE TABLAS")
        print("=" * 60)

        estructuras = {
            'ventas (120 registros)': {
                'columnas': ['id_venta (PK, INT)', 'fecha (DATE)', 'id_cliente (FK, INT)',
                             'nombre_cliente (VARCHAR(100))', 'email (VARCHAR(150))',
                             'medio_pago (ENUM)'],
                'descripcion': 'Tabla principal de transacciones de venta'
            },
            'productos (100 registros)': {
                'columnas': ['id_producto (PK, INT)', 'nombre_producto (VARCHAR(200))',
                             'categoria (VARCHAR(100))', 'precio_unitario (DECIMAL(10,2))'],
                'descripcion': 'Catálogo de productos disponibles'
            },
            'detalle_ventas (343 registros)': {
                'columnas': ['id_venta (FK, INT)', 'id_producto (FK, INT)',
                             'nombre_producto (VARCHAR(200))', 'cantidad (INT)',
                             'precio_unitario (DECIMAL(10,2))', 'importe (DECIMAL(12,2))'],
                'descripcion': 'Tabla pivote que relaciona ventas con productos'
            },
            'clientes (100 registros)': {
                'columnas': ['id_cliente (PK, INT)', 'nombre_cliente (VARCHAR(100))',
                             'email (VARCHAR(150))', 'ciudad (VARCHAR(100))',
                             'fecha_alta (DATE)'],
                'descripcion': 'Registro de clientes del sistema'
            }
        }

        for tabla, info in estructuras.items():
            print(f"\n📊 {tabla.upper()}")
            print(f"   Descripción: {info['descripcion']}")
            print("   Columnas:")
            for columna in info['columnas']:
                print(f"     └─ {columna}")

    def mostrar_metricas(self):
        print("\n" + "📊 MÉTRICAS Y ESTADÍSTICAS DEL SISTEMA")
        print("=" * 60)

        metricas = [
            ("Total Clientes", "100", "Registros únicos en sistema"),
            ("Total Productos", "100", "Inventario activo"),
            ("Total Ventas", "120", "Transacciones completadas"),
            ("Detalles de Ventas", "343", "Items vendidos en total"),
            ("Productos por Venta", "2.85", "Densidad promedio"),
            ("Medios de Pago", "4 tipos", "tarjeta, qr, transferencia, efectivo"),
            ("Relaciones", "1:N principales", "Clientes→Ventas, Ventas→Detalles, Productos→Detalles")
        ]

        for nombre, valor, descripcion in metricas:
            print(f"• {nombre}: {valor} - {descripcion}")

        print(f"\n💡 Observación: La tabla detalle_ventas funciona como tabla pivote")
        print("  conectando ventas con productos, con un promedio de 2.85 productos por venta")

    def mostrar_diagrama(self):
        print("\n" + "🔄 DIAGRAMA DE RELACIONES Y FLUJO DEL SISTEMA")
        print("=" * 60)
        print("""
        RELACIONES ENTRE TABLAS (Modelo Entidad-Relación):

        CLIENTES (100) ||--o{ VENTAS (120) : realiza
        VENTAS (120) ||--o{ DETALLE_VENTAS (343) : contiene  
        PRODUCTOS (100) ||--o{ DETALLE_VENTAS (343) : aparece_en

        FLUJO DEL SISTEMA:

        ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
        │    CLIENTES     │    │     VENTAS      │    │   PRODUCTOS     │
        │                 │    │                 │    │                 │
        │ • id_cliente (PK)│    │ • id_venta (PK) │    │ • id_producto(PK)│
        │ • nombre        │    │ • fecha         │    │ • nombre        │
        │ • email         │    │ • id_cliente(FK)│    │ • categoria     │
        │ • ciudad        │    │ • medio_pago    │    │ • precio        │
        │ • fecha_alta    │    │ • nombre_cliente│    └────────┬────────┘
        └────────┬────────┘    │ • email        │              │
                 │             └────────┬────────┘              │
                 │                      │                       │
                 └──────────────────────┼───────────────────────┘
                                        │
                                        ▼
                            ┌─────────────────────┐
                            │ DETALLE_VENTAS (343)│
                            │                     │
                            │ • id_venta (FK)     │
                            │ • id_producto (FK)  │
                            │ • nombre_producto   │
                            │ • cantidad          │
                            │ • precio_unitario   │
                            │ • importe           │
                            └─────────────────────┘
        """)

    def mostrar_sugerencias_copilot(self):
        print("\n" + "💡 SUGERENCIAS DE COPILOT IMPLEMENTADAS")
        print("=" * 60)

        print("\n✅ ACEPTADAS:")
        sugerencias_aceptadas = [
            "Organización modular del código en clases",
            "Manejo robusto de entradas de usuario",
            "Representación visual mejorada de datos",
            "Métricas cuantificables para demostrar impacto",
            "Documentación interactiva con navegación fluida"
        ]

        for i, sugerencia in enumerate(sugerencias_aceptadas, 1):
            print(f"  {i}. {sugerencia}")

        print("\n❌ DESCARTADAS:")
        sugerencias_descartadas = [
            "Integración directa con base de datos (fuera del alcance)",
            "Funciones de escritura/actualización (solo consulta)",
            "Interfaz gráfica (mantener enfoque en CLI)"
        ]

        for i, sugerencia in enumerate(sugerencias_descartadas, 1):
            print(f"  {i}. {sugerencia}")

    def ejecutar(self):
        print("🚀 INICIANDO SISTEMA DE GESTIÓN DE VENTAS")
        print("   Basado en la documentación del proyecto E-commerce")

        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción (1-6): ").strip()

            if opcion == '1':
                self.mostrar_documentacion()
            elif opcion == '2':
                self.mostrar_estructura_tablas()
            elif opcion == '3':
                self.mostrar_metricas()
            elif opcion == '4':
                self.mostrar_diagrama()
            elif opcion == '5':
                self.mostrar_sugerencias_copilot()
            elif opcion == '6':
                print("\n" + "=" * 50)
                print("¡Gracias por usar el Sistema de Gestión de Ventas!")
                print("Documentación basada en el proyecto E-commerce")
                print("=" * 50)
                break
            else:
                print("\n❌ Opción inválida. Por favor, seleccione 1-6.")

            input("\n📍 Presione Enter para volver al menú principal...")


# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaGestionVentas()
    sistema.ejecutar()