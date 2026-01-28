from pathlib import Path
import json
from datetime import datetime
from sentinel.doctrine_controller import DoctrineController

class ShadowGrid:
    """
    ShadowGrid captures files from honeypots, logs PURGATORY runs, and proposes doctrines.
    """
    def __init__(self, grid, gsg, purgatory_log_root="gsg-data/purgatory_runs"):
        self.grid = grid
        self.gsg = gsg
        self.captured_files = []
        self.doctrines = DoctrineController()
        self.purgatory_root = Path(purgatory_log_root)
        self.purgatory_root.mkdir(parents=True, exist_ok=True)

    # ------------------------
    # Capture files from honeypot
    # ------------------------
    def capture_from_honeypot(self, grid_file):
        # Freeze & copy
        grid_file.freeze("Captured by ShadowGrid")
        self.captured_files.append(grid_file)
        self.gsg.capture_file(grid_file)
        self.grid.log_global(f"ShadowGrid captured {grid_file.name}")

        # Log to PURGATORY runs
        self._log_purgatory_run(grid_file.name, "CAPTURED")

    # ------------------------
    # Log a PURGATORY run
    # ------------------------
    def _log_purgatory_run(self, file_name: str, status: str):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "timestamp": timestamp,
            "file": file_name,
            "status": status,
            "castle": self.grid.identity.name
        }
        log_file = self.purgatory_root / f"{timestamp.replace(':','-')}_{file_name}.json"
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2)

    # ------------------------
    # Propose doctrine for Sentinel
    # ------------------------
    def propose_doctrine(self, name: str, source_run: str, affected_layers: list, description: str):
        doctrine_id = self.doctrines.create_pending(
            name=name,
            source_castle=self.grid.identity.name,
            source_run=source_run,
            affected_layers=affected_layers,
            description=description
        )
        self.grid.log_global(f"ShadowGrid proposed doctrine {doctrine_id}")
        # Also log in PURGATORY
        self._log_purgatory_run(f"Doctrine {name}", "PENDING")
        return doctrine_id

    # ------------------------
    # Submit doctrine directly to GSG (optional)
    # ------------------------
    def submit_doctrine(self, castle_name: str, doctrine_name: str, content: str):
        self.gsg.submit_doctrine(castle_name, doctrine_name, content)
        self._log_purgatory_run(f"Doctrine {doctrine_name}", "SUBMITTED")
