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

lista = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu",
        "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"] 
kuukausi = int(input("Anna kuukausi (1-12): "))
if 1 <= kuukausi <= 12:
    print("Kuukauden nimi:", lista[kuukausi - 1])
else:
    print("Kuukausi ei kelpaa!")

## Ohjelman tulostus voi olla seuraava:
## Anna kuukausi (1-12): 9
## Kuukauden nimi syyskuu

## Ohjelman toiminta perustuu siihen, että listan alkioon voi viitata muuttujan avulla. Listassa kauukausin
## numerointi alkaa nollasta, minkä vuoksi ohjelma pienentää yhden käyttäjän antamaan numeroa. Esimerkiksi
## jos käyttäjä antaa numeron 9, ohjelma hakee kuukauden nimen kohdasta lista[8].