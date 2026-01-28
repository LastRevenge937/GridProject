class Sentinel:
    def __init__(self, grid):
        self.grid = grid

    def breach_detected(self, layer_index: int):
        if layer_index == 0 or layer_index in self.grid.layers:
            self.grid.activate_purge()
