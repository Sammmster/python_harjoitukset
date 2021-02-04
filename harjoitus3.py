#! /usr/bin/python3

# ollaan käytetty jo funktioita:
# int() eli integer eli numero
# str() eli string eli kirjaimet
# input()
# print()


# def eli define
def eka_funktio():
    print("eka funktio tulostaa!")

eka_funktio()
eka_funktio()
eka_funktio()
# tulostaa määritellyn eka_funktion useamman kertaan.
# funktiokutsu

# funktio argumentillä
def toka_funktio(teksti):
    print("toka funktio tulostaa taman + argumentin: " +teksti)
toka_funktio("ihan mitä vaan")
toka_funktio("tai myös tälläistä")

# funktio palautuksella "return"
def kolmas_funktio():
    luku = 25
    return luku
funktion_palautus = kolmas_funktio()
print(funktion_palautus)