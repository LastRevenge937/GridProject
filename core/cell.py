class Cell:
    def __init__(self, name: str):
        self.name = name
        self.status = "Online"

    def shutdown(self):
        self.status = "Offline"

    def start(self):
        self.status = "Online"
