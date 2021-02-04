#! /usr/bin/python3
# aloita aina polusta mistä python löytyy

# Tämä on kommentti

#"""
#Tämä
#on
#useamman
#rivin
#kommentti
#"""

ensimmainen_muuttuja = 1
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = "hello world!"
print(ensimmainen_muuttuja)
# kuten huomataan niin muuttuja voi olla 2 eri asiaa

ensimmainen_muuttuja = 'hello world2'
print (ensimmainen_muuttuja)
# myös tämä esitystapa toimii
# muuttuja muuttujassa "hello 'käyttäjä' "

ensimmainen_muuttuja = 10
print(ensimmainen_muuttuja)
# muuttuja muuttuu, yllätys :)

# luku integer
# kirjain string

print(ensimmainen_muuttuja +3)
# print(ensimmainen_muuttuja) #huom, tämä tulostaa 10 eikä 13
# eli tämä vain laskee muuttujan päälle 3

ensimmainen_muuttuja = ensimmainen_muuttuja +4
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = "hello world"
print(ensimmainen_muuttuja)
ensimmainen_muuttuja = ensimmainen_muuttuja + ", I say"
print(ensimmainen_muuttuja)

jaettava = 7
print(type(jaettava))
jakaja = 2
print(type(jakaja))

tulos = jaettava / jakaja
print(type(tulos))
print(tulos)

kokonaisluku_tulos = jaettava // jakaja
print(type(kokonaisluku_tulos))
print(kokonaisluku_tulos)

jakojaannos = jaettava % jakaja
print(jakojaannos)

print(7/2)
print(7//2)
print(7%2)

print("tulos oli: " +str(tulos)) #tässä tulostetaan string + numero

# kertolasku
kerrottava_luku1 = 5
kerrottava_luku2 = 3
kertolaskun_tulos = kerrottava_luku1 * kerrottava_luku2
print(kertolaskun_tulos)

# potenssilasku
kerrottava_luku2_potenssiin_kolme = kerrottava_luku2 * kerrottava_luku2 * kerrottava_luku2
print(kerrottava_luku2_potenssiin_kolme)

kolmen_potenssi_kolmeen = kerrottava_luku2 **3
print(kolmen_potenssi_kolmeen)

kantaluku = 2
potenssi = 8
potenssin_tulos = kantaluku ** potenssi
print(potenssin_tulos)

ehto_muuttuja = "kylla"
if ehto_muuttuja == "kylla": #huom vertailussa käytetään muotoa == vertailuun, ja loppuu : kaksoispisteeseen
    print("tosi")
ehto_muuttuja = "ei"
if ehto_muuttuja == "kylla":
    print("tosi")

ehto_muuttuja_2 = 1
ehto_muuttuja = "ei"
if ehto_muuttuja == "kylla":
    print("tosi")
    if ehto_muuttuja_2 == 1:
        print("kuin vesi")
else:
    print("ei ole tosi") #huomaa sisennys

####################################################
ehto_numero = 10

if ehto_numero > 10:
    print("numero on suurempi kuin 10")
# 2 peräkkäistä if lausetta tarkistetaan molemmat lausekkeet
# elif käskyssä jälkimmäinen toteutetaan vain jos ensimmäinen täyttyy
elif ehto_numero < 10:
    print("numero on pienempi kuin 10")
elif ehto_numero == 10:
    print("numero on tasan 10")
####################################################

#kayttajan_vastaus = input("onko python hyva kieli")
#print("vastasit kysymykseen, onko python hyva kieli: ", kayttajan_vastaus)

#kayttajan_vastaus = input("anna numero")
#print(type(kayttajan_vastaus))

#kayttajan_vastaus_int = int(kayttajan_vastaus)
#print(type(kayttajan_vastaus_int))


#kysy kayttajalta kaksi numeroa, ja tulosta niiden summa

luku1 = int(input("anna numero1: "))
luku2 = int(input("anna numero2: "))
tulos = luku1 + luku2
#print("lukujen summa on: " + str(tulos)) #samat asiat kun alempi
print("lukujen summa on: ", tulos)

#luku3 = input("anna numero", tulos) #tämä ei toimi

