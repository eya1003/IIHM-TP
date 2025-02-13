from NormalCursor import NormalCursor
from BubbleWidget import BubbleWidget

from random import randint
import time
import os

class NormalWidget(BubbleWidget):
    def __init__(self, targets_path= os.path.join(os.path.dirname(__file__), "../doc/src_tp_bubble.csv"), sequence_path = None):
        super().__init__(NormalCursor, targets_path, sequence_path)

    def mousePressEvent(self, event):
        if self.cursor.toSelect and self.cursor.toSelect.toSelect:
            self.cursor.toSelect.selected = False
            self.cursor.toSelect.highlighted = True
            self.cursor.toSelect.toSelect = False  

            print("Réussite ! Temps de réaction :", int(round(time.time() * 1000)) - self.timer, "millisecondes")
            self.pressedTargets.append([len(self.pressedTargets),
                                        int(round(time.time() * 1000)) - self.timer,
                                        self.nb_erreurs_cible])
            self.timer = int(round(time.time() * 1000))

            self.nb_erreurs_cible = 0

            if self.cibles_restantes != []:
                self.cibles_restantes.pop(0).toSelect = True
            else:
                self.close()
                print("Bravo ! Stage terminé")
        else:
            self.nb_erreurs_cible += 1
