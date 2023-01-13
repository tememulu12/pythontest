import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


app = QApplication([])
window = QWidget()
window.setWindowTitle('HBoxLayout')

layout = QHBoxLayout()
layout.addWidget(QPushButton("Lewy"))
layout.addWidget(QPushButton("Środkowy"))
layout.addWidget(QPushButton("Prawy"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
