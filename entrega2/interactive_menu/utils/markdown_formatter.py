"""
Funciones para formatear Markdown en la terminal con colores ANSI.
"""
import re
from .colors import Colors

def format_markdown_line(line):
    """
    Formatea una línea de Markdown para visualización en terminal.
    
    Args:
        line (str): Línea de texto en formato Markdown
        
    Returns:
        str: Línea formateada con códigos de color ANSI
    """
    text = line.strip()
    
    # Headers H3
    if text.startswith("### "):
        return f"{Colors.YELLOW}{Colors.BOLD}{text[4:]}{Colors.RESET}"
    
    # Bold text **text**
    text = re.sub(r'\*\*(.+?)\*\*', rf'{Colors.BOLD}\1{Colors.RESET}', text)
    
    # Italic text *text* (solo si no es parte de **)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', rf'{Colors.UNDERLINE}\1{Colors.RESET}', text)
    
    # Code inline `code`
    text = re.sub(r'`(.+?)`', rf'{Colors.CYAN}\1{Colors.RESET}', text)
    
    # Bullet points
    if text.startswith("* ") or text.startswith("- "):
        return f"  {Colors.GREEN}•{Colors.RESET} {text[2:]}"
    
    # Numbered lists
    if re.match(r'^\d+\.\s', text):
        return f"  {Colors.GREEN}{text}{Colors.RESET}"
    
    # Horizontal rules
    if text.startswith("---") or text == "=" * len(text):
        return f"{Colors.BLUE}{'─' * 60}{Colors.RESET}"
    
    # Links [text](url)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', rf'{Colors.BLUE}{Colors.UNDERLINE}\1{Colors.RESET}', text)
    
    return text if text else ""

def render_content(lines, format_code_blocks = True):
    """
    Renderiza un conjunto de líneas con formato Markdown.
    
    Args:
        lines (list): Lista de líneas a formatear
        format_code_blocks (bool): Si se deben formatear bloques de código
        
    Yields:
        str: Líneas formateadas una por una
    """
    in_code_block = False
    
    for line in lines:
        # Detectar bloques de código ```
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            if format_code_blocks:
                yield f"{Colors.CYAN}{'─' * 60}{Colors.RESET}"
            continue
        
        if in_code_block:
            # Mostrar código sin formatear, solo con color
            yield f"{Colors.CYAN}{line}{Colors.RESET}"
        else:
            # Aplicar formato Markdown
            yield format_markdown_line(line)