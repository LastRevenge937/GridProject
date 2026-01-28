from typing import List, Optional
from .layer import Layer
from .file import GridFile
from .firewall import Firewall

class GridManager:
    def __init__(self, castle_name: str):
        self.castle_name = castle_name
        self.layers: List[Layer] = []
        self.global_firewall: Optional[Firewall] = None

    def attach_global_firewall(self, firewall: Firewall):
        self.global_firewall = firewall
        print(f"[Grid] Global Firewall attached: {firewall.name}")

    def add_layer(self, layer: Layer):
        self.layers.append(layer)
        print(f"[Grid] Added layer: {layer.name}")

    def receive_file(self, file: GridFile):
        # Global firewall check
        if self.global_firewall and not self.global_firewall.scan(file):
            print(f"[Grid] Global Firewall blocked file: {file.name}")
            return
        # Layer-level delivery
        for layer in self.layers:
            layer.receive_file(file)

    def generate_all_layers(self):
        # Placeholder for layer creation
        for i in range(12):
            self.add_layer(Layer(i, f"Layer {i}"))

    def boot_layers(self):
        for layer in self.layers:
            print(f"[Layer {layer.index}: {layer.name}] Online")


class GridManager:
    def __init__(self, castle_name: str):
        self.castle_name = castle_name
        self.layers = []
        self.global_firewall = None
        self.firewall_events = []

    def attach_global_firewall(self, firewall):
        self.global_firewall = firewall
        self.log_global(f"Global Firewall attached: {firewall.name}")

    def log_firewall_event(self, message: str):
        self.firewall_events.append(message)
        self.log_global(f"[FIREWALL] {message}")

