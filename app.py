import webview

class Api:
    def hallo(self):
        return "Hallo aus Python!"

api = Api()

webview.create_window(
    "Mini App",
    "index.html",
    js_api=api,
    width=800,
    height=600
)

webview.start()
