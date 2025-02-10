import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from BubbleWidget import BubbleWidget
from NormalWidget import NormalWidget
from BubbleCursor import BubbleCursor
from RopeCursor import RopeCursor
from ExpSetup import ExpSetup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bubble Cursor")
        self.resize(1024, 800)
        self.move(300, 50)

        self.show_setup_dialog()

    def show_setup_dialog(self):
        setup_dialog = ExpSetup(self)
        if setup_dialog.exec_() == QDialog.Accepted:
            # Récupérer les valeurs saisies
            user_id = setup_dialog.user_input.value()
            technique = setup_dialog.technique_combo.currentText()
            densities = setup_dialog.density_input.value()
            sizes = setup_dialog.size_input.value()
            repetitions = setup_dialog.repetition_input.value()

            print(f"User {user_id}, Technique {technique}, "
                  f"Densities {densities}, Sizes {sizes}, Repetitions {repetitions}")

            # Charger le widget correspondant à la technique sélectionnée
            if technique == "Normal":
                widget = NormalWidget()
            elif technique == "Bubble":
                widget = BubbleWidget(BubbleCursor)
            elif technique == "Rope":
                widget = BubbleWidget(RopeCursor)
            else:
                return

            self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    app.setOverrideCursor(QCursor(Qt.ArrowCursor))

    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == "__main__":
    main()
