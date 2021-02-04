#! /usr/bin/python3

eka_lista = [12,21,54,12,75]
print(eka_lista)
# printtaa koko listan

print(eka_lista[0])
# printtaa koko listan +ensimmäisen numeron eli 12, 
# koska 0 vastaa listan ensimmäistä indeksiä

toka_lista = ["tämä", "on", "toinen", "listamme"]
print (toka_lista)
# eli lista voi sisältää myös sanoja eikä vain numeroita.
print(toka_lista[0])
# printtaa sanan "tämä" koska se on index 0

toka_lista[1] ="ei ole"
print(toka_lista)
# listan sisältöä voidaan muuttaa "lennossa"

## toka_lista[4] = "toimiiko"
## tämä antaa virheilmoituksen koska indeski numero 4ää, eli 5ttä ei ole olemassa

eka_lista.append("toimiiko")
print(eka_lista)
kolmas_lista = eka_lista + toka_lista
print(kolmas_lista)
## listoja voidaan myös yhdistää

kolmas_lista[0] = eka_lista
print(kolmas_lista)

print(kolmas_lista[0][0])
# tämä printtaa ensimmäisen listan ensimmäisen indexin

print(toka_lista)
eka_muuttuja = toka_lista.pop(0)
# pop on funktio joka tulee aina () sulkujen väliin, oli siinä numero tai ei
print(toka_lista)
print(eka_muuttuja)
# pop poistaa halutun elementin listalta, anna haluttu indexi parametriksi.
# poistaa viimeisen jos parametriä ei anneta

for mita_tahansa in toka_lista:
    print(mita_tahansa)
# käy läpi toka_lista yksi kerrallaan ja printtaa ne omille riveilleen

print(len(toka_lista))
# printtaa miten pitkä (lenght) toka lista on

for i in range(len(toka_lista)):
    print(toka_lista[i])
# sama kun edellinen for käsky, vain eri tavalla
# puhutaan myös iteraatiosta

for i in range(8):
    print("luku" + str(i))
# printtaa sanat luku0-luku7 jokaiselle riville

for i in range(30):
    print("luku" + str(i))
    if i == 9:
        break
# katkaisee indexin luvun ja printtauksen numeroon 9 eli indesiin numero 10




