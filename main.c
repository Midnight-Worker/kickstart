// pacman -S mingw-w64-x86_64-ncurses
// gcc main.c -o main -I/mingw64/include/ncursesw -lncursesw
// gcc main.c -o main $(pkg-config --cflags --libs ncursesw)

#include <ncurses.h>

int main(void) {
    initscr();              // curses starten

    printw("Hallo ncurses!");
    refresh();              // anzeigen

    getch();                // Taste warten
    endwin();               // Terminal zurücksetzen

    return 0;
}
