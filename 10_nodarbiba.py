#Uzdevums: Uzrakstat programmu, 
# kurā lietotājs ievada vairāku
# cilvēku datus (vārds; uzvārds, vecums). 
# Visiem laukiem jābūt atsevišķi 
# (t.i. neapvienojat vārdu un uzvārdu).
# Individuālu cilvēka dati jāsaglabā vārdnīcā. 
# Visu cilvēku datus varat apvienot 
# datu struktūrā pēc jūsu izvēles.
# (^ Šis bija iepriekšējā stundā uz i/ni)
# Saglabājat šos datus failā. 
# Uzsākot programmu izvadat šos datus.
# Pagaidām sākumā izveidojat tukšu 
# failu manuāli, lai mēģinot nolasīt
# nav kļūda (mēģinot atvērt neeksistējošu 
# failu ar r izmetīs kļūdu)
# import json
# import os

# if os.path.isfile("cilveki.json"): # True ja fails eksistē, false, ja neeksistē
#     with open("cilveki.json", "r", encoding="UTF-8") as f:
#         print(json.load(f))

# # Piemērs ievadei:
# cilveki = []
# while True:
#     vards = input("Ievadi vārdu: ")
#     uzvards = input("Ievadi uzvārdu: ")
#     vecums = int(input("Ievadi vecumu: "))

#     cilveks ={
#         "vards": vards,
#         "uzvards": uzvards,
#         "vecums": vecums,
#     }

#     cilveki.append(cilveks)

#     turp = input("Vēlies ievadīt vēlvienu cilvēku?")
#     if turp=="nē":
#         break

# with open("cilveki.json", "w", encoding="UTF-8") as f:
#     json.dump(cilveki, f)

# Faila pārbaude -- vai fails eksistē
# os.path.isfile("cilveki.json")
# Mapes pārbaude -- vai eksistē mape
# os.path.isdir("mape")
# Pārbauda vai ceļš eksistē (mape VAI fails -- neizvada kurš)
# os.path.exists("mape/fails")

import sys
import os
# Pašreizējā faila atrašanās vieta
# Speciāls mainīgais, kurš satur pašreizējā skripta atrašanās vietu
# print(os.path.dirname(__file__))
# print(__file__)
# print(sys.argv[0]) 
# print(sys.argv[1])
# print(sys.argv[2])

import os
pasreizeja_mape = os.path.dirname(__file__)
# .\\ -- Pašreizējā mape
# ..\\ -- Mape vienu līmeni augstāk
# ..\\.. - Mape divus līmeņus augstāk
# U.t.t.
# with open(f"{pasreizeja_mape}\\..\\..\\cilveki.json", "w", encoding="UTF-8") as f:
#     f.write("!")

# import pathlib
# p = pathlib.Path('/path/to/my/file')
# p.parents[0]

# Izveido mapi
# Piez. šie ceļi ir tikai demonstrācijai kā miksēt absolūtus ceļus (C:/mape) ar relatīviem (../mape).
print(f"{pasreizeja_mape}\\..\\11-6-2024\\test")
if not os.path.isdir(f"{pasreizeja_mape}\\..\\11-6-2024\\test"):
    os.mkdir(f"{pasreizeja_mape}\\..\\11-6-2024\\test")
    with open(f"{pasreizeja_mape}\\test\\cilveki.json", "w", encoding="UTF-8") as f:
        f.write("!")

# # Izdzēst visu mapi ar failiem tajā
# for file in os.listdir("test"):
#     os.remove(f"test\\{file}") # Jānorāda pilns ceļš uz failu (!!!)
# os.rmdir("test")

# import shutil
# shutil.rmtree(f"{pasreizeja_mape}\\test")

# Uzdevums: Izveidojat mapē "mape" failus ar nosaukumiem no 0 līdz 100
import os

if not os.path.isdir("mape"):
    os.mkdir("mape")

for i in range(0, 101):
    with open(f"mape\\{i}", "w") as f:
        pass

for file in os.listdir("mape"):
    os.remove(f"mape\\{file}")

# Uzdevums: Izmainīt šo (^) programmu lai kādā no izveidotajiem failiem (nejauši izvēlēts)
# ierakstītu vērtību uz labu laimi. Pēc tam prasīt lietotājam ievadīt
# šo vērtību un izvadīt, vai ievade bija pareiza, vai nepareiza.