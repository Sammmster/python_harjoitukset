#! /usr/bin/python3

from math import sqrt
# import ottaa käyttöön neliöjuuri funktion moduulista math.

print("Haluatko laskea hypotenuusan(1) vai kateetin(2)?")
vastaus = input("")
if vastaus == "1":
    kateetti1 = int(input("anna ensimmäinen kateetti "))
    kateetti2 = int(input("anna toinen kateetti "))
    hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
    print ("hypotenuusan pituus on = " , hypotenuusa)
## vastaus = "2"
else: 
    kateetti1 = int(input("anna ensimmäinen kateetti "))
    hypotenuusa = int(input("anna hypotenuusan pituus "))
    kateetti2 = sqrt(hypotenuusa**2 - kateetti1**2)
    print ("toisen kateetin pituus on = " , kateetti2)


print("Haluatko myös laskea kolmion pinta-alan (k/e)?")
vastaus2 = input("")
if vastaus2 == "k":
    ala = (kateetti1*kateetti2/2)
    print("Pinta-ala on ", ala)
else:
    print ("Mukavaa työpäivää")