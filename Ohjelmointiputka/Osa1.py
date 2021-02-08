#! /usr/bin/python3
# https://www.ohjelmointiputka.net/oppaat/opas.php?tunnus=python3_01

# tervehdyksen tulostus
print("Tervetuloa!")

# tunnussanan kysyminen
sana = input("Kirjoita tunnussana: ")

# seuraava tulostus riipuu tunnussanasta
if sana == "python":
    print("Matka voi alkaa...")
else:  
    print("Yritä uudelleen...")