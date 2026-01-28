import json
import shutil
from pathlib import Path
from datetime import datetime

class DoctrineController:
    def __init__(self, doctrine_root="gsg-data/doctrines"):
        self.root = Path(doctrine_root)
        self.root.mkdir(parents=True, exist_ok=True)

        for sub in ["pending", "approved", "rejected", "needs_testing", "deployed"]:
            (self.root / sub).mkdir(exist_ok=True)

    def approve(self, doctrine_name: str, approver: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "approved" / doctrine_name

        if not src.exists():
            raise FileNotFoundError(f"{doctrine_name} not found in pending")

        with open(src, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["status"] = "APPROVED"
        data["approved_at"] = datetime.utcnow().isoformat()
        data["approved_by"] = approver

        with open(src, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        shutil.move(str(src), str(dst))

    def reject(self, doctrine_name: str, reason: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "rejected" / doctrine_name

        if not src.exists():
            raise FileNotFoundError(f"{doctrine_name} not found in pending")

        with open(src, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["status"] = "REJECTED"
        data["notes"] = reason

        with open(src, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        shutil.move(str(src), str(dst))

    def needs_testing(self, doctrine_name: str, note: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "needs_testing" / doctrine_name

        if not src.exists():
            raise FileNotFoundError(f"{doctrine_name} not found in pending")

        with open(src, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["status"] = "NEEDS_MORE_TESTING"
        data["notes"] = note

        with open(src, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        shutil.move(str(src), str(dst))
