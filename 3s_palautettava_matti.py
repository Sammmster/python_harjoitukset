#! /usr/bin/python3


from math import sqrt


"""
print("tama ohjelma laskee hypotenuusen, kahden annetun kateetin avulla")
kateetti1 = int(input("anna ensimmäinen kateetti"))
kateetti2 = int(input("anna toinen kateetti"))
hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
print ("hypotenuusen pituus on = " , hypotenuusa)


helppo: kysy ensin kayttajalta halutaanko laskea hypotenuusa vai katetti
sen jälkeen kysy joko kaksi katettia tai kateetti ja hypotenuusa.
normaali: sama kuin helppo, mutta kysytään myos haluaako kayttaja tietaa kolmion alan, jos haluaa
lasketaan myos se ja tulostetaan tulos
Vaikea: Koodi tarkastaa etta kayttaja on antanut oikean vastauksen, mikali ei kysyy uudelleen saman kysymyksen
"""

print("Haluatko laskea hypotenuusan (1) vai kateetin (2)?")
vastaus = input("")
if vastaus =="1":
    kateetti1 = int(input("anna ensimmäinen kateetti1"))
    kateetti2 = int(input("anna toinen kateetti"))
    hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
    print("hypotenuusen pituus on = " , hypotenuusa)
# tässä on sisennys virhe, print alkuinen lause kuuluu alkaa
# kaikki samalta tasolta jotta tuo toimii. Sinulla tuo oli rivin
# alussa.

else:
    kateetti1 = int(input("anna ensimmäinen kateetti1"))
    hypotenuusa = int(input("anna hypotenuusa"))
    kateeetti2 = sqrt(hypotenuusa**2 - kateetti1**2)
    # kateeetti2 = sqrt(hypotenuusa**2 - kateetti1*)
    # viimeinen kohta, kateetti1* kuuluu olla kateetti1**2
    print("kateetti2 pituus on = " , kateetti2)
# tässä sama sisennysvirhe

print("Haluatko tietää kolmion pinta-alan (k/e)?")
vastaus2 = input("")
if vastaus2 == "k":
# if vastaus2 == "k", sinulta puuttui : merkki rivin lopusta.
    ala = (kateetti1*kateetti2/2)
    print("Pinta-ala on ", ala)
else:
    print("Hei, hei ! ")