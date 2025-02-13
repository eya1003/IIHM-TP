from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from random import randint, shuffle
import time
import os
from typing import List
from PyQt5.QtCore import pyqtSignal

from BubbleCursor import BubbleCursor
from Target import Target

class BubbleWidget(QWidget):
    finished = pyqtSignal()

    def __init__(self, cursor, targets_path = os.path.join(os.path.dirname(__file__), "../doc/src_tp_bubble.csv"), sequence_path = None):
        super().__init__()
        self.setMouseTracking(True)
        self.targets: List[Target] = []
        self.loadTargets(targets_path)
        
        self.cursor: BubbleCursor = cursor(self.targets)
        # Initalisation du timer
        self.timer = int(round(time.time() * 1000))

        self.pressedTargets = []
        self.cibles_restantes: List[Target] = []
        self.loadSequence(sequence_path)
        self.nb_erreurs_cible = 0

    def loadTargets(self, name_file):
        with open(name_file, "r") as file:
            for line in file:
                x, y, size = line.split(",")
                self.targets.append(Target(int(x), int(y), int(size)))
        self.targets[randint(0, len(self.targets) - 1)].toSelect = True

    def loadSequence(self, sequence_path):
        with open(sequence_path, "r") as file:
            lines = file.readlines()
            
            # Vérifie si la première ligne contient du texte au lieu d'un nombre
            if not lines[0][0].isdigit():
                lines = lines[1:]  # Ignore la première ligne (en-tête)

            for line in lines:
                x = line.strip()
                if x.isdigit():  # Vérifie que x est bien un nombre
                    self.cibles_restantes.append(self.targets[int(x)])


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.cursor.paint(painter)
        for target in self.targets:
            target.paint(painter)

    def mouseMoveEvent(self, event):
        self.cursor.move(event.x(), event.y())
        self.update()

    def mousePressEvent(self, event):
        if self.cursor.closest.toSelect:
            self.cursor.closest.selected = False
            self.cursor.closest.highlighted = True
            self.cursor.closest.toSelect = False
            print("Réussite ! Temps de réaction :", int(round(time.time() * 1000)) - self.timer, "millisecondes")
            self.pressedTargets.append([len(self.pressedTargets), int(round(time.time() * 1000))- self.timer, self.nb_erreurs_cible])
            self.timer = int(round(time.time() * 1000))

            self.nb_erreurs_cible = 0
            if self.cibles_restantes != []:
                self.cibles_restantes.pop(0).toSelect = True

            else:
                self.close()
                print("Bravo ! Stage terminé")
        else :
            self.nb_erreurs_cible += 1
    def closeEvent(self, event):
        self.finished.emit()
        super().closeEvent(event)