import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window

    width: 420
    height: 280
    visible: true
    title: "QML Kickstart"

    property int counter: 0

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 12

        Label {
            text: "Mein erstes QML-Programm"
            font.pixelSize: 24
            Layout.alignment: Qt.AlignHCenter
        }

        TextField {
            id: nameInput

            placeholderText: "Gib deinen Namen ein"
            Layout.fillWidth: true
        }

        Label {
            id: output

            text: "Noch wurde nichts eingegeben."
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            text: "Begrüßen"
            Layout.fillWidth: true

            onClicked: {
                if (nameInput.text === "") {
                    output.text = "Bitte zuerst einen Namen eingeben."
                } else {
                    output.text = "Hallo " + nameInput.text + "!"
                }
            }
        }

        Button {
            text: "Zähler: " + window.counter
            Layout.fillWidth: true

            onClicked: {
                window.counter++
            }
        }

        Button {
            text: "Beenden"
            Layout.fillWidth: true

            onClicked: {
                Qt.quit()
            }
        }

        Item {
            Layout.fillHeight: true
        }
    }
}
