"""Visor interactivo de documentación para el proyecto Aurelion.

Lee archivos Markdown y permite navegar por secciones mediante un menú.
Este módulo contiene funciones pequeñas y bien tipadas para facilitar su
lectura y pruebas.
"""
from __future__ import annotations

import os
from typing import Dict, List, Optional

from .utils import Colors, clear_screen, format_markdown_line, render_content

DEFAULT_MD_FILENAME = "README.md"


def load_file(path: str) -> List[str]:
    """Leer un archivo de texto y devolver sus líneas.

    Args:
        path: Ruta al archivo a leer.

    Returns:
        Lista de líneas (sin saltos de línea).

    Raises:
        FileNotFoundError: si el archivo no existe.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def parse_document(lines: List[str]) -> List[Dict]:
    """Parsear líneas Markdown en una estructura de secciones.

    Se consideran H1 (`# `) como secciones principales y H2 (`## `) como
    subsecciones.
    """
    sections: List[Dict] = []
    current_section: Optional[Dict] = None
    current_subsection: Optional[Dict] = None

    for line in lines:
        text = line.lstrip()

        if text.startswith("# "):
            title = text[2:].strip()
            current_section = {"titulo": title, "contenido": [], "subsecciones": []}
            sections.append(current_section)
            current_subsection = None

        elif text.startswith("## "):
            title = text[3:].strip()
            if current_section is None:
                current_section = {"titulo": "INTRODUCCIÓN", "contenido": [], "subsecciones": []}
                sections.append(current_section)
            current_subsection = {"titulo": title, "contenido": []}
            current_section["subsecciones"].append(current_subsection)

        else:
            if current_subsection is not None:
                current_subsection["contenido"].append(line)
            elif current_section is not None:
                current_section["contenido"].append(line)

    return sections

def find_section(sections: List[Dict], prefix: str) -> Optional[Dict]:
    """Buscar una sección cuyo título empiece por el prefijo dado (insensible a mayúsculas)."""
    prefix_lower = prefix.lower()
    for sec in sections:
        if sec["titulo"].lower().startswith(prefix_lower):
            return sec
    return None

def find_subsection(section: Dict, prefix: str) -> Optional[Dict]:
    """Buscar una subsección dentro de una sección por prefijo."""
    prefix_lower = prefix.lower()
    for sub in section.get("subsecciones", []):
        if sub["titulo"].lower().startswith(prefix_lower):
            return sub
    return None

def show_subsections(section: Dict, keys: Optional[List[str]] = None) -> None:
    """Imprimir una sección o subsecciones específicas con formato."""
    if keys:
        for key in keys:
            sub = find_subsection(section, key)
            if not sub:
                print(f"\n{Colors.RED}[Subsección '{key}' no encontrada]{Colors.RESET}")
                continue
            print(f"\n{Colors.CYAN}{Colors.BOLD}{sub['titulo']}{Colors.RESET}")
            print(f"{Colors.CYAN}{'-' * len(sub['titulo'])}{Colors.RESET}")
            for line in sub["contenido"]:
                formatted = format_markdown_line(line)
                if formatted:
                    print(formatted)
            if not sub["contenido"] or not any(sub["contenido"]):
                print(f"{Colors.YELLOW}[sin contenido]{Colors.RESET}")
    else:
        print(f"\n{Colors.HEADER}{Colors.BOLD}{section['titulo']}{Colors.RESET}")
        print(f"{Colors.HEADER}{'=' * len(section['titulo'])}{Colors.RESET}")
        if section["contenido"]:
            for line in section["contenido"]:
                formatted = format_markdown_line(line)
                if formatted:
                    print(formatted)
        for sub in section.get("subsecciones", []):
            print(f"\n{Colors.CYAN}{Colors.BOLD}{sub['titulo']}{Colors.RESET}")
            print(f"{Colors.CYAN}{'-' * len(sub['titulo'])}{Colors.RESET}")
            for line in sub["contenido"]:
                formatted = format_markdown_line(line)
                if formatted:
                    print(formatted)
            if not sub["contenido"] or not any(sub["contenido"]):
                print(f"{Colors.YELLOW}[sin contenido]{Colors.RESET}")

def show_notebooks_menu():
    """Muestra información sobre los notebooks de análisis."""
    notebooks = [
        {
            "nombre": "01 - Exploración de Datos",
            "archivo": "01_exploracion_datos.ipynb",
            "descripcion": "Limpieza y exploración inicial de datos. Validación de calidad y creación de dataset consolidado.",
            "contenido": ["Inspección de datasets", "Limpieza de datos", "Visualizaciones exploratorias", "Matriz de correlación"]
        },
        {
            "nombre": "02 - Análisis de Productos",
            "archivo": "02_analisis_productos.ipynb",
            "descripcion": "Análisis de rendimiento de productos y categorías.",
            "contenido": ["Top productos", "Ingresos por categoría", "Análisis de precios", "Correlación de métricas"]
        },
        {
            "nombre": "03 - Análisis de Clientes",
            "archivo": "03_analisis_clientes.ipynb",
            "descripcion": "Segmentación de clientes y análisis de comportamiento.",
            "contenido": ["Segmentación RFM", "Distribución geográfica", "Medios de pago", "Top clientes"]
        },
        {
            "nombre": "04 - Análisis de Ventas",
            "archivo": "04_analisis_ventas.ipynb",
            "descripcion": "Análisis temporal de ventas y tendencias.",
            "contenido": ["Evolución mensual", "Tendencias diarias", "Patrones semanales", "Distribución de tickets"]
        }
    ]

    print(f"\n{Colors.HEADER}{Colors.BOLD}ANÁLISIS DE DATOS - NOTEBOOKS DISPONIBLES{Colors.RESET}")
    print(f"{Colors.HEADER}{'=' * 60}{Colors.RESET}\n")

    for i, nb in enumerate(notebooks, 1):
        print(f"{Colors.CYAN}{Colors.BOLD}{i}. {nb['nombre']}{Colors.RESET}")
        print(f"   {Colors.YELLOW}Archivo:{Colors.RESET} {nb['archivo']}")
        print(f"   {nb['descripcion']}")
        print(f"   {Colors.GREEN}Contenido:{Colors.RESET}")
        for item in nb['contenido']:
            print(f"     • {item}")
        print()

    print(f"{Colors.YELLOW}Para abrir un notebook:{Colors.RESET}")
    print(f"  jupyter notebook notebooks/{Colors.CYAN}<nombre_archivo>{Colors.RESET}\n")
    print(f"{Colors.YELLOW}Ubicación:{Colors.RESET} ./notebooks/\n")

def show_menu():
    """Muestra el menú de opciones."""
    print("\n" + f"{Colors.BLUE}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.HEADER} VISOR DE DOCUMENTACIÓN - TIENDA AURELION{Colors.RESET}")
    print(f"{Colors.BLUE}{'=' * 60}{Colors.RESET}")
    print(f" {Colors.GREEN}1){Colors.RESET} Tema, Problema y Solución")
    print(f" {Colors.GREEN}2){Colors.RESET} Dataset de Referencia (Completo)")
    print(f" {Colors.GREEN}3){Colors.RESET} Escala de la Base de Datos (Volumen)")
    print(f" {Colors.GREEN}4){Colors.RESET} Información del Programa")
    print(f" {Colors.GREEN}5){Colors.RESET} Mostrar documento completo")
    print(f" {Colors.CYAN}6){Colors.RESET} Análisis de Datos (Notebooks)")
    print(f" {Colors.RED}0){Colors.RESET} Salir")
    print(f"{Colors.BLUE}{'=' * 60}{Colors.RESET}")

def main():
    """Función principal del programa."""
    # Cargar y parsear el archivo (buscar en el directorio padre)
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(parent_dir, DEFAULT_MD_FILENAME)
    try:
        lines = load_file(path)
    except FileNotFoundError:
        print(f"{Colors.RED}Error: archivo de documentación no encontrado en {path}{Colors.RESET}")
        return
    sections = parse_document(lines)
    
    if not sections:
        print(f"{Colors.RED}Error: No se encontraron secciones en el archivo.{Colors.RESET}")
        return
    
    # Localizar secciones principales
    first_section = sections[0]
    dataset_section = find_section(sections, "Dataset")
    program_section = find_section(sections, "Programa")
    
    # Buscar subsección de escala dentro de Dataset
    scale_subsection = None
    if dataset_section:
        scale_subsection = find_subsection(dataset_section, "Escala")
    
    # Loop del menú
    while True:
        clear_screen()
        show_menu()
        
        try:
            option = input(f"\n{Colors.YELLOW} ➤  Seleccione una opción: {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n{Colors.GREEN} Saliendo...{Colors.RESET}")
            return
        
        if option == "0":
            print(f"\n{Colors.GREEN} Saliendo...{Colors.RESET}")
            return
        
        elif option == "1":
            show_subsections(first_section, ["Tema", "Problema", "Solución"])
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")
        
        elif option == "2":
            if dataset_section:
                show_subsections(dataset_section)
            else:
                print(f"\n{Colors.RED}[Error: Sección 'Dataset de Referencia' no encontrada]{Colors.RESET}")
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")
        
        elif option == "3":
            if scale_subsection:
                print(f"\n{Colors.CYAN}{Colors.BOLD}{scale_subsection['titulo']}{Colors.RESET}")
                print(f"{Colors.CYAN}{'-' * len(scale_subsection['titulo'])}{Colors.RESET}")
                
                # Formatear cada línea del contenido
                for line in scale_subsection["contenido"]:
                    formatted = format_markdown_line(line)
                    if formatted:
                        print(formatted)
                
                if not scale_subsection["contenido"] or not any(scale_subsection["contenido"]):
                    print(f"{Colors.YELLOW}[sin contenido]{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}[Error: Subsección 'Escala' no encontrada]{Colors.RESET}")
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")
        
        elif option == "4":
            if program_section:
                show_subsections(program_section)
            else:
                print(f"\n{Colors.RED}[Error: Sección 'Programa' no encontrada]{Colors.RESET}")
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")
        
        elif option == "5":
            print("\n" + f"{Colors.BLUE}{'=' * 60}{Colors.RESET}")
            print(f"{Colors.BOLD}CONTENIDO COMPLETO{Colors.RESET}")
            print(f"{Colors.BLUE}{'=' * 60}{Colors.RESET}\n")

            # Renderizar todo el documento
            for formatted_line in render_content(lines):
                print(formatted_line)

            print("\n" + f"{Colors.BLUE}{'=' * 60}{Colors.RESET}")
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")

        elif option == "6":
            show_notebooks_menu()
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")

        else:
            print(f"\n{Colors.RED}[Opción inválida. Ingrese 0-6]{Colors.RESET}")
            input(f"\n{Colors.YELLOW}Presione ENTER para continuar...{Colors.RESET}")

if __name__ == "__main__":
    main()
    # Ejecuta el comando: python interactive_menu/main.py