# kickstart-aliases.sh

#30 schwarz
#31 rot
#32 grün
#33 gelb
#34 blau
#35 magenta
#36 cyan
#37 weiß

#Beispiel:
#    \033[31m   rot
#    \033[32m   grün
#    \033[34m   blau

alias kmain='git switch main'
alias kst='git status --short --branch'
alias kbr='git branch --all'

alias vw='git switch v-web'
alias bw='git switch b-web'
alias tw='git switch t-web'

alias rea='git switch react'
alias ele='git switch electron'
alias exp='git switch express'
alias wv='git switch webview'

alias kiv='git switch kivy'
alias tk='git switch tkinter'
alias px='git switch pyxel'
alias pg='git switch pygame'

alias sdl='git switch sdl2'
alias c64='git switch c64'


green() {
		  printf "\033[32m%s\033[0m\n" "$*"
  }

blue() {
		  printf "\033[34m%s\033[0m\n" "$*"
  }

red() {
		  printf "\033[31m%s\033[0m\n" "$*"
  }

yellow() {
		  printf "\033[33m%s\033[0m\n" "$*"
  }
