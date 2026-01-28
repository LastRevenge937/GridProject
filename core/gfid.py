import uuid
import hashlib
import time

class GFID:
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.created_at = time.time()
        self.ledger = []

    def log(self, entry: str):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        record = f"{timestamp} | {entry}"
        self.ledger.append(record)

    def fingerprint(self) -> str:
        h = hashlib.sha256()
        for entry in self.ledger:
            h.update(entry.encode())
        return h.hexdigest()
