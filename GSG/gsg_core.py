import os
import json
from core.file import GridFile
from core.identity import CastleIdentity
from gsg.news_feed import NewsFeed

class GlobalShadowGrid:
    def __init__(self):
        self.identity = CastleIdentity()
        self.identity.load()

        self.news = NewsFeed()

    def add_news(self, message: str):
        self.news.post(f"[{self.identity.name}] {message}")

class GlobalShadowGrid:
    """
    Local Python implementation of the GSG.
    Holds doctrines, stores captured files from ShadowGrid,
    and manages news feed for connected castles.
    """
    DATA_DIR = "gsg/data"
    DOCTRINE_FILE = "doctrines.json"
    NEWS_FILE = "news_feed.json"

    def __init__(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        self.doctrines = self.load_json(self.DOCTRINE_FILE)
        self.news_feed = self.load_json(self.NEWS_FILE)
        self.captured_files = []

    def load_json(self, filename):
        path = os.path.join(self.DATA_DIR, filename)
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return {}

    def save_json(self, data, filename):
        path = os.path.join(self.DATA_DIR, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def submit_doctrine(self, castle_name: str, doctrine_name: str, content: str):
        self.doctrines.setdefault(castle_name, {})
        self.doctrines[castle_name][doctrine_name] = content
        self.save_json(self.doctrines, self.DOCTRINE_FILE)
        self.add_news(f"{castle_name} submitted doctrine '{doctrine_name}'")

    def add_news(self, message: str):
        from time import time
        self.news_feed[time()] = message
        self.save_json(self.news_feed, self.NEWS_FILE)

    def capture_file(self, grid_file: GridFile):
        # Store read-only copy for testing
        grid_file.freeze("Captured by GSG")
        self.captured_files.append(grid_file)
        self.add_news(f"GSG captured file {grid_file.name}")
