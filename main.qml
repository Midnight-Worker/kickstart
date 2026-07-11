import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 320
    height: 180
    visible: true
    title: "PySide6 QML Starter"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Label {
            id: label
            text: "Hallo QML"
        }

        Button {
            text: "Klick mich"

            onClicked: {
                label.text = "Button wurde geklickt"
            }
        }
    }
}
