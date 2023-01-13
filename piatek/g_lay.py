import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('GridLayout')

layout = QGridLayout()
layout.addWidget(QPushButton("Przycisk (0,0)"), 0, 0)
layout.addWidget(QPushButton("Przycisk (0,1)"), 0, 1)
layout.addWidget(QPushButton("Przycisk (0,2)"), 0, 2)
layout.addWidget(QPushButton("Przycisk (1,0)"), 1, 0)
layout.addWidget(QPushButton("Przycisk (1,1)"), 1, 1)
layout.addWidget(QPushButton("Przycisk (1,2)"), 1, 2)
layout.addWidget(QPushButton("Przycisk (2,0)"), 2, 0)
layout.addWidget(
    QPushButton("Przycisk (2,1) + 2 kolumny span"), 2, 1, 1, 2
)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
