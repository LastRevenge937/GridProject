import os
from core.security import verify_password
from core.protocols import ProtocolState

class AURA_UI:
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
        print(f"Protocol: {self.grid.protocol}")
        print("=" * 50)

        for i in range(12):
            layer = self.grid.layers[i]
            print(f"[{i}] {layer.name:<18} | {layer.status}")

        print("\n[1] Cells  [2] Metrics  [3] GSG")
        print("[P] PURGE  [L] LASTREVENGE  [Q] Quit")

    def run(self):
        while True:
            self.draw()
            cmd = input("> ").strip().upper()

            if cmd == "Q":
                break

            if cmd in ("P", "L"):
                pw = input("Admin Password: ")
                if not verify_password(pw, self.config["hash"]):
                    input("Invalid password. Press Enter.")
                    continue

                if cmd == "P":
                    self.grid.activate_purge()
                else:
                    self.grid.activate_last_revenge()
