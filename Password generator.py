import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QPushButton, \
    QMessageBox
from PyQt5.QtCore import Qt


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisation des variables
        self.maj = "ABCDEFGHJKMNPQRSTUVWXYZ"
        self.min = "abcdefghjkmnpqrstuvwxyz"
        self.chiffres = "0123456789"
        self.charac_spec = "#*-+:@_&%!?"
        self.liste = [self.maj, self.min, self.chiffres, self.charac_spec]
        self.selection = [self.maj, self.min, self.chiffres, self.charac_spec]

        self.initUI()

    def initUI(self):
        self.setWindowTitle("P@ssw0rd G€n€r@70r")
        self.setStyleSheet("background-color: #f0f0f5;")

        # Layouts
        main_layout = QVBoxLayout()
        check_layout = QHBoxLayout()
        entry_layout = QVBoxLayout()

        # Création des widgets
        self.chk_maj = QCheckBox("Majuscules")
        self.chk_min = QCheckBox("Minuscules")
        self.chk_num = QCheckBox("Chiffres")
        self.chk_spe = QCheckBox("Spéciaux")

        self.chk_maj.setChecked(True)
        self.chk_min.setChecked(True)
        self.chk_num.setChecked(True)
        self.chk_spe.setChecked(True)

        # Connecter les cases à cocher
        self.chk_maj.stateChanged.connect(self.update_selection)
        self.chk_min.stateChanged.connect(self.update_selection)
        self.chk_num.stateChanged.connect(self.update_selection)
        self.chk_spe.stateChanged.connect(self.update_selection)

        # Entrées
        self.label_nbcar = QLabel("Nombres de caractères souhaité")
        self.nbcar = QLineEdit()
        self.nbcar.setPlaceholderText("10 à 30 caractères")

        self.label_pwd = QLabel("Your P@ssw0rd, (clique sur Générer before)")
        self.password = QLineEdit()
        self.password.setReadOnly(True)

        # Boutons
        self.bouton_generate = QPushButton("Générer")
        self.bouton_generate.clicked.connect(self.generate)

        self.bouton_copy = QPushButton("Copy / paste dans le presse papier")
        self.bouton_copy.clicked.connect(self.add_to_clipboard)

        self.bouton_exit = QPushButton("Fermer l'outil du Turfu")
        self.bouton_exit.clicked.connect(self.close)

        # Placement des widgets dans le layout
        check_layout.addWidget(self.chk_maj)
        check_layout.addWidget(self.chk_min)
        check_layout.addWidget(self.chk_num)
        check_layout.addWidget(self.chk_spe)

        entry_layout.addWidget(self.label_nbcar)
        entry_layout.addWidget(self.nbcar)
        entry_layout.addWidget(self.bouton_generate)
        entry_layout.addWidget(self.label_pwd)
        entry_layout.addWidget(self.password)
        entry_layout.addWidget(self.bouton_copy)
        entry_layout.addWidget(self.bouton_exit)

        main_layout.addLayout(check_layout)
        main_layout.addLayout(entry_layout)

        self.setLayout(main_layout)

        self.resize(300, 200)
        self.center()

    def update_selection(self):
        # Met à jour la liste des caractères disponibles en fonction des cases cochées
        self.liste.clear()

        if self.chk_maj.isChecked():
            self.liste.append(self.maj)
        if self.chk_min.isChecked():
            self.liste.append(self.min)
        if self.chk_num.isChecked():
            self.liste.append(self.chiffres)
        if self.chk_spe.isChecked():
            self.liste.append(self.charac_spec)

    def generate(self):
        if not self.liste:
            QMessageBox.information(self, "Erreur", "Selectionne au moins une option patate! ;-)")
        else:
            try:
                nb = int(self.nbcar.text())
                if nb < 10 or nb > 30:
                    QMessageBox.information(self, "Erreur", "La taille de ton pé... Heu MDP doit faire entre 10 et 30 caractères")
                else:
                    compteur = 0
                    position = -1
                    D = []
                    while compteur < nb:
                        if position < len(self.liste) - 1:
                            position += 1
                        else:
                            position = 0
                        D = D + random.sample(self.liste[position], 1)
                        compteur += 1
                    random.shuffle(D)
                    D = "".join(D)
                    self.password.setText(D)
            except ValueError:
                QMessageBox.information(self, "Erreur",
                                        "Indique un nombre de caractères pour le MDP et non autre chose (smiley coeur).")

    def add_to_clipboard(self):
        text = self.password.text()
        if not text:
            QMessageBox.information(self, "Erreur", "Génère ton MDP avant BG #Michou #TMTC ")
        else:
            QApplication.clipboard().setText(text)

    def center(self):
        # Centre la fenêtre sur l'écran
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())
