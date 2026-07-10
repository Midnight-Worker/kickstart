#include <QApplication>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>

int main(int argc, char *argv[])
{
    // Die zentrale Qt-Anwendung.
    QApplication app(argc, argv);

    // Unser Hauptfenster.
    QWidget window;
    window.setWindowTitle("Qt6 Kickstart");
    window.resize(400, 250);

    // Widgets erzeugen.
    QLabel title("Mein erstes Qt6-Programm");

    QLineEdit input;
    input.setPlaceholderText("Gib deinen Namen ein");

    QLabel output("Noch wurde nichts eingegeben.");

    QPushButton helloButton("Begrüßen");
    QPushButton closeButton("Beenden");

    // Widgets untereinander anordnen.
    QVBoxLayout layout;

    layout.addWidget(&title);
    layout.addWidget(&input);
    layout.addWidget(&output);
    layout.addWidget(&helloButton);
    layout.addWidget(&closeButton);

    // Das Layout gehört zum Fenster.
    window.setLayout(&layout);

    // Klick auf den Begrüßen-Button.
    QObject::connect(
        &helloButton,
        &QPushButton::clicked,

        [&input, &output]() {
            QString name = input.text();

            if (name.isEmpty()) {
                output.setText("Bitte zuerst einen Namen eingeben.");
            } else {
                output.setText("Hallo " + name + "!");
            }
        }
    );

    // Klick auf den Beenden-Button.
    QObject::connect(
        &closeButton,
        &QPushButton::clicked,
        &window,
        &QWidget::close
    );

    // Fenster sichtbar machen.
    window.show();

    // Qt-Eventloop starten.
    return app.exec();
}
