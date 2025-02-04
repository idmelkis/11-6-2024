# Iepriekšējās stundas uzd
class Darbinieks:
    def __init__(self, vards, uzvards, alga, amats, stazs):
        self.vards = vards
        self.uzvards = uzvards
        self.alga = alga
        self.amats = amats
        self.stazs = stazs
    def aprekiniBonusu(self):
            return 0
    def aprekiniKopalgu(self):
            return self.alga * self.stazs + self.aprekiniBonusu()
    def __str__(self):
        return f"{self.vards} {self.uzvards} -- {self.amats} ({self.aprekiniKopalgu()})"
class Menedzeris(Darbinieks):
    def __init__(self, vards, uzvards, alga, amats, stazs, padotie):
        self.padotie = padotie
        super().__init__(vards, uzvards, alga, amats, stazs)
    def aprekiniBonusu(self):
         return self.padotie * 100;
class Programmetajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, amats, stazs, projekts):
        self.projekts = projekts
        super().__init__(vards, uzvards, alga, amats, stazs)
    def aprekiniBonusu(self):
        return self.alga * 0.10
class Testetajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, amats, stazs, projekts, nostradataisStSkaits):
        self.projekts = projekts
        self.nostradataisStSkaits = nostradataisStSkaits
        super().__init__(vards, uzvards, alga, amats, stazs)
    def aprekiniBonusu(self):
        return self.alga * 0.05  
    def aprekiniKopalgu(self):
        return self.nostradataisStSkaits * 7 + self.aprekiniBonusu()

janis = Menedzeris("Jānis", "Uzvārds", 10, "Menedžeris", 10, 10)
pēteris = Programmetajs("Pēteris", "Uzvārds", 10, "Menedžeris", 10, "Proj1")
gunita = Testetajs("Gunita", "Uzvārds", 1, "Testētājs", 0, "Proj1", 10)
print(janis)
print(pēteris)
print(gunita)

# 1. Uzdevums
class Galdins:
    numurs :int
    aiznemts :bool
    pirkumi :'list[str]'
    def __init__(self, numurs :bool):
        self.numurs = numurs
        self.aiznemts = False
        self.pirkumi = []
    def aiznemt_galdinu(self):
        self.aiznemts = True
    def pievienot_pirkumu(self, pirkums):
        self.pirkumi.append(pirkums)
class Restorans:
    edieni :'dict[str, float]'
    galdini :'list[Galdins]'
    def __init__(self):
         self.edieni = {}
         self.galdini = []
    def pievienot_edienu(self, ediens :'dict[str, float]'):
        self.edieni.update(ediens)
    def izvada_edienkarti(self):
        print("Ēdienkarte: ")
        for key, value in self.edieni:
             print(f" -- {key}: {value}")
        print("************")
    def pievienot_galdinu(self, galdins :Galdins):
        self.galdini.append(galdins)
    def rezervet_galdinu(self, numurs):
        for galdins in self.galdini:
            if galdins.numurs == numurs:
                galdins.aiznemt_galdinu()
                break
    def registret_pirkumu(self, numurs, ediens):
        for galdins in self.galdini:
            if galdins.numurs == numurs:
                if galdins.aiznemts:
                    galdins.pievienot_pirkumu(ediens)
                else:
                    print("Galdiņš nav aizņemts!")

# 2. Uzdevums
import json
import os

class Cilveks:
    vards :str
    uzvards :str
    vecums :int
    def __init__(self, vards, uzvards, vecums):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
cilveki = []

if os.path.isfile("cilveki.json"): # True ja fails eksistē, false, ja neeksistē
    with open("cilveki.json", "r", encoding="UTF-8") as f:
        vertibas = json.load(f)
        for vertiba in vertibas:
            cilveks = Cilveks(vertiba["vards"], vertiba["uzvards"], int(vertiba["vecums"]))
            cilveki.append(cilveks)

while True:
    cilveks = Cilveks(input("Ievadi vārdu: "), input("Ievadi uzvārdu: "), int(input("Ievadi vecumu: ")))
    cilveki.append(cilveks)

    turp = input("Vēlies ievadīt vēlvienu cilvēku?")
    if turp=="nē":
        break

with open("cilveki.json", "w", encoding="UTF-8") as f:
    # TODO: Izvadīt sarakstu failā :)