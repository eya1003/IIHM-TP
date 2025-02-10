from PyQt5.QtGui import QPainter, QColor
from math import ceil, sqrt
from Target import Target

class BubbleCursor:
    bubbleColor = QColor("blue")

    def __init__(self, targets):
        self.size: int = 10
        self.x: int = 0
        self.y: int = 0
        self.targets: List[Target] = targets
        self.closest: Target = None

    def paint(self, painter):
        painter.setBrush(self.bubbleColor)
        painter.drawEllipse(int(self.x - self.size/2), int(self.y - self.size/2), self.size, self.size)

    def move(self, a, b):
        if self.closest != None:
            self.closest.selected = False
        self.closest, distance_closest = self.findTheClosest(a, b)
        self.closest.selected = True
        self.size = int(distance_closest)*2
        self.x = a
        self.y = b 

    def findTheClosest(self, a, b):
        closest = None
        distance_closest = 100000
        for target in self.targets:
            if target.selected:
                continue
            distance = abs(sqrt((target.x - a)**2 + (target.y - b)**2) - target.size/2)
            if distance < distance_closest:
                closest = target
                distance_closest = distance
        return closest, distance_closest