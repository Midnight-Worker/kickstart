import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(
    title="Mein erstes ttkbootstrap Fenster",
    themename="darkly",
    size=(600, 400)
)

label = ttk.Label(
    app,
    text="Hallo ttkbootstrap!",
    font=("Segoe UI", 18)
)
label.pack(pady=30)

button = ttk.Button(
    app,
    text="Klick mich",
    bootstyle=PRIMARY
)
button.pack()

app.mainloop()
