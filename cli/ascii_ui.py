import os
from datetime import datetime

class AURA_UI:
    """
    ASCII UI for CastleGrid.
    Navigation keys:
      [0]–[11] : jump to layer
      1 : cell status
      2 : system metrics
      3 : PURGATORY runs
      4 : Doctrine workflow
      Q : quit
    """
    def __init__(self, grid, sentinel, shadowgrid, config):
        self.grid = grid
        self.sentinel = sentinel
        self.shadowgrid = shadowgrid
        self.config = config
        self.current_layer = 0

    # ------------------------
    # Run UI loop
    # ------------------------
    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_map()
            print("\nPress [0-11] to navigate layers, 1=Cells, 2=Metrics, 3=PURGATORY, 4=Doctrine, Q=Quit")
            choice = input("Choice: ").strip().upper()

            if choice == 'Q':
                print("Exiting CastleGrid UI...")
                break
            elif choice in [str(i) for i in range(12)]:
                self.current_layer = int(choice)
            elif choice == '1':
                self.show_cells()
            elif choice == '2':
                self.show_metrics()
            elif choice == '3':
                self.show_purgatory()
            elif choice == '4':
                self.show_doctrines()
            else:
                print("Invalid input! Press Enter to continue...")
                input()

    # ------------------------
    # Display ASCII Layer Map
    # ------------------------
    def display_map(self):
        layers = self.grid.layers
        print("┌──────────────────────── CASTLEGRID ────────────────────────┐")
        for i, layer in enumerate(layers):
            mark = ">" if i == self.current_layer else " "
            print(f"│{mark}[{i}] {layer.name:<20} │ {layer.description:<30}│")
        print("└────────────────────────────────────────────────────────────┘")

    # ------------------------
    # Show cell status
    # ------------------------
    def show_cells(self):
        layer = self.grid.layers[self.current_layer]
        print(f"\n[Layer {self.current_layer}] {layer.name} — Cells Status")
        for cell in layer.cells:
            status = getattr(cell, "status", "Idle")
            print(f"- {cell.name:<25} Status: {status}")
        input("\nPress Enter to return to map...")

    # ------------------------
    # Show simulated system metrics
    # ------------------------
    def show_metrics(self):
        # Example: aggregate CPU/GPU/RAM from Infrastructure layers
        print(f"\n[Layer {self.current_layer}] {self.grid.layers[self.current_layer].name} — Metrics")
        cpu = getattr(self.grid.layers[2], "cpu_load", 12)  # placeholder
        gpu = getattr(self.grid.layers[2], "gpu_load", 7)   # placeholder
        ram = getattr(self.grid.layers[2], "ram_usage", 34) # placeholder
        print(f"CPU Load: {cpu}%")
        print(f"GPU Load: {gpu}%")
        print(f"RAM Usage: {ram}%")
        input("\nPress Enter to return to map...")

    # ------------------------
    # Show PURGATORY runs
    # ------------------------
    def show_purgatory(self):
        print("\n[ PURGATORY RUNS ]")
        log_root = self.shadowgrid.purgatory_root
        files = sorted(log_root.glob("*.json"))
        for f in files[-10:]:  # show last 10 runs
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            ts = data.get("timestamp")
            file_name = data.get("file")
            status = data.get("status")
            castle = data.get("castle")
            print(f"{ts} | {castle} | {file_name} | {status}")
        input("\nPress Enter to return to map...")

    # ------------------------
    # Show Doctrine workflow
    # ------------------------
    def show_doctrines(self):
        print("\n[ DOCTRINE WORKFLOW ]")
        root = self.shadowgrid.doctrines.root
        for folder in ["pending", "needs_testing", "approved", "rejected", "deployed"]:
            print(f"\n-- {folder.upper()} --")
            for f in root.glob(f"{folder}/*.json"):
                with open(f, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
                name = data.get("name")
                status = data.get("status")
                created = data.get("created_at")
                print(f"{name:<30} | Status: {status} | Created: {created}")
        input("\nPress Enter to return to map...")



