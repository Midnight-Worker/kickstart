import sys
from pathlib import Path

from PySide6.QtCore import QObject, QUrl, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Backend(QObject):
    messageChanged = Signal(str)

    @Slot(str)
    def sendToPython(self, text):
        print("Aus QML:", text)

        self.messageChanged.emit(
            f"Python hat empfangen: {text}"
        )


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
backend = Backend()

engine.rootContext().setContextProperty(
    "backend",
    backend
)

qml_file = Path(__file__).parent / "bridgemain.qml"
engine.load(QUrl.fromLocalFile(qml_file))

if not engine.rootObjects():
    sys.exit(1)

sys.exit(app.exec())
