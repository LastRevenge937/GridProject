class Layer:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.status = "OFFLINE"
        self.cells = []

    def boot(self):
        self.status = "ONLINE"

    def shutdown(self):
        self.status = "OFFLINE"

    def add_cell(self, cell):
        self.cells.append(cell)
