from core.layer import Layer
from core.cell import Cell

def build_limbo():
    layer = Layer(0, "LIMBO")

    cells = [
        "Moat Cell",
        "Gate Cell",
        "Sentinel Guard HQ",
        "Firewall Cell",
        "Portcullis Cell",
        "Checkpoint Cell",
        "Network Honeypot Cell",
        "Dockyard Cell",
        "Library Cell",
        "Audit Log Cell"
    ]

    for c in cells:
        layer.add_cell(Cell(c))

    return layer
