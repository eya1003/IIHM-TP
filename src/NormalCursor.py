from Target import Target
from typing import List
import math
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class NormalCursor:
    def __init__(self, targets: List[Target]):
        self.size: int = 10
        self.x: int = 0
        self.y: int = 0
        self.targets: List[Target] = targets
        self.toSelect = None  
    def move(self, a, b):
        self.x = a
        self.y = b
        self.cursorInTarget(a, b)
        

    def cursorInTarget(self, x, y):
        self.toSelect = None
        for target in self.targets:
            target.highlighted = False
            target.selected = False
        for target in self.targets:
            if ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5 <= target.size/2:
                target.highlighted = True
                if target.toSelect:
                    self.toSelect = target
                    target.selected = True
                    break
  