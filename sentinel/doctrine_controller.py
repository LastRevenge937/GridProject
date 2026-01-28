import json
import shutil
from pathlib import Path
from datetime import datetime

class DoctrineController:
    def __init__(self, doctrine_root="gsg-data/doctrines"):
        self.root = Path(doctrine_root)

    def submit(self, doctrine_path: Path):
        target = self.root / "pending" / doctrine_path.name
        shutil.move(str(doctrine_path), target)

    def approve(self, doctrine_name: str, approver: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "approved" / doctrine_name

        with open(src, "r+") as f:
            data = json.load(f)
            data["status"] = "APPROVED"
            data["approved_at"] = datetime.utcnow().isoformat()
            data["approved_by"] = approver
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        shutil.move(src, dst)

    def reject(self, doctrine_name: str, reason: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "rejected" / doctrine_name

        with open(src, "r+") as f:
            data = json.load(f)
            data["status"] = "REJECTED"
            data["notes"] = reason
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        shutil.move(src, dst)

    def needs_testing(self, doctrine_name: str, note: str):
        src = self.root / "pending" / doctrine_name
        dst = self.root / "needs_testing" / doctrine_name

        with open(src, "r+") as f:
            data = json.load(f)
            data["status"] = "NEEDS_MORE_TESTING"
            data["notes"] = note
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        shutil.move(src, dst)
