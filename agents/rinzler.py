class RinzlerAgent:
    """
    Defensive containment agent.
    Never attacks, never leaves grid.
    """
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def contain(self, grid_file):
        grid_file.log(f"Contained by Rinzler Agent {self.agent_id}")
        grid_file.freeze("Rinzler containment")
