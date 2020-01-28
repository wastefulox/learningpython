class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions, raisins=40):
        super().__init__(potatoes, celery, onions)
        if raisins:
            self.raisins = raisins
