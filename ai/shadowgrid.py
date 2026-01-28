class ShadowGrid:
    def __init__(self, grid):
        self.grid = grid
        self.captured = []

    def capture(self, grid_file):
        grid_file.freeze("Captured by ShadowGrid")
        self.captured.append(grid_file)
