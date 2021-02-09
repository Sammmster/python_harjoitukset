#! /usr/bin/python3

############ python ohjelmointi: osa4 - Toistorakenteet #######

## Ehtorakenteiden avulla ohjelma voi suorittaa valikoivasti koodiriviä, mutta
## ohjelman suoritus etenee silti koko ajan riviltä alaspäin.
## Toistorakenteet antavat ohjelmalle mahdollisuuden suorittaa samoja rivejä
## monta kertaa peräkkäin. Nyt jos ohjelman täytyy tehdä monta samaa asiaa,
## tarvitaan koodi kirjoittaa vain kerran.

## Python -kielen toistorakenteet ovat while -silmukka, jossa ohjelma toistaa samaa
## koodia niin kauan kun jokin ehto on voimassa, sekä for -silmukka, jossa ohjelma käy läpi
## joukon tietoja ja suorittaa jokaisessa kodassa saman koodin. Tämä opas esittelee molemmat
## toistorakenteet, vaikka for -silmukka pääse täysiin oikeuksiinsa vasta seuraavissa oppaissa
## lisjoten ja merkkijonojen käsittelyssä.

####### while -silmukka ############

## Seuraava ohjelma kysyy käyttäjältä tunnussanaa, kunnes käyttäjä antaa oikean tunnussanan
## "python".

sana = ""
while sana != "python":
    sana = input("Kirjoita tunnussana: ")
print("Tervetuloa")

## Ohjelman tulostis voi olla seuraava:
## Kirjoita tunnussana: kissa
## Kirjoita tunnussana: putka
## Kirjoita tunnussana: python
## Tervetuloa!

## Ohjelmassa on while -silmukka jonka alussa on totuusmuotoinen ehto. Tässä ehto sana != "python"
## tarkoittaa, että ohjelma toistaa silmukkaa niin kauan, kuin tunnussana ei ole oikein. Jokaisessa
## silmukan kierroksessa ohjelma kysyy tunnussanaa ja kun käyttäjä antaa oikean tunnussanan, silmukan
## ehto ei ole enää voimasssa ja silmukka päättyy.

## Esimerkissä ohjelman suoritus etenee seuraavasti:
## 
##     Muuttuja sana saa alkuarvon "".
##     Ohjelma saapuu silmukkaan.
##     Ehto sana != "python" pätee ja ohjelma suorittaa silmukan koodin.
##     Silmukassa sana saa arvon "kissa".
##     Ohjelma palaa silmukan alkuun.
##     Ehto sana != "python" pätee ja ohjelma suorittaa silmukan koodin.
##     Silmukassa sana saa arvon "putka".
##     Ohjelma palaa silmukan alkuun.
##     Ehto sana != "python" pätee ja ohjelma suorittaa silmukan koodin.
##     Silmukassa sana saa arvon "python".
##     Ohjelma palaa silmukan alkuun.
##     Ehto sana != "python" ei päde ja silmukka päättyy.

########### for-silmukka ###########3

## Seuraava ohjelma tulostaa lukujen 0–9 neliöt eli luvut korotettuna toiseen potenssiin. 
## Esimerkiksi luvun 5 neliö on 25, koska 5 potenssiin 2 = 5 * 5 = 25.


for i in range(10):
    print("Luvun", i, "neliö on", i * i)

## Ohjelman tulostus on seuraava:
## Luvun 0 neliö on 0
## Luvun 1 neliö on 1
## Luvun 2 neliö on 4
## Luvun 3 neliö on 9
## Luvun 4 neliö on 16
## Luvun 5 neliö on 25
## Luvun 6 neliö on 36
## Luvun 7 neliö on 49
## Luvun 8 neliö on 64
## Luvun 9 neliö on 81

## Ohjelmassa on for-silmukka, joka käy läpi joukon tietoja ja suorittaa joka tiedon kohdalla saman koodin.
## Tässä range(10) tarkoittaa, että silmukka käy läpi kymmenen ensimmäistä kokonaislukua nollasta alkaen.
## Jokaisella silmukan kierroksella muuttuja i saa arvokseen käsiteltävän kokonaisluvun.

## Esimerkissä ohjelman suoritus etenee seuraavasti:
##     Muuttuja i saa arvon 0.
##     Ohjelma suorittaa silmukan sisällä olevan koodin.
##     Muuttuja i saa arvon 1.
##     Ohjelma suorittaa silmukan sisällä olevan koodin.
##     Muuttuja i saa arvon 2.
##     Ohjelma suorittaa silmukan sisällä olevan koodin.
##     (jne.)

## Lukuväliin liittyy kolme parametria: mistä luvusta silmukka alkaa, minkä luvun kohdalla silmukka päättyy ja
## kuinka paljon luku kasvaa silmukan kierroksen jälkeen. Oletuksena silmukka alkaa nollasta ja luku kasvaa
##  yhdellä kierroksen jälkeen. Seuraavassa on esimerkkejä lukuväleistä:

## merkintä	            lukuväli
## range(10)	        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
## range(5, 15)	        5, 6, 7, 8, 9, 10, 11, 12, 13, 14
## range(-6, 3)	        -6, -5, -4, -3, -2, -1, 0, 1, 2
## range(24, 16, -1)	24, 23, 22, 21, 20, 19, 18, 17
## range(3, 20, 2)	    3, 5, 7, 9, 11, 13, 15, 17, 19
## range(35, 4, -4)	    35, 31, 27, 23, 19, 15, 11, 7

## Opassarjan seuraavissa osissa nähdään, mitä muuta for-silmukalla voi tehdä kuin käydä läpi lukuvälejä.

################ Keskeytys #################

## Tunnussanan kysymisen voi toteuttaa myös seuraavasti:

while True:
    sana = input("Kirjoita tunnussana: ")
    if sana == "python":
        break
print("Tervetuloa!")

## Tässä silmukan alussa on ehto True, joka on aina tosi eikä rajoita silmukan toistamista. Kuitenkin silmukan 
## sisällä komento break keskeyttää silmukan, jos käyttäjä antaa oikean tunnussanan. Silmukan toimintatapa on
## siis ennallaan, mutta ehdon sijainti poikkeaa aiemmasta.

## Komentoa break voi käyttää kaikissa silmukoissa: while-silmukassa se keskeyttää silmukan, vaikka alkuehto
##  olisi voimassa, ja for-silmukassa se keskeyttää silmukan, vaikka kaikkia tietoja ei olisi vielä käsitelty.

################## Uusi kierros ################

## Seuraava ohjelma tulostaa parittomien lukujen neliöitä:

for i in range(10):
    if i % 2 == 0:
        continue
    print("Luvun", i, "neliö on", i * i)

## Ohjelman tulostus on seuraava:

## Luvun 1 neliö on 1
## Luvun 3 neliö on 9
## Luvun 5 neliö on 25
## Luvun 7 neliö on 49
## Luvun 9 neliö on 81

## Tässä silmukan sisällä on komento continue, joka siirtyy silmukassa uudelle kierrokselle, jos käsiteltävä
##  luku on parillinen. Komennon vaikutuksesta silmukan loppuosa jää suorittamatta, jos luku on parillinen,
##  eli silmukka tulostaa vain parittomien lukujen neliöt.

## Komentoa continue voi käyttää kaikissa silmukoissa: while-silmukassa se palaa silmukan alkuun ehdon
## tarkistukseen, ja for-silmukassa se palaa silmukan alkuun ja siirtyy seuraavan tiedon käsittelyyn.

################## Esimerkki: Viljanjyvät ############

## Tarinan mukaan shakkipelin keksijä pyysi palkkiokseen yhden viljanjyvän shakkilaudan ensimmäiseen ruutuun,
## kaksi toiseen ruutuun, neljä kolmanteen ruutuun, kahdeksan neljänteen ruutuun jne., siis joka ruutuun
## kaksinkertaisen määrän jyviä edelliseen ruutuun verrattuna.

## Seuraava ohjelma laskee, kuinka monta viljanjyvää shakkilaudan kuhunkin ruutuun tulisi ja kuinka monta
## viljanjyvää shakkilaudalla olisi yhteensä.

jyvat = 1
kaikki = 0
for ruutu in range(64):
    print("Ruudussa", ruutu + 1, "on", jyvat, "jyvää")
    kaikki += jyvat
    jyvat *= 2
print("Yhteensä", kaikki, "jyvää")

## Ohjelman tulostus on seuraava:

## Ruudussa 1 on 1 jyvää
## Ruudussa 2 on 2 jyvää
## Ruudussa 3 on 4 jyvää
## Ruudussa 4 on 8 jyvää
## ... (välissä rivejä)
## Ruudussa 61 on 1152921504606846976 jyvää
## Ruudussa 62 on 2305843009213693952 jyvää
## Ruudussa 63 on 4611686018427387904 jyvää
## Ruudussa 64 on 9223372036854775808 jyvää
## Yhteensä 18446744073709551615 jyvää

## Shakkipelin keksijän palkkiota ei pystytty koskaan maksamaan, koska koko maailmassa ei ole näin monta viljanjyvää.


################## Esimerkki: Suorakulmiot #################


## Seuraava ohjelma tulostaa suorakulmioita käyttäjän ohjeiden mukaisesti:

while True:
    korkeus = int(input("Korkeus: "))
    leveys = int(input("Leveys: "))
    if korkeus <= 0 or leveys <= 0:
        # negatiiviset arvot eivät kelpaa
        continue
    for y in range(korkeus):
        for x in range(leveys):
            # end = "" tarkoittaa, että ei tulosteta loppuun rivinvaihtoa
            print("*", end = "")
        # tässä taas tulostetaan pelkkä rivinvaihto
        print()
    vastaus = input("Haluatko jatkaa (k/e)? ")
    if vastaus == "e":
        break

## Ohjelman tulostus voi olla seuraava:

## Korkeus: 4
## Leveys: 5
## *****
## *****
## *****
## *****
## Haluatko jatkaa (k/e)? k
## Korkeus: 2
## Leveys: 10
## **********
## **********
## Haluatko jatkaa (k/e)? k
## Korkeus: 6
## Leveys: 3
## ***
## ***
## ***
## ***
## ***
## ***
## Haluatko jatkaa (k/e)? e

## Ohjelman pääsilmukka on while-silmukka, jonka jokaisella kierroksella ohjelma tulostaa yhden suorakulmion
## for-silmukan avulla. Ensimmäinen for-silmukka tulostaa yhden suorakulmion rivin, ja toinen for-silmukka
## tulostaa yhden rivillä olevan merkin.


################# Esimerkki: Luvun tekijät ############

## Luvun jakaminen tekijöihin tarkoittaa, että luku esitetään kertolaskuna, jossa olevia lukuja
## (tekijöitä) ei voi enää jakaa osiin. Toisin sanoen luku esitetään alkulukujen tulona. Esimerkiksi luvun
## 15 tekijät ovat 3 ja 5, koska 3 * 5 = 15, ja luvun 44 tekijät ovat 2, 2 ja 11, koska 2 * 2 * 11 = 44.
## Luku 31 on alkuluku, joten sitä ei voi jakaa osiin.

## Seuraava ohjelma jakaa annetun luvun tekijöihin:

luku = int(input("Anna luku: "))
tekija = 2
while tekija <= luku:
    while luku % tekija == 0:
        luku //= tekija
        if luku > 1:
            # tulostetaan " * ", ellei kyseessä ole viimeinen tekijä
            print(tekija, end = " * ")
        else:
            # viimeisen tekijän jälkeen tulee normaalisti rivinvaihto
            print(tekija)
    tekija += 1

## Seuraavassa on muutamia ohjelman tulostuksia:

## Anna luku: 15
## 3 * 5

## Anna luku: 44
## 2 * 2 * 11

## Anna luku: 31
## 31

## Ohjelma käy läpi mahdollisia luvun tekijöitä 2:sta alkaen. Jokaisen tekijän kohdalla luku jaetaan tekijällä ja
## tekijä tulostetaan, kunnes luku ei ole enää jaollinen tekijällä. Ohjelma päättyy, kun kokeiltava tekijä on lukua
## suurempi. Käytännössä tällöin luku on jakolaskujen seurauksena 1.
