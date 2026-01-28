import json
import shutil
from pathlib import Path
from datetime import datetime
import uuid

class DoctrineController:
    """
    Handles doctrine lifecycle.
    Works with Sentinel and ShadowGrid.
    """

    def __init__(self, doctrine_root="gsg-data/doctrines"):
        self.root = Path(doctrine_root)
        self.root.mkdir(parents=True, exist_ok=True)

        # ensure all folders exist
        for sub in ["pending", "approved", "rejected", "needs_testing", "deployed"]:
            (self.root / sub).mkdir(exist_ok=True)

    # ------------------------
    # Creation (ShadowGrid → PURGATORY)
    # ------------------------
    def create_pending(self, name: str, source_castle: str, source_run: str,
                       affected_layers: list, description: str):
        doctrine_id = str(uuid.uuid4())
        doctrine = {
            "doctrine_id": doctrine_id,
            "name": name,
            "origin": "PURGATORY",
            "source_castle": source_castle,
            "source_run": source_run,
            "affected_layers": affected_layers,
            "description": description,
            "status": "PENDING",
            "version": "1.0.0",
            "created_at": datetime.utcnow().isoformat(),
            "approved_at": None,
            "approved_by": None,
            "notes": ""
        }

        path = self.root / "pending" / f"{doctrine_id}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doctrine, f, indent=2)

        return doctrine_id

    # ------------------------
    # Sentinel authority
    # ------------------------
    def approve(self, doctrine_id: str, approver: str):
        self._transition(doctrine_id, "pending", "approved", status="APPROVED", approver=approver)

    def reject(self, doctrine_id: str, reason: str):
        self._transition(doctrine_id, "pending", "rejected", status="REJECTED", notes=reason)

    def needs_testing(self, doctrine_id: str, note: str):
        self._transition(doctrine_id, "pending", "needs_testing", status="NEEDS_MORE_TESTING", notes=note)

    def deploy(self, doctrine_id: str):
        self._transition(doctrine_id, "approved", "deployed", status="DEPLOYED")

    # ------------------------
    # Internal helper
    # ------------------------
    def _transition(self, doctrine_id, src_folder, dst_folder, status, approver=None, notes=None):
        src = self.root / src_folder / f"{doctrine_id}.json"
        dst = self.root / dst_folder / f"{doctrine_id}.json"

        if not src.exists():
            raise FileNotFoundError(f"Doctrine {doctrine_id} not found in {src_folder}")

        with open(src, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["status"] = status
        if approver:
            data["approved_by"] = approver
            data["approved_at"] = datetime.utcnow().isoformat()
        if notes:
            data["notes"] = notes

        with open(src, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        shutil.move(str(src), str(dst))
