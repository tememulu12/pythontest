import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('FormLayout')

layout = QFormLayout()
layout.addRow('Imię', QLineEdit())
layout.addRow('Wiek', QLineEdit())
layout.addRow('Praca', QLineEdit())
layout.addRow('Hobby', QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec())
