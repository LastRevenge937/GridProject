from core.protocols import ProtocolState
from core.identity import CastleIdentity

identity = CastleIdentity()
identity.load()

print(f"[Sentinel] Online — Castle: {identity.name}")

class Sentinel:
    def __init__(self, grid):
        self.grid = grid

    def report_breach(self, layer_index: int, reason: str):
        self.grid.log_global(f"Breach detected on Layer {layer_index}: {reason}")

        # LIMBO or uncontrolled breach → PURGE
        if layer_index == 0 or layer_index not in (6, 7):
            self.grid.activate_purge()

    def approve_manual_protocol(self, protocol: str):
        if protocol == ProtocolState.LAST_REVENGE:
            self.grid.activate_last_revenge()
