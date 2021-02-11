#! /usr/bin/python3

############## Osa 5 - Listojen käsittely ###############

## Listojen avulla ohjelma voi käsitellä kätevästi suurta määrää tietoa.
## Esimerkiksi jos ohjelman muistissa ovat sadan käyttäjän nimet, niiden
## tallentaminen erillisiin muuttujiin nimi1, nimi2, nimi3..., nimi100 olisi
## hankalaa. Kun nimet ovat listassa, kaikkiin nimiin voi viitata helposti 
## yhden muuttujan nimen kautta.
## 
## Listojen merkittävä etu on että ohjelman rakenne pysyy samana,
## vaikka tiedon määrä olisi vaihteleva. Esimerkiksi nimien käsittelyssä
## samanlainen ohjelma kelpaa tilanteissa, jossa nimiä on viisi, sata ja 
## miljoona. Lisäksi vaikka tiedon määrä olisi pieni, listat voivat selventää
## ohjelman rakennetta.
## 
## Lista on yleisin Python -kielen valmiista tietorakenteista ja soveltuu
## moniin ohjelmointitehtäviin.

############## Lista ###########################
## Lista on muuttuja, joka sisältää kokoelman alkioita tietyssä järjesyksessä.
## Listassa olevat alkiot voivat olla esimerkiksi lukuja tai merkkijonoja.
## 
## Seuraavassa ohjelmassa on lista "nimet", joka sisältää nimet Sami, Uolevi ja
## Antti. Ohjelma tulostaa ensin nimet yksi kerrallaan ja sitten uudestaan koko
## listan. Tämän jälkeen ohjelma muuttaa Uolevin nimeksi Einari ja tulostaa koko listan.

"""
nimet = ["Sami", "Uolevi", "Antti"]
## Huom että tuossa on hakasulkeet, eivät tavalliset sulkumerkit.
print ("Ensin tulee", nimet [0])
print ("Sitten on", nimet [1])
print ("Viimeisenä on", nimet [2])

print("Tässä vielä koko joukko:")
print (nimet)

nimet[1] = "Einari"
print("Toinen onkin", nimet[1])
# Tässä vaihdetaan listan toinen nimi Uolevi Einariksi. Listan muuttujia voi muuttaa
# kuten mitä muuta muuttujaa tahansa.

# print("Tässä vielä koko joukko:", nimet)
# jompikumpi tapa. Ylempi tulostaa koko joukon samalle riville lauseen kanssa.
print ("Tässä vielä koko joukko:")
print (nimet)
"""

## Ohjelman tulostus on seuraava:

# Ensin tulee Henrikki
# Sitten on Uolevi
# Viimeisenä on Antti
# Tässä vielä koko joukko:
# ['Henrikki', 'Uolevi', 'Antti']
# Toinen onkin Einari
# Tässä vielä koko joukko:
# ['Henrikki', 'Einari', 'Antti']

## Listan luonissa alkiot merkitään hakasulkujen sisään pilkulla erotettuna. Tämän jälkeen alkioihin voi viitata
## kokonaisluvuin nillasta alkaen: tässä nimet[0] on ensimmäinen nimi, nimet[1] on toinen nimi ja nimi[2]
## on kolmas nimi. Listan koko sisällön voi tulostaa antamalla pelkän listan nimen print-komennolle.

####################### esimerkki kuukaudet ######################
## Yksi listan käyttötarkoitus on, että se toimii ohjelman tietovarastona. Seuraavassa ohjelmassa lista sisältää
## kuukausien nimet suomeksi, jolloin ohjelman on helppo nimetä käyttäjän antama kuukausi.

"""
lista = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu",
        "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"] 
kuukausi = int(input("Anna kuukausi (1-12): "))
if 1 <= kuukausi <= 12:
    print("Kuukauden nimi:", lista[kuukausi - 1])
else:
    print("Kuukausi ei kelpaa!")
"""

## Ohjelman tulostus voi olla seuraava:
## Anna kuukausi (1-12): 9
## Kuukauden nimi syyskuu

## Ohjelman toiminta perustuu siihen, että listan alkioon voi viitata muuttujan avulla. Listassa kauukausin
## numerointi alkaa nollasta, minkä vuoksi ohjelma pienentää yhden käyttäjän antamaan numeroa. Esimerkiksi
## jos käyttäjä antaa numeron 9, ohjelma hakee kuukauden nimen kohdasta lista[8].

######### Listassa oleminen ###############
## Totuusarvo "alkio in lista" on tosi, jos alkio on listassa. Vastaavasti totuusarvo "alkio not in lista" on tosi,
## jos alkio ei ole listassa. Seuraava ohjlema tulostaa eri viestin listassa oleville käyttäjille.

"""
sakki = ["Sami", "Uolevi", "Antti"]
nimi = input("Anna nimi: ")
if nimi in sakki:
    pritn("Mitä uutta, kuoma?")
else:
    print("Et kuulu sisäpiiriin")
"""

## Tässä on ohjelman mahdollisia tulostuksia:
## Anna nimi: Sami
## Mitä uutta, kuoma?

## Tässä on ohjelman mahdollisia tulostuksia:
## Anna nimi: Topi
## Et kuulu sisäpiiriin

## Jos nimi on Sami, Uolevi tai Antti, ohjlema tulostaa viestin "Mitä uutta, kuoma?". Muuten ohelma tulostaa
## veistin "Et kuulu sisäpiiriin"


############### Alkion lisääminen ########################
## Listaan voi lisätä alkioita metodilla append. Seuraavassa esimerkissä lista on alkuksi tyhjä ja ohjelma lisää
## siihen käyttäjän antamia sanoja. Ohjelma päättyy, kun käyttäjä antaa saman sanan uudelleen.

"""
lista = []
while True:
    sana = input("Kirjoita sana: ")
    if sana not in lista:
        lista.append(sana)
    else:
        print("Kirjoitit saman sanan uudelleen!")
        break
"""

## Ohjelman tulostus voi olla seuraava:
## Kirjoita sana: talo
## Kirjoita sana: metsä
## Kirjoita sana: auto
## Kirjoita sana: tie
## Kirjoita sana: talo
## Kirjoitit saman sanan uudelleen!

##################### Listan läpikäynti ###################
## Listassa olevat alkiot voi käydä läpi for-silmukalla. Silmukalle annetaan muuttuja ja lista, jonka jälkeen
## muutujan arvo on silmukan joka kierroksella vuorollaan yksi listan alkioista.
"""
nimet = [
    "maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"
]
for nimi in nimet:
    print(nimi)
"""

## Ohjelman tulostus on seuraava:
## maanantai
## tiistai
## keskiviikko
## torstai
## perjantai
## lauantai
## sunnuntai

## Seuraava ohjelma kysyy käyttäjältä sanoja, kunnes käyttäjä antaa tyhjän sanan. Sitten ohjelma tulostaa
## sanojen määrän ja kaikki sanat

"""
lista = []
while True:
    sana = input("Kirjoita eri sanoja: ")
    if sana == "":
        break
    lista.append(sana)
print("Kirjoitit", len(lista), "sanaa.")
print("Sanat ovat:")
for sana in lista:
    print(sana, end = " ")
print()
"""

## Tässä funktio len kertoo kuinka monta alkiota listassa on

################ listan metodit #############
## listaan liittyvät mm. seuraavat metodit:
##  metodi                  selitys
## lista.append(alkio)      lisää alkion listaan
## lista.index(alki)        etsii alkion kohdan listassa
## lista.count(alkio)       laskee alkion esiintymiskerran listassa
## lista.remove(alkio)      poistaa alkion listasta
## lista.sort()             järjestää listan alkiot
## lista.reverse()          kääntää listan toisinpäin

## Seuraava ohjelma etsii listasta käyttäjän antaman kuukauden:

"""
lista = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu",
        "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"] 
nimi = input ("Anna kuukauden nimi: ")
if lista.count(nimi) == 0:
    print("Kuukausi ei kelpaa!")
else:
    print ("Kuukauden numero:", lista.index(nimi) +1)
"""

## Ohjelman tulostus voi olla seuraava:
## Anna kuukauden nimi: tammikuu
## Kuukauden numero: 1

## Tällä kertaa kuukauden kohtaan listassa pitää lisätä yksi, jotta tuloksena on tuttu kuukauden
## numero. Esimerkiksi jos kuukausi on syyskii se on listassa kohdassa [8] ja
## ohjelma ilmoittaa numeroksi 9.

############### Esimerkki: Presidentit ##################
## Seuraava ohjelma tarkistaa kuinka monta presidenttiä käyttäjä muistaa:

"""
lista = [
    "Ståhlberg", "Relander", "Svinhufvud",
    "Kallio", "Ryti", "Mannerheim",
    "Paasikivi", "Kekkonen", "Koivisto",
    "Ahtisaari", "Halonen", "Niinistö"
]
print("Kuinka monta presidenttiä muistat?")
maara = 0
while len(lista) > 0:
    nimi = input("Nimi: ")
    if nimi == "":
        break
    if nimi in lista:
        print("Oikein!")
        maara += 1
        # kokeile maara +1
        lista.remove(nimi)
    else:
        print("Ei kelpaa!")
print("Muistit", maara, "Presidenttiä!")
"""

## Ohjelman alussa lista sisältää kaikkien presidenttien nimet. Aina kun käyttäjä muistaa presidentin, ohjelma
## poistaa sen listasta. Tämän ansiosta käyttäjä ei voi kerätä pisteitä antamalla saman nimen monta kertaa.
## Ohjelma päättyy jos käyttäjä antaa tyhjän nimen tai muistaa kaikki nimet.

################# Esimerkki: lukutilasto ###################
## Seuraava ohjelma lisää käyttäjän antamia lukuja listaan kunnes käyttäjä antaa luvun nolla. Sitten ohjelma
## ilmoittaa listan pienimmän ja suurimman luvun, listan lukujen summan sekä järjestyksessä kaikki eri luvut
## esiintymiskertoineen.

"""
print("Ohjelma päättyy kun annat numeron 0")
lista = []
while True:
    luku = int(input("Kirjoita luku: "))
    if luku == 0:
        break
    lista.append(luku)
print("Pienin luku:", min(lista))
print("Suurin luku:", max(lista))
print("Lukujen summa:", sum(lista))
lista.sort()
vanha = 0 # Listassa ei ole lukua nolla 0
for luku in lista:
    if luku != vanha:
        print("Luku", luku, "on listassa", lista.count(luku), "kertaa.")
    vanha = luku
"""
## Funktiot min, max ja sum kertovat listan pienimmän luvun, suurimman luvun ja lukujen summan. Ohjelma
## käy lopuksi läpi kaikki luvut mutta tulostaa jokaisen eri luvun vain kerran. Tämä vuoksi ohjelma pitää
## muistissa muuttujassa "vanha" edellisen kierroksen luvut.