class Manufacturer:
    def __init__(self, name, description, category, active=True):
        self.name  = name
        self.description = description
        self.category = category
        self.active = active

    def make_inactive(self):
        self.active = False