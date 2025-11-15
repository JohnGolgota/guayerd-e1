"""
Configuración de colores ANSI para mejorar la visualización en terminal.
"""
import os

class Colors:
    """Códigos de color ANSI para formateo de terminal."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """
    Limpia la pantalla de la terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')