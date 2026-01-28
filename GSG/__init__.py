# gsg/gsg_core.py
from gsg.news_feed import NewsFeed

class GlobalShadowGrid:
    def __init__(self):
        self.news = NewsFeed()
        self.doctrines = {}
        self.captured_files = []

    def add_news(self, message: str):
        self.news.post(message)

