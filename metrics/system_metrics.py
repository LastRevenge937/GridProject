import random

class SystemMetrics:
    """
    Simulated CPU / GPU / RAM metrics for ASCII UI
    """
    def snapshot(self):
        return {
            "CPU": f"{random.randint(10, 90)}%",
            "GPU": f"{random.randint(5, 70)}%",
            "RAM": f"{random.randint(20, 80)}%",
        }
