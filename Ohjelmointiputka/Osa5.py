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

print("Tässä vielä koko joukko:")
print (nimet)

