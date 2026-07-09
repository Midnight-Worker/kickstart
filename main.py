import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def say_hello():
    name = name_entry.get()

    if name.strip():
        output_label.config(text=f"Hallo, {name}!")
    else:
        output_label.config(text="Bitte gib einen Namen ein.")


app = ttk.Window(
    title="ttkbootstrap Kickstart",
    themename="superhero",
    size=(500, 300)
)

title = ttk.Label(
    app,
    text="TerminalMentor Setup",
    font=("Segoe UI", 20, "bold")
)
title.pack(pady=20)

name_entry = ttk.Entry(
    app,
    width=30
)
name_entry.pack(pady=10)

button = ttk.Button(
    app,
    text="Begrüßen",
    bootstyle=SUCCESS,
    command=say_hello
)
button.pack(pady=10)

output_label = ttk.Label(
    app,
    text="",
    font=("Segoe UI", 12)
)
output_label.pack(pady=10)

app.mainloop()
