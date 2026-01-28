import os
from core.security import verify_password
from metrics.system_metrics import SystemMetrics
from core.identity import CastleIdentity

identity = CastleIdentity()
identity.load()

print(f"CASTLEGRID :: {identity.name}")

class AURA_UI:
    """
    Main ASCII UI for CastleGrid
    Supports:
        - Layer map
        - Protocol display
        - Numkey navigation to Cells / Metrics / GSG
        - PURGE / LAST_REVENGE commands
        - Quit
    """
    def __init__(self, grid, sentinel, shadowgrid, config):
        self.grid = grid
        self.sentinel = sentinel
        self.shadowgrid = shadowgrid
        self.config = config

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def draw(self):
        self.clear()
        print(f"🏰 CASTLEGRID — {self.grid.castle_name}")
        print(f"Protocol: {self.grid.protocol}\n")

        # ASCII UI Map
        print("┌──────────────────────── CASTLEGRID ────────────────────────┐")
        for i in range(12):
            layer = self.grid.layers[i]
            status = layer.status
            name = layer.name
            print(
                f"│ [{i:<2}] {name:<20} │ {'Description':<28} │ {status:<6} │"
            )
        print("└────────────────────────────────────────────────────────────┘\n")

        # Commands
        print("[1] Cells  [2] Metrics  [3] GSG")
        print("[P] PURGE  [L] LASTREVENGE  [Q] Quit\n")

    def run(self):
        while True:
            self.draw()
            cmd = input("> ").strip().upper()

            if cmd == "Q":
                break

            elif cmd in ("P", "L"):
                pw = input("Admin Password: ")
                if not verify_password(pw, self.config["hash"]):
                    input("Invalid password. Press Enter to continue...")
                    continue

                if cmd == "P":
                    self.grid.activate_purge()
                elif cmd == "L":
                    self.grid.activate_last_revenge()

            elif cmd == "1":
                self.show_cells()

            elif cmd == "2":
                self.show_metrics()

            elif cmd == "3":
                self.show_gsg()

            else:
                input("Unknown command. Press Enter to continue...")

    def show_cells(self):
        self.clear()
        print("=== Cells Status ===")
        for layer in self.grid.layers.values():
            print(f"Layer {layer.index}: {layer.name}")
            for cell in layer.cells:
                print(f"  - {cell.name}")
        input("\nPress Enter to return to main menu...")

    def show_metrics(self):
        self.clear()
        metrics = SystemMetrics().snapshot()
        print("=== System Metrics ===")
        for key, value in metrics.items():
            print(f"{key}: {value}")
        input("\nPress Enter to return to main menu...")

    def show_gsg(self):
        self.clear()
        print("=== Global Shadow Grid ===")
        print(f"Captured files: {len(self.shadowgrid.captured_files)}")
        print("Pending doctrines:", len(getattr(self.shadowgrid, "pending_doctrines", [])))
        input("\nPress Enter to return to main menu...")



def show_gsg(self):
    self.clear()
    print("=== GLOBAL SHADOW GRID ===\n")
    print("Recent News:\n")
    for ts, msg in self.shadowgrid.gsg.news.latest():
        print(f"[{ts}] {msg}")
    input("\nPress Enter to return...")


