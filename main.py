from kivy.app import App
from kivy.properties import StringProperty


class MainApp(App):
    text = StringProperty("READY.")

    def build(self):
        return None

    def kv_ruft_python(self):
        self.text = "KV hat Python gerufen!"

    def python_ruft_kv(self):
        self.root.ids.ausgabe.text = "Python hat KV geändert!"



MainApp().run()
