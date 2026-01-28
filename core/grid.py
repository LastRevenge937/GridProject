from core.layer import Layer
from layers.limbo import build_limbo
from layers.infrastructure import build_infrastructure
from layers.operations import build_operations
from layers.purgatory import build_purgatory

class GridManager:
    def __init__(self, castle_name: str):
        self.castle_name = castle_name
        self.layers = {}
        self.purge_active = False
        self.last_revenge_active = False

    def generate_all_layers(self):
        self.layers[0] = build_limbo()
        self.layers[2] = build_infrastructure()
        self.layers[3] = build_operations()
        self.layers[7] = build_purgatory()

        for i in range(12):
            if i not in self.layers:
                self.layers[i] = Layer(i, f"LAYER {i}")

    def boot_layers(self):
        for layer in self.layers.values():
            layer.boot()
            print(f"Layer {layer.index}: {layer.name} — Online")

    def activate_purge(self):
        self.purge_active = True
        for layer in self.layers.values():
            if layer.index not in (0, 7):
                layer.shutdown()

    def activate_last_revenge(self):
        self.last_revenge_active = True
        for layer in self.layers.values():
            if layer.index != 0:
                layer.shutdown()
