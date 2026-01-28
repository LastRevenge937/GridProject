class DeadManCore:
    """
    Absolute system lockdown.
    Manual activation only.
    """
    def __init__(self, grid):
        self.grid = grid
        self.armed = False

    def arm(self):
        self.armed = True
        self.grid.log_global("Dead-Man Core armed")

    def activate(self):
        if not self.armed:
            return

        self.grid.log_global("DEAD-MAN CORE ACTIVATED")
        for layer in self.grid.layers.values():
            layer.shutdown()
