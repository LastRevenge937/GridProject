from sentinel.doctrine_controller import DoctrineController

class ShadowGrid:
    """
    ShadowGrid captures files from honeypots and proposes doctrines.
    """

    def __init__(self, grid, gsg):
        self.grid = grid
        self.gsg = gsg
        self.captured_files = []
        self.doctrines = DoctrineController()

    # ------------------------
    # Capture files from honeypot
    # ------------------------
    def capture_from_honeypot(self, grid_file):
        grid_file.freeze()  # makes read-only
        self.captured_files.append(grid_file)
        self.gsg.capture_file(grid_file)
        self.grid.log_global(f"ShadowGrid captured {grid_file.name}")

    # ------------------------
    # Propose doctrine
    # ------------------------
    def propose_doctrine(self, name: str, source_run: str, affected_layers: list, description: str):
        doctrine_id = self.doctrines.create_pending(
            name=name,
            source_castle=self.grid.identity.name,
            source_run=source_run,
            affected_layers=affected_layers,
            description=description
        )
        self.grid.log_global(f"ShadowGrid proposed doctrine {doctrine_id}")
        return doctrine_id

