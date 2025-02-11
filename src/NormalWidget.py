from NormalCursor import NormalCursor
from BubbleWidget import BubbleWidget

from random import randint
import time
import os

class NormalWidget(BubbleWidget):
    def __init__(self, targets_path= os.path.join(os.path.dirname(__file__), "../doc/src_tp_bubble.csv"), sequence_path = None):
        super().__init__(NormalCursor, targets_path, sequence_path)

    def mousePressEvent(self, event):
        # Le clic est valide uniquement si le curseur survole une cible
        # ET si cette cible est celle qui est censée être atteinte (toSelect == True)
        if self.cursor.toSelect and self.cursor.toSelect.toSelect:
            self.cursor.toSelect.selected = False
            self.cursor.toSelect.highlighted = True
            self.cursor.toSelect.toSelect = False  # On "désactive" la cible atteinte

            print("Cible atteinte en", int(round(time.time() * 1000)) - self.timer, "millisecondes")
            self.pressedTargets.append([len(self.pressedTargets),
                                        int(round(time.time() * 1000)) - self.timer,
                                        self.nb_erreurs_cible])
            self.timer = int(round(time.time() * 1000))

            self.nb_erreurs_cible = 0

            if self.cibles_restantes != []:
                self.cibles_restantes.pop(0).toSelect = True
            else:
                self.close()
                print("Partie terminée")
        else:
            # Si le clic est sur une cible non désignée ou sur rien, on incrémente le compteur d'erreurs
            self.nb_erreurs_cible += 1
