import random
import os
import sys
from PyQt5.QtWidgets import QApplication

from BubbleCursor import BubbleCursor
from RopeCursor import RopeCursor
from BubbleWidget import BubbleWidget
from NormalWidget import NormalWidget

class XPManager:
    def __init__(self, fen, name_user, technique, densities, sizes, repetitions):
        self.fen = fen
        if name_user == "":
            self.name_user = "Anonyme"
        else :
            self.name_user = name_user

        if technique == "All":
            self.technique = ["Bubble Cursor", "Rope Cursor", "Normal Cursor"]
        else:
            self.technique = [technique]

        if densities == "All":
            self.densities = [30, 60, 90]
        else:
            self.densities = [int(densities)]

        if sizes == "All":
            self.sizes = [6, 12, 18]
        else:
            self.sizes = [int(sizes)]

        self.repetitions = int(repetitions)

        self.permutations_possibles = [
            (i, j, k, l) for i in self.technique for j in self.densities for k in self.sizes for l in range(self.repetitions)
        ]
        self.permutations_realisees = []

        self.current_widget = None

        self.run_next_experiment()

    def get_random_permutation(self):
        if len(self.permutations_possibles) == 0:
            return None
        else:
            permutation = random.choice(self.permutations_possibles)
            self.permutations_realisees.append(permutation)
            self.permutations_possibles.remove(permutation)
            return permutation

    def run_next_experiment(self):
        if len(self.permutations_possibles) == 0:
            print("Toutes les expériences ont été réalisées.")
            return

        permutation = self.get_random_permutation()
        if permutation is None:
            return

        os.system(f"python generer_aleatoirement.py {permutation[1]} {permutation[2]}")
        name_folder = f"generated_csv/partie_{permutation[1]}_{permutation[2]}"

        if permutation[0] == "Bubble Cursor":
            self.current_widget = BubbleWidget(BubbleCursor, f"{name_folder}/targets.csv", f"{name_folder}/sequence.csv")
        elif permutation[0] == "Rope Cursor":
            self.current_widget = BubbleWidget(RopeCursor, f"{name_folder}/targets.csv", f"{name_folder}/sequence.csv")
        else:
            self.current_widget = NormalWidget(f"{name_folder}/targets.csv", f"{name_folder}/sequence.csv")

        self.current_widget.setGeometry(300, 50, 1024, 800)
        self.current_widget.finished.connect(lambda: self.end_experiment(self.current_widget, permutation))

        self.current_widget.show()

    def end_experiment(self, widget, permutation):
        self.save_results(widget, permutation)
        self.run_next_experiment()

    def save_results(self, widget, permutation):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        with open(f"logs/user_results.csv", "a") as file:
            for target, time, nb_errors in widget.pressedTargets:
                file.write(f"{self.name_user},{permutation[0]},{permutation[1]},{permutation[2]},{permutation[3]},{target},{time},{nb_errors}\n")
            



                
            

                
                
        