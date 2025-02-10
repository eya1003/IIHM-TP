# ExpSetup.py
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QSpinBox, QPushButton, QGroupBox
)
from PyQt5.QtGui import QIntValidator  # Pour autoriser uniquement des chiffres dans le QLineEdit
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ExpSetup(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        self.move(300, 100)
        self.setWindowTitle("Setup de l'Expérience")

        # Création des sections du formulaire
        self.create_user_section()
        self.create_repetition_section()
        self.create_buttons_section()

        # Mise en page principale
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.user_group)
        main_layout.addWidget(self.repetition_group)
        main_layout.addLayout(self.buttons_layout)
        self.setLayout(main_layout)

    def create_user_section(self):
        self.user_group = QGroupBox("Informations utilisateur")
        user_layout = QHBoxLayout()
        self.user_label = QLabel("ID utilisateur:")
        self.user_input = QLineEdit()
        # Seuls les chiffres sont autorisés
        self.user_input.setValidator(QIntValidator(0, 999999))
        user_layout.addWidget(self.user_label)
        user_layout.addWidget(self.user_input)
        self.user_group.setLayout(user_layout)

    def create_repetition_section(self):
        self.repetition_group = QGroupBox("Paramètres de l'expérience")
        rep_layout = QHBoxLayout()
        self.repetitions_label = QLabel("Nombre de répétitions:")
        self.repetitions_input = QSpinBox()
        self.repetitions_input.setMinimum(2)   # valeur minimale = 2
        self.repetitions_input.setMaximum(10)
        self.repetitions_input.setValue(2)       # valeur par défaut à 2
        rep_layout.addWidget(self.repetitions_label)
        rep_layout.addWidget(self.repetitions_input)
        self.repetition_group.setLayout(rep_layout)

    def create_buttons_section(self):
        self.buttons_layout = QHBoxLayout()
        self.validate_button = QPushButton("Valider")
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.validate_button)
        self.validate_button.clicked.connect(self.validate_form)

    def validate_form(self):
        # On vérifie quand même la valeur (même si la QSpinBox empêche normalement <2)
        repetitions = self.repetitions_input.value()
        if repetitions < 2:
            print(f"Le nombre de répétitions ({repetitions}) doit être strictement supérieur à 1.")
            self.repetitions_input.setValue(2)
            return
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ExpSetup()
    if dialog.exec_() == QDialog.Accepted:
        print("ID utilisateur :", dialog.user_input.text())
        print("Répétitions :", dialog.repetitions_input.value())
    sys.exit(app.exec_())
