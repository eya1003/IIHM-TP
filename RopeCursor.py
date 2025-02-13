from BubbleCursor import BubbleCursor

class RopeCursor(BubbleCursor):
    def __init__(self, targets):
        super().__init__(targets)
        self.closest = None

    def paint(self, painter):
        if self.closest is not None:
            painter.setBrush(self.bubbleColor)
            painter.drawLine(self.x, self.y, self.closest.x, self.closest.y)
      