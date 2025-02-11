from NormalCursor import NormalCursor
from BubbleWidget import BubbleWidget
import time
import os

class NormalWidget(BubbleWidget):
    def __init__(self, targets_path=os.path.join(os.path.dirname(__file__), "../doc/src_tp_bubble.csv"), sequence_path=None):
        # On transmet NormalCursor à BubbleWidget pour que self.cursor soit une instance de NormalCursor.
        super().__init__(NormalCursor, targets_path, sequence_path)
        # Si une séquence est définie, on désigne la première cible de la séquence.
        if self.cibles_restantes:
            # On s'assure qu'aucune autre cible n'est marquée
            for t in self.targets:
                t.toSelect = False
            first_target = self.cibles_restantes.pop(0)
            first_target.toSelect = True
            self.update()

    def mousePressEvent(self, event):
        # Mise à jour de la position du curseur (ce qui déclenche le survol)
        self.cursor.move(event.x(), event.y())
        if self.cursor.toSelect is not None:
            target = self.cursor.toSelect
            # Le curseur survole bien la cible désignée → le clic est valide.
            # On efface la sélection pour cette cible...
            target.selected = False
            # ...et on la marque comme atteinte (couleur "highlighted")
            target.highlighted = True
            target.toSelect = False  # On efface le flag de désignation

            print("Cible atteinte en", int(round(time.time() * 1000)) - self.timer, "millisecondes")
            self.pressedTargets.append([
                len(self.pressedTargets),
                int(round(time.time() * 1000)) - self.timer,
                self.nb_erreurs_cible
            ])
            self.timer = int(round(time.time() * 1000))
            self.nb_erreurs_cible = 0

            # Désigner la prochaine cible de la séquence, s'il y en a une
            if self.cibles_restantes:
                for t in self.targets:
                    t.toSelect = False
                    t.selected = False
                next_target = self.cibles_restantes.pop(0)
                next_target.toSelect = True
            else:
                self.close()
                print("Partie terminée")
            self.update()
        else:
            self.nb_erreurs_cible += 1
