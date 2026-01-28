from core.layer import Layer
from core.cell import Cell

class ArenaLog(Cell):
    def __init__(self):
        super().__init__("Arena Findings Log")
        self.entries = []

    def log(self, msg):
        self.entries.append(msg)

def build_purgatory():
    layer = Layer(7, "PURGATORY")

    cells = [
        "Arena Cell",
        "Recon Cell",
        "Vulnerability Scan",
        "Exploit Simulation",
        "Auth & Crypto Test",
        "Forensics",
    ]

    for c in cells:
        layer.add_cell(Cell(c))

    layer.add_cell(ArenaLog())
    return layer
