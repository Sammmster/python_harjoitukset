#! /usr/bin/python3

## vertailu     milloin tosi?
## x == y       x on sama kuin y
## x != y       x ei ole sama kuin y
## x < y        x on pienempi kuin y
## x <= y       x on pienempi tai sama kuin y
## x > y        x on suurempi kuin y
## x >= y       x on suurempi tai sama kuin y
## Jos vertailussa ovat lukuarvit, "pienempi" ja "suurempi" tarkoittavat lukujen
## suuruusjärjestystä. Jos vertailussa ovat merkkijonot, pienempi ja suurempi tarkoittava
## merkkijonojen aakkosjärjestystä, joka riippuu siitä, missä järjestyksessä merkit ovat
## käytössä merkistössä.

####### ehtorakenne ###################
## Ehtorakenne muuttaa ohjelman suoritusta sen mukaan onko jokin totuusarvo tosi vai epätosi
## eli pitääkö jokin ehto paikkansa vai ei. Seuraava ohjelma tervehtii käyttäjää vain, jos
## hänen nimensä on Henrikki.

nimi = input("Nimi: ")
if nimi == "Sami":
    print ("Hoi, sankari!")
    print ("Minne makta?")
print ("Ei muuta...")

### (jos nimi ei ole Sami)
## Nimi: Topi
## Ei muuta

### (jos nimi on Sami)
## Nimi: Sami
## Hoi, sankari!
## Minne matka?
## Ei muuta...

## Ehtorakenteen aloittaa if-sana, jonka jälkeen totuusarvomuotoinen ehto. Jos ehto on tosi,
## ohjelma suorittaa ehtorakenteen sisällä olevat rivit. Muuten ohjelma hyppää ehtorakenteen
## yli. Tässä ehto on tosi jos nimi on Sami.

############ lisää ehtoja ###############

## Seuraava ohjelma tervehtii Samia eri tavoin kuin muita. Ohjelma sanoo Samille "Moi sankari!"
## ja kaikille muille "Hellurei!"

nimi = input("Nimi: ")
if nimi == "Sami":
    print("Hoi, sankari!")
else:
    print("Hellurei!")

### Ohejelman voi toteuttaa myös näin:
## nimi = input("Nimi: ")
## if nimi == "Sami":
##    print("Hoi, sankari!")
## else:
##    print("Hellurei!")

### Tässä ohjelman erilaiset tulokset:
## Nimi: Sami
## Hoi, sankari!

## Nimi: Topi
## Hellurei!

## Ylempänä. Nyt ehtorakenteen lopussa on else-sana, jonka ohjelma suorittaa jos alussa oleva
## ehto ei ole tosi.

## Seuraava ohjelma sisältää omat tervehdykset Samille, Antille ja Uoleville. Kaikkia muita
## ohjelma tervehtii samalla tavalla.

nimi = input("Nimi: ")
if nimi == "Sami":
    print("Hoi Sankari!")
elif nimi == "Antti":
    print ("Morjens")
elif nimi == "Uolevi":
    print ("Tsaukki")
else:
    print("Hellurei!")

## Tämä on ehtorakenteen laajin muoto: Ohjelma suorittaa ensimmäisen if- tai elif -osan,
## jos vastaava ehto on tosi. Jos mikään ehto ei ole tosi, ohjelma suorittaa else -osan.
## Ehtorakenteesta voi aina puuttua else -osa, jolloin ohjelma ei tee mitään, jos mikään
## ehto ei ole tosi.

######## totuusarvojen yhdistys #########
## yhdistys     Milloin tosi?
## a and b      A on tosi ja B on tosi
## a or b       A on tosi tai B on tosi
## not a        A ei ole tosi

## Ehtorakenteessa yhdistyksen and avulla voidaan tarkistaa päteekö monta ehtoa yhtä aikaa,
## ja yhdistyksen or avulla voi tarkistaa, päteekö ainakin yksi ehdoista.

## Seuraava ohjelma tarkistaa, ovatko käyttäjän tunnus ja salasana oikein.
tunnus = input("Tunnus: ")
salasana = input("Salasana: ")
if tunnus == "Sami" and salasana == "abc":
    print("Oikein")
else:
    print("Väärin")
## Ohjelma tulostaa "Oikein" jos tunnus on Sami ja salasana on abc

## Seuraava ohjelma tarkistaa käyttäjän iän
ika = int(input("Ikä: "))
if ika < 0 or ika > 120:
    print("Mahdotonta")

## Jos totuusarvo on monimutkainen, sulkujen avulla voi varmistaa että Python tulkitsee sen oikein.
## Esimerkiksi on vaikeaa tietää, miten python tulkitsee totuusarvon tunnus == "antti" and salasana == "abc"
## or suojaus == 0. Sulkujen avulla pystyy erottamaan mahdolliset tulkinnat:
## 1) (tunnus == "antti" and salasana == "abc") or suojaus == 0
## 2) tunnus == "antti" and (salasana == "abc" or suojaus == 0)
## Ensimmäisessä tapauksessa riittää, että tunnus ja salasana on oikein tai suojaus on 0. Toisessa tapauksessa
## ensinnäkin tunnuksen täytyy olla oikein ja lisäksi salasanan täytyy olla oikein tai suojauksen täytyy olla 0.

########### esimerkki: tietokilpailu ##############
## Seuraava ohjelma kysyy käyttäjältä kolme kysymystä. Jokaisesta oikeasta vastauksesta saa pisteen ja ohjelma
## ilmoittaa lopuksi pistemäärän.

print("Tervetuloa tietokilpailuun!")
pisteet = 0

vastaus = input("Kuinka monta sekunttia on tunnissa?\n")
if vastaus == "3600":
    print("Oikein")
    pisteet += 1
else:
    print("Väärin")

vastaus = input("Minä vuonna Sibelius kuoli?\n")
if vastaus == "1957":
    print("Oikein")
    pisteet += 1
else:
    print("Väärin")

vastaus = input("Mikä on Bulgarian pääkaupunki?\n")
if vastaus == "Sofia":
    print("Oikein")
    pisteet += 1
else:
    print("Väärin")

print("Pisteet: ", pisteet)

## Ohjelmassa muuttuja pisteet on laskurimuuttuja, jonka arvo on aluksi nolla ja jonka arvo kasvaa yhdellä aina, kun
## käyttäjä vastaa kysymykseen oikein. Lyhennys "pisteet += 1" tarkoittaa samaa "pisteet = pisteet +1".
## Vastaavaa merkintää voi käyttää myös muiden laskutoimitusten kanssa.

####### Esimerkki: Arvaaja ###############

## Seruaava ohjelma arvaa käyttäjän ajatteleman viikonpäivän. Ohjelma kysyy korkeintaan kolme kyllä/ei kysymystä.

print("Ajattele jotain viikonpäivää!")

alku = "Onko viikonpäivän nimessä "
loppu = "-kirjain (k/e)?"

if input(alku + "n" + loppu) == "k":
    if input(alku + "u + loppu") == "k":
        if input(alku + "s" + loppu) == "k":
            tulos = "sunnuntai"
        else:
            tulos = "lauantai"
    else:
        if input(alku + "r" + loppu) == "k":
            tulos = "perjantai"
        else:
            tulos = "maanantai" 
else:
    if input(alku + "k" +loppu) == "k":
        tulos = "keskiviikko"
    else:
        if input(alku + "r" +loppu) == "k":
            tulos = "torstai"
        else:
            tulos = "tiistai"

print("Viikonpäivä on " + tulos + "!")

### Ohjelman tulostus voi olla seuraava:
## Ajattele jotain viikonpäivää!
## Onko viikonpäivän nimessä n-kirjain (k/e)? e
## Onko viikonpäivän nimessä k-kirjain (k/e)? e
## Onko viikonpäivän nimessä r-kirjain (k/e)? k
## Viikonpäivä on torstai!

## Ohjelma sisältää paljon sisäkkäisiä ehtorakenteita, joissa liikutaan sen mukaan, mitä vastauksia käyttäjä
## antaa kysymyksiin. Ohjelman täytyy tulostaa monessa kohdassa melkein samanlainen kysymys, minkä vuoksi
## kysymyksen alkuosa ja loppuosa haetaan muuttujista. Kuten ohjelmasta näkyy, input- funktion tulos voi olla
## suoraan osana ehtoa.

