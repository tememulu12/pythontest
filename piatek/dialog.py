import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QWidget,
    QVBoxLayout,
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle('QDialog')
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Imię', QLineEdit())
        formLayout.addRow('Wiek', QLineEdit())
        formLayout.addRow('Praca', QLineEdit())
        formLayout.addRow('Hobby', QLineEdit())
        dialogLayout.addLayout(formLayout)
        button = QDialogButtonBox()
        button.setStandardButtons(QDialogButtonBox.StandardButton.Cancel |
                                  QDialogButtonBox.StandardButton.Ok)
        dialogLayout.addWidget(button)
        self.setLayout(dialogLayout)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())