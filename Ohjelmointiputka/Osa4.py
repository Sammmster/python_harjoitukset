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