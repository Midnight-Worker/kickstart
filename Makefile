CC=gcc
CFLAGS=-Wall -Wextra -std=c11 $(shell pkg-config --cflags sdl2)
LDLIBS=$(shell pkg-config --libs sdl2)

main: main.c
	$(CC) $(CFLAGS) main.c -o main $(LDLIBS)

run: main
	./main

clean:
	rm -f main
