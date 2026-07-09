## Neues Projekt aus einem Kickstart erstellen

```bash
git clone git@github.com:Midnight-Worker/kickstart.git mein-projekt
cd mein-projekt

git switch pygame

rm -rf .git
git init
git add .
git commit -m "init"


Kickstart Branches:

  bootstrap4
  canvas
  electron
  express
  kivy
* main
  mvc
  ncurses
  prg
  pycurses
  pygame
  pywsclient
  pywsserver
  pyxel
  react
  sdl2
  tailwind
  tcp
  tkinter
  ttkbootstrap
  web
  web-min
  webview
  ws
