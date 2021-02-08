#! /usr/bin/python3

######### Merkkijono #############################

print("Ohjelma alkaa...")
print("eka", "toka", "kolmas")
print("esi" + "merkki")
print("t" + "e" + "s" + "t" + "i")
print("Ohjelma päättyy...")

# Ohjelma alkaa...
# eka toka kolmas
# esimerkki
# testi
# Ohjelma päättyy...

# kenoviivalla (\) on erityismerkitys merkkijonossa: Jos merkkijonin sisällä on merkki, joka myös
# ympäröi merkkijonoa, sen eteen täytyy kirjoittaa kenoviiva. Lisäksi merkintä \n tarkoittaa rivinvaihtoa
# ja merkintä \\ tarkoittaa kenoviivaa.
# Tarkoittaa että siis jos haluat tulostukseen tulevan myös "moi" hipsukoineen niin täytyy käyttää \ viivaa

print ("\"abc\" on merkkijono")
print ("eka \ntoka \nkolmas")
print ("c:\\python\\testi.py")
# "abc" on merkkijono
# eka
# toka
# kolmas
# c:\python\testi.py

############ Lukuarvo ##########################

## kokonaisluku 1, 43, 6543
## liukuluku 4.4234
##
## merkintä  selitys                 esimerkki   tulos
## a+b       yhteenlasku             3+4         7
## a-b       vähennyslasku           7-20        -13
## a*b       kertolasku              11*8        88
## a/b       jakolasku               17/4        4.25
## a//b      jakolaskun kokonaisosa  17//4       4
## a%b       jakojäännös             17%4        1
## a**b      potenssilasku           2**5        32

#print (1+2+3+4+5)
#print (0.01 + 12.783 * (89 - 13))
#print ("Vuodessa on:")
#print (365, "päivää")
#print (365*24, "tuntia")
#print (365*24*60, "minuuttia")
#print (365*24*60*60, "sekunttia")
#print ("Jos 6 lasta saavat 45 karkkia")
#print ("kukin lapsi saa", 45//6, "karkkia")
#print ("ja", 45%6, "karkkia jää yli.")

## 15
## 971.517999999999
## Vuodessa on:
## 365 päivää
## 8760 tuntia
## 525600 minuuttia
## 31536000 sekunttia
## Jos 6 lasta saavat 45 karkkia
## kukin lapsi saa 7 karkkia
## ja 3 karkkia jää yli.


################# muuttujia #############3
#nimi = "Sami"
#vuosi = 1672
#ika = 25
#print (nimi, "on urhea ritari,")
#print ("syntynyt vuonna", vuosi, "kaukana täältä.")
#print (nimi, "on tämän pelin sankari.")
#print ("Nyt", nimi, "on", ika, "vuotta vanha,")
#print ("eletään vuotta", vuosi + ika, "siis")

# Sami on urhea ritari,
# syntynyt vuonna 1672 kaukana täältä.
# Sami on tämän pelin sankari.
# Nyt Sami on 25 vuotta vanha,
# eletään vuotta 1697 siis.

################# muuttuja käyttäjältä ###############

#nimi = input("Nimi: ")
#viesti = input("Viesti: ")
#print(nimi, "sanoo:")
#print(viesti)
#print(viesti)
#print(viesti)

## Nimi: Sami
## Viesti: Haistakaa kakka!
## Sami sanoo:
## Haistakaa kakka!
## Haistakaa kakka!
## Haistakaa kakka!


#nimi = input("Nimi: ")
#print(nimi)
#nimi = nimi + nimi
#print(nimi)
#nimi = nimi + nimi
#print(nimi)

# Nimi: Sami
# Sami
# SamiSami
# SamiSamiSamiSami


############### funktio #################

print("Merkkien määrä:", len("python"))
# Merkkien määrä: 6

print ("Anna nimesi: ")
sana = input()
print("Merkkien määrä:", len(sana))
# kirjoita oma nimesi niin antaa 4
# oma variaatio

# Tässä tapauksessa funktio len ottaa vastaan merkkijonon ja palauttaa merkkien määrän
# Joskus funktion palautusarvoon vaikuttaa muutkin asiat kun sille annetut tiedot. Esimerkiksi
# funktio input palauttaa käyttäjän kirjoittaman tekstin merkkijonona.
# Tässä on muutamia hyödyllisiä Python-kielen funktioita:
# len       laskee merkkijonon merkkien määrän
# int       muuttaa arvon kokonaisluvuksi
# float     muuttaa arvon liukuluvuksi
# str       muuttaa arvon merkkijonoksi
# round     pyöristää luvun halutulle tarkkuudelle
# abs       laskee luvun itseisarvon
# Funktiot int, float ja str ovat tarpeellisia, koska luvuille ja merkkijonoille voi tehdä erilaisia asioita.
# Esimerkiksi + merkintä laskee lukuja yhteen tai liittää merkkijonoja toisiinsa. Funktiolle len voi antaa myös
# merkkijonon, kun taas funktiolle abs voi antaa vain luvun.

###### esimerkki kertolasku ############

eka = int(input("Anna 1. luku: "))
toka = int(input("Anna 2. luku: "))
tulo = eka * toka
print("Lukujen tulo:", tulo)
print("Numeroita:", len(str(tulo)))

# Anna 1. luku: 1832
# Anna 2. luku: 5755
# Lukujen tulo: 10543160
# Numeroita: 8
# Funktion input palauttamat merkkijonot täytyy muuttaa kokonaisluvuiksi, jotta kertolasku voidaan
# suorittaa. Lopuksi laskun tulos täytyy muuttaa merkkijonoksi, jotta numeroiden määrän
# laskeminen onnistuu.

############## esimerkki alennushinta ##############
hinta = float(input("Alkuperäishinta "))
alennus = float(input("Alennusprosentti: "))
hinta = hinta - hinta * (alennus/100)
print("Alennushinta: ", round(hinta, 2))
# Alkuperäishinta: 78
# Alennusprosentti: 12
# Alennushinta: 68.64
