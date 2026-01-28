class Firewall:
    """
    Generic Firewall for CastleGrid.
    Users can subclass this to create custom firewall logic.
    """

    def __init__(self, name="Default Firewall"):
        self.name = name

    def scan(self, grid_file) -> bool:
        """
        Return True if file passes, False if blocked.
        Default behavior: block anything with 'malware' in name.
        """
        if "malware" in grid_file.name.lower():
            return False
        return True

    def monitor(self, grid_file):
        print(f"[{self.name}] Monitoring file: {grid_file.name}")
