class Sentinel:
    def __init__(self, grid):
        self.grid = grid

    def report_breach(self, layer_index: int, reason: str):
        print(f"[Sentinel] Breach detected on Layer {layer_index}: {reason}")
        self.grid.activate_purge()

    def approve_manual_protocol(self, protocol: str):
        if protocol == "LAST_REVENGE":
            self.grid.activate_last_revenge()

    # Optional: Sentinel can also monitor global and layer firewalls
    def monitor_firewalls(self):
        if self.grid.global_firewall:
            print(f"[Sentinel] Global firewall '{self.grid.global_firewall.name}' online")
        for layer in self.grid.layers:
            if layer.firewall:
                print(f"[Sentinel] Layer {layer.index} firewall '{layer.firewall.name}' online")
