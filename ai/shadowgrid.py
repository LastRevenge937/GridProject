class ShadowGrid:
    """
    ShadowGrid copies captured files and sends doctrines to GSG.
    """
    def __init__(self, grid, gsg: 'GlobalShadowGrid'):
        self.grid = grid
        self.gsg = gsg
        self.captured_files = []

    def capture_from_honeypot(self, grid_file):
        grid_file.freeze("Captured by ShadowGrid")
        self.captured_files.append(grid_file)
        self.gsg.capture_file(grid_file)
        self.grid.log_global(f"ShadowGrid captured {grid_file.name}")

    def submit_doctrine(self, castle_name: str, doctrine_name: str, content: str):
        self.gsg.submit_doctrine(castle_name, doctrine_name, content)
