import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PySide6 Kickstarter")
window.resize(320, 180)

label = QLabel("Hallo PySide6!")
button = QPushButton("Klick mich")


def button_clicked():
    label.setText("Button wurde geklickt!")


button.clicked.connect(button_clicked)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
