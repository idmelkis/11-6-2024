vardnica = {
    "1": 1,
    "2": 2,
    "3": 3,
}

vardnica["4"] = ""
vardnica.update({"5": 5})

del vardnica["1"]
rez = vardnica.pop("2")
print(vardnica)
print(rez)

# Uzdevums: (Dots) Tiek ģenerēts saraksts ar 20 vērtībām
# Ar ciklu izdzēst katru otro vērtību
# Vārdnīcas garums ja vajag: len(vardnica)
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 10)
print(vardnica)

for iii in range(0, 20, 2):
    del vardnica[iii]
print(vardnica)

# Šādi nestrādās: NEDRĪKST (!) mainīt elementus 
# iekš for cikla ejot pāri vārdnīcai
# for iii in vardnica:
#     if iii % 2 == 0:
#         del vardnica[iii]

# Uzdevums
# Izveidot vārdnīcu no sarakstiem keys un values, kur keys ir atslēgas, 
# un values ir vērtības
# Ir garantēts, ka keys un values sarakstu garumi ir vienādi.
import random
keys = [ 1, 2, "10", 3, random.randint(0, 100) ]
values = [ "viens", 4, False, [1,3,4], random.randint(0, 100) ]

rezultats = {}
for iii in range(0, len(keys)):
    rezultats[keys[iii]] = values[iii]

# Alternatīva:
#dict(zip(keys, values))

# (i/ni)
#Uzdevums: Uzrakstat programmu, kurā lietotājs ievada vairāku cilvēku datus
#(vārds; uzvārds, vecums). Indiv. cilvēka dati jāsaglabā vārdnīcā. Visu
#cilvēku datus varat apvienot datu struktūrā pēc jūsu izvēles.
#Izvadat visu ievadīto cilvēku informāciju.