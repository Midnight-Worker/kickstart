import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 360
    height: 220
    visible: true
    title: "QML Python Brücke"

    Column {
        anchors.centerIn: parent
        spacing: 10

        TextField {
            id: input
            placeholderText: "Nachricht eingeben"
        }

        Button {
            text: "An Python senden"

            onClicked: {
                backend.sendToPython(input.text)
            }
        }

        Label {
            id: output
            text: "Noch keine Antwort"
        }
    }

    Connections {
        target: backend

        function onMessageChanged(message) {
            output.text = message
        }
    }
}
