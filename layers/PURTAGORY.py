from core.layer import Layer
from core.cell import Cell

def build_purgatory():
    layer = Layer(7, "PURGATORY")

    cells = [
        "Arena Cell",
        "Recon Cell",
        "Vulnerability Scan",
        "Exploit Simulation",
        "Crypto Test",
        "Forensics",
        "Arena Log"
    ]

    for c in cells:
        layer.add_cell(Cell(c))

    return layer
