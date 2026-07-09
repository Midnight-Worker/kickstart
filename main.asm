// java -jar KickAssembler/KickAss.jar main.asm

BasicUpstart2(start)

* = $0810

start:
    lda #147        // Bildschirm löschen
    jsr $ffd2       // CHROUT

    ldx #0

loop:
    lda text,x
    beq done        // Ende bei 0-Byte
    jsr $ffd2       // Zeichen ausgeben
    inx
    jmp loop

done:
    rts             // zurück zum BASIC

text:
    .text "HALLO WELT!"
