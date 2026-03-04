from pathlib import Path

class Folder:
    def __init__(self):
        pass

    def create(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)