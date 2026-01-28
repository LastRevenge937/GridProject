import os
import json
import hashlib
from core.grid import GridManager
from core.layer import Layer
from core.cell import Cell
from ai.sentinel import Sentinel
from ai.shadowgrid import ShadowGrid
from gsg.gsg_core import GlobalShadowGrid
from cli.ascii_ui import AURA_UI
from core.identity import CastleIdentity

CONFIG_FILE = "castle_config.json"

# -----------------------------
# First boot: Castle name + admin password
# -----------------------------
def first_boot():
    print("🏰 Welcome to CastleGrid! First boot detected.\n")
    castle_name = input("Enter your Castle name (cannot change for 1 week): ").strip()
    while not castle_name:
        castle_name = input("Castle name cannot be empty. Try again: ").strip()

    admin_pw = input("Set your admin password (PURGE / LAST_REVENGE): ").strip()
    while not admin_pw:
        admin_pw = input("Password cannot be empty. Try again: ").strip()

    pw_hash = hashlib.sha256(admin_pw.encode()).hexdigest()

    config = {
        "castle": castle_name,
        "hash": pw_hash
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\nCastle '{castle_name}' saved! Sentinel and ShadowGrid will be online at boot.")
    input("Press Enter to continue...")
    return config

# -----------------------------
# Load existing config
# -----------------------------
def load_config():
    if not os.path.exists(CONFIG_FILE):
        return first_boot()
    with open(CONFIG_FILE) as f:
        return json.load(f)

# -----------------------------
# Build LIMBO / Layer 0
# -----------------------------
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

# -----------------------------
# Boot CastleGrid
# -----------------------------
def main():
    config = load_config()

    # Initialize main components
    grid = GridManager(config["castle"])
    sentinel = Sentinel(grid)
    gsg = GlobalShadowGrid()
    shadowgrid = ShadowGrid(grid, gsg)

    # Generate all 12 layers
    grid.generate_all_layers()
    # Replace Layer 0 with LIMBO
    grid.layers[0] = build_limbo()

    # Boot layers
    grid.boot_layers()

    # Confirm online
    print(f"\nCastleGrid '{config['castle']}' online!")
    print(f"Sentinel: Online | ShadowGrid: Online | GSG: Online ({len(gsg.captured_files)} files captured)\n")
    input("Press Enter to launch UI...")

    # Launch ASCII UI
    ui = AURA_UI(grid, sentinel, shadowgrid, config)
    ui.run()

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main()
