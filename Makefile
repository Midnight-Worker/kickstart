KICKASS=/c/C64/tools/KickAss.jar
JAVA=java

SRC=main.asm
PRG=main.prg

all: $(PRG)

$(PRG): $(SRC)
	$(JAVA) -jar $(KICKASS) $(SRC)

run: $(PRG)
	x64sc $(PRG)

clean:
	rm -f $(PRG) main.sym main.dbg
