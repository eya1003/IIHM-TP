from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Target:
    defaultCol = QColor(255, 0, 0)  # Rouge 
    highlightCol = QColor(0, 0, 0)  # Noir 
    toSelectCol = QColor(0, 255, 0)  # Vert
    selectedCol = QColor(0, 0, 255)  # Bleu 

    def __init__(self, x, y, size):
        self.x: int = x
        self.y: int = y
        self.size: int = size
        self.selected: bool = False
        self.highlighted: bool = False
        self.toSelect: bool = False

    def paint(self, painter):
        if self.selected:
            painter.setBrush(self.selectedCol)  
        elif self.toSelect:
            painter.setBrush(self.toSelectCol) 
        elif self.highlighted:
            painter.setBrush(self.defaultCol)  
        else:
            painter.setBrush(self.defaultCol)  
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(int(self.x - self.size / 2), int(self.y - self.size / 2), self.size, self.size)
