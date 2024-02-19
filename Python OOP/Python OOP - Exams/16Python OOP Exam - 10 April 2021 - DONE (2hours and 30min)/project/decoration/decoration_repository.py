class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        else:
            return False

    def find_by_type(self, decoration_type: str):
        decoration = [d for d in self.decorations if type(d).__name__ == decoration_type]
        if decoration:
            return decoration[0]
        else:
            return "None"
