from typing import List, Optional
from .cell import Cell
from .file import GridFile
from .firewall import Firewall

class Layer:
    def __init__(self, index: int, name: str, description: str = ""):
        self.index = index
        self.name = name
        self.description = description
        self.cells: List[Cell] = []
        self.firewall: Optional[Firewall] = None

    def add_cell(self, cell: Cell):
        self.cells.append(cell)
        print(f"[{self.name}] Added cell: {cell.name}")

    def attach_firewall(self, firewall: Firewall):
        self.firewall = firewall
        print(f"[{self.name}] Firewall attached: {firewall.name}")

    def receive_file(self, file: GridFile):
        # Layer-level firewall first
        if self.firewall and not self.firewall.scan(file):
            print(f"[{self.name}] Firewall blocked file: {file.name}")
            return
        for cell in self.cells:
            cell.receive_file(file, self.name)
