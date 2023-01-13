import sys

from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget,
)


app = QApplication([])
window = QWidget()
window.setWindowTitle('VBoxLayout')

layout = QVBoxLayout()
layout.addWidget(QPushButton("Góra"))
layout.addWidget(QPushButton("Środkowy"))
layout.addWidget(QPushButton("Dół"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
