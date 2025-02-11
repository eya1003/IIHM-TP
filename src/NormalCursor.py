from Target import Target

class NormalCursor:
    def __init__(self, targets):
        self.size: int = 10
        self.x: int = 0
        self.y: int = 0
        self.targets: List[Target] = targets
        self.toSelect = None

    def paint(self, painter):
        pass

    def move(self, a, b):
        self.x = a
        self.y = b
        self.cursorInTarget(self.x, self.y)

    def cursorInTarget(self, x, y):
        self.toSelect = None
        for target in self.targets:
            target.selected = False
        for target in self.targets:
            if ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5 <= target.size/2:
                self.toSelect = target
                target.selected = True
                break