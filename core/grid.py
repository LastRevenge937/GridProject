from core.protocols import ProtocolState
from core.protocol_visuals import ProtocolVisuals
from core.deadman import DeadManCore
from core.protocols import ProtocolState

class GridManager:
    def __init__(self, castle_name: str):
        self.castle_name = castle_name
        self.layers = {}
        self.protocol = ProtocolState.NORMAL
        self.global_log = []

    def log_global(self, message: str):
        self.global_log.append(message)

    def generate_all_layers(self):
        from layers.limbo import build_limbo
        from layers.infrastructure import build_infrastructure
        from layers.operations import build_operations
        from layers.purgatory import build_purgatory

        self.layers[0] = build_limbo()
        self.layers[2] = build_infrastructure()
        self.layers[3] = build_operations()
        self.layers[7] = build_purgatory()

        for i in range(12):
            if i not in self.layers:
                from core.layer import Layer
                self.layers[i] = Layer(i, f"LAYER {i}")

    def boot_layers(self):
        for layer in self.layers.values():
            layer.boot()
            print(f"Layer {layer.index}: {layer.name} — Online")

    def activate_purge(self):
        if self.protocol == ProtocolState.LAST_REVENGE:
            return

        self.protocol = ProtocolState.PURGE
        self.log_global("PURGE protocol activated")

        for idx, layer in self.layers.items():
            if idx not in (0, 7):
                layer.shutdown()

    def activate_last_revenge(self):
        self.protocol = ProtocolState.LAST_REVENGE
        self.log_global("LAST_REVENGE protocol activated")

        for idx, layer in self.layers.items():
            if idx != 0:
                layer.shutdown()

