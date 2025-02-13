from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ExpSetup import ExpSetup
from XPManager import XPManager

LARGEUR = 1024
HAUTEUR = 800

class MainUser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jeu")
        self.resize(LARGEUR, HAUTEUR)
        self.move(300, 50)

        self.exp_setup = ExpSetup()
        self.exp_setup.validate_button.clicked.connect(self.start_experiment)
        self.exp_setup.exec_()

    def start_experiment(self):
        user = self.exp_setup.user_input.text()
        repetitions = self.exp_setup.repetitions_input.value()
        
        self.exp_setup.close()
        self.xpmanager = XPManager(self, user, "All", "All", "All", repetitions)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUser()
    app.exec_()
