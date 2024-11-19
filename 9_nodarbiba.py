# JSON - JavaScript Object Notation
# {"Atslēga": "vērtība"}
import json
vardnica = {
    "key": "value",
    "True": True,
    23: 32,
    False: True
}
json_str = json.dumps(vardnica) # dump string
json_str = "{\"123\":true,\"312\":\"World\"}"
vardnica = json.loads(json_str)
print(vardnica)

# Lūdzu šādi nedarat
# fails = open("nosaukums.json", "w")
# print("Hello!")
# fails.close()

# with open() as <mainigais>
# import os
import os
print(os.path.dirname(__file__))

# open(faila-nosaukums, atversanas-tips, encoding)
# atversanas-tips: r,w,a
# r - read (atvērt lasīšanai)
# w - write (atvērt rakstīšanai) - pārraksta visu failu
# a - append (atvērt pievienošanai) - pievieno faila galā
# r+ - read+write
# Vairāk informācija: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#with open("nosaukums.json", "r+", encoding="UTF-8") as f:
    #f.write("1")
    #f.writelines(["Rinda", "Rinda2"])
    #faila_saturs = f.read()
    #print(faila_saturs)
    # Lasam pa rindām:
    # for line in f:
    #     print(line.strip())
    # 
    # rindas = f.readlines()
    # print(rindas)

import json
vardnica = { "Vards": "Jānis", "Uzvārds": "Liepiņš" }
# Rakstīšana
with open("nosaukums.json", "w", encoding="UTF-8") as fails:
    # Rakstīt pa tiešo failā
    #json.dump(vardnica, fails)
    
    # Pārveidot vārdnīcu par tekstu un rakstīt tekstu failā
    json_teksts = json.dumps(vardnica)
    fails.write(json_teksts)

with open("nosaukums.json", "r", encoding="UTF-8") as fails:
    #dati = json.load(fails)
    dati = json.loads(fails.read())
    print(dati)

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

# Piemērs ievadei:
cilveki = []
while True:
    vards = input("Ievadi vārdu: ")
    uzvards = input("Ievadi uzvārdu: ")
    vecums = int(input("Ievadi vecumu: "))

    cilveks ={
        "vards": vards,
        "uzvards": uzvards,
        "vecums": vecums,
    }

    cilveki.append(cilveks)

    turp = input("Vēlies ievadīt vēlvienu cilvēku?")
    if turp=="nē":
        break
# ...Saglabāšana failā