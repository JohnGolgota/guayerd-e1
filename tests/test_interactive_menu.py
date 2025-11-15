import importlib.util
import importlib
import sys
import types
from pathlib import Path


def load_module_from_path() -> object:
    repo_root = Path(__file__).resolve().parents[1]
    mod_path = repo_root / "entrega2" / "interactive_menu" / "main.py"

    # Prepare package placeholders so relative imports inside the module work
    pkg = "entrega2"
    subpkg = "entrega2.interactive_menu"
    if pkg not in sys.modules:
        sys.modules[pkg] = types.ModuleType(pkg)
    # marcar la ruta del paquete para que los imports relativos funcionen
    sys.modules[pkg].__path__ = [str(repo_root / "entrega2")]
    if subpkg not in sys.modules:
        sys.modules[subpkg] = types.ModuleType(subpkg)
    sys.modules[subpkg].__path__ = [str(repo_root / "entrega2" / "interactive_menu")]

    spec = importlib.util.spec_from_file_location(subpkg + ".main", str(mod_path))
    mod = importlib.util.module_from_spec(spec)
    # set package so relative imports resolve
    mod.__package__ = subpkg
    spec.loader.exec_module(mod)  # type: ignore
    return mod


def test_parse_document_basic():
    mod = load_module_from_path()
    lines = ["# Titulo", "Linea intro", "## Sub", "Contenido sub", "Otra linea"]
    sections = mod.parse_document(lines)
    assert isinstance(sections, list)
    assert sections[0]["titulo"] == "Titulo"
    assert len(sections[0]["subsecciones"]) == 1
    assert sections[0]["subsecciones"][0]["titulo"] == "Sub"
    assert sections[0]["subsecciones"][0]["contenido"] == ["Contenido sub", "Otra linea"]


def test_find_section_and_subsection():
    mod = load_module_from_path()
    lines = ["# Dataset", "info", "## Escala", "detalle"]
    sections = mod.parse_document(lines)
    sec = mod.find_section(sections, "Dataset")
    assert sec is not None and sec["titulo"] == "Dataset"
    sub = mod.find_subsection(sec, "Escala")
    assert sub is not None and sub["titulo"] == "Escala"


def test_load_file(tmp_path):
    mod = load_module_from_path()
    f = tmp_path / "tmp.md"
    f.write_text("# Hola\nlinea2")
    lines = mod.load_file(str(f))
    assert lines[0].startswith("# Hola")
