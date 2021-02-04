#! /usr/bin/python3

class Ensimmainen_luokka:
    x=2
# muuttujan x määrittely

luokka_objekti = Ensimmainen_luokka
print(luokka_objekti.x)
# class hyvä tapa erottaa funktioista on aloittaa sen nimi isolla kirjaimella

luokka_objekti.x = 4
print(luokka_objekti.x)
# luokan x arvoa voidaan muuttaa


class Toinen_luokka:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def tulosta_arvot(self):
        print (self.x)
        print (self.y)

luokka2_objekti = Toinen_luokka(4,5)
luokka2_objekti.tulosta_arvot()

while True:
    syote = input("kirjoita: ei ")
    if syote == "ei": 
# == tosi
        break
syote2 = ""
while syote2 != "on":
# != epätosi
    syote = input("kirjoita: on ")