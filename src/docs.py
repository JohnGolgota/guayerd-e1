
class SistemaGestionVentas:
    def __init__(self):
        self.documentacion = {
            'tema': "Sistema de Gestión de Ventas para E-commerce",
            'problema': """
            Problemáticas identificadas:
            • Duplicación del 15% en registros de clientes
            • Errores en el 8% de transacciones
            • 3 horas promedio para generar reportes
            • Pérdida del 12% del historial de compras
            """,
            'solucion': """
            Solución implementada:
            • Base de datos relacional centralizada
            • Automatización de procesos
            • Reportes en tiempo real
            • Trazabilidad completa
            """,
            'tablas': """
            Tablas disponibles:
            1. ventas (120 registros)
            2. productos (100 registros) 
            3. detalle_ventas (343 registros)
            4. clientes (100 registros)
            """,
            'metricas': """
            Métricas del sistema:
            • Total clientes: 100
            • Total productos: 100  
            • Total ventas: 120
            • Productos por venta: 2.85
            """
        }
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("   SISTEMA DE GESTIÓN DE VENTAS")
        print("="*50)
        print("1. 📋 Ver documentación del proyecto")
        print("2. 🔍 Consultar estructura de tablas")
        print("3. 📊 Ver métricas y estadísticas")
        print("4. 🔄 Diagrama de flujo del sistema")
        print("5. 🚪 Salir")
        print("="*50)
    
    def mostrar_documentacion(self):
        print("\n" + "📋 DOCUMENTACIÓN DEL PROYECTO")
        print("-" * 40)
        for key, value in self.documentacion.items():
            print(f"\n{key.upper()}:\n{value}")
    
    def mostrar_estructura_tablas(self):
        print("\n" + "🔍 ESTRUCTURA DE TABLAS")
        print("-" * 40)
        
        estructuras = {
            'ventas': ['id_venta (PK)', 'fecha', 'id_cliente (FK)', 'nombre_cliente', 'email', 'medio_pago'],
            'productos': ['id_producto (PK)', 'nombre_producto', 'categoria', 'precio_unitario'],
            'detalle_ventas': ['id_venta (FK)', 'id_producto (FK)', 'nombre_producto', 'cantidad', 'precio_unitario', 'importe'],
            'clientes': ['id_cliente (PK)', 'nombre_cliente', 'email', 'ciudad', 'fecha_alta']
        }
        
        for tabla, columnas in estructuras.items():
            print(f"\n{tabla.upper()}:")
            for columna in columnas:
                print(f"  └─ {columna}")
    
    def mostrar_metricas(self):
        print("\n" + "📊 MÉTRICAS DEL SISTEMA")
        print("-" * 40)
        
        metricas = [
            ("Total Clientes", "100", "Registros únicos en sistema"),
            ("Total Productos", "100", "Inventario activo"),
            ("Total Ventas", "120", "Transacciones completadas"),
            ("Detalles Ventas", "343", "Items vendidos total"),
            ("Productos/Venta", "2.85", "Densidad promedio"),
            ("Categorías Productos", "5", "Alimentos, Limpieza, etc.")
        ]
        
        for nombre, valor, descripcion in metricas:
            print(f"• {nombre}: {valor} - {descripcion}")
    
    def mostrar_diagrama(self):
        print("\n" + "🔄 DIAGRAMA DE FLUJO DEL SISTEMA")
        print("-" * 40)
        print("""
        ┌─────────────────┐
        │  INICIO SISTEMA │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │   MENÚ PRINCIPAL│
        └────────┬────────┘
        ┌────────┼────────┐
        ▼        ▼        ▼
    CONSULTA  REPORTES GESTIÓN
       │         │        │
       ▼         ▼        ▼
    RESULTADOS ←───── OPERACIONES
        │
        ▼
    REGRESO A MENÚ
        """)
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción (1-5): ").strip()
            
            if opcion == '1':
                self.mostrar_documentacion()
            elif opcion == '2':
                self.mostrar_estructura_tablas()
            elif opcion == '3':
                self.mostrar_metricas()
            elif opcion == '4':
                self.mostrar_diagrama()
            elif opcion == '5':
                print("\n¡Gracias por usar el Sistema de Gestión de Ventas! 👋")
                break
            else:
                print("\n❌ Opción inválida. Por favor, seleccione 1-5.")
            
            input("\nPresione Enter para continuar...")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaGestionVentas()
    sistema.ejecutar()