class Manufacturer:
    def __init__(self, name, description, category, active=True, id=None):
        self.name  = name
        self.description = description
        self.category = category
        self.active = active
        self.id = id

    def make_inactive(self):
        self.active = False