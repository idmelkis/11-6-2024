class BankasKonts:
    nauda = 0.0
    def __init__(self):
        self.nauda = 0.0
    def ieskaitit(self, summa):
        self.nauda += summa
    def iznemt(self, summa):
        if self.nauda - summa >= 50.0:
            self.nauda -= summa
        else:
            print("Nepietiek līdzekļi!")
    def __str__(self):
        return f"Kontā ir {self.nauda}EUR"
class Krajkonts(BankasKonts):
    def iznemt(self, summa):
        iznemta_summa = summa * 1.05
        super().iznemt(iznemta_summa)
konts1 = BankasKonts()
konts1.ieskaitit(100)
konts1.iznemt(60)
print(konts1)
konts2 = Krajkonts()
konts2.ieskaitit(100)
konts2.iznemt(90)
print(konts2)

# 1. uzd
class Prece:
    nosaukums :str = ""
    cena :float = 0.0
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena
class Grozs:
    preces :'list[Prece]'
    def __init__(self):
        self.preces = []
    def pievienot(self, prece :Prece):
        self.preces.append(prece)
    def iznemt(self, preces_nosaukums :str):
        for preces_idx in range(0, len(self.preces)):
            if self.preces[preces_idx].nosaukums == preces_nosaukums:
                self.preces.pop(preces_idx)
                break
    def aprekinat_vertibu(self):
        vertiba = 0.0
        for prece in self.preces:
            vertiba += prece.cena
        return vertiba
    
piens = Prece("piens", 1.5)
maize = Prece("maize", 0.75)
grozs = Grozs()
grozs.pievienot(piens)
grozs.pievienot(maize)
print(grozs.aprekinat_vertibu())
grozs.iznemt("piens")
print(grozs.aprekinat_vertibu())

# 2. uzd
class Darbinieks:
    def __init__(self, id, vards, alga, amats, stazs):
        self.id = id
        self.vards = vards
        self.alga = alga
        self.amats = amats
        self.stazs = stazs
    def __str__(self):
        return f"[{self.id}] Darbinieks {self.vards} - {self.amats}, pelna {self.alga}EUR/mēn."
    def izmaksata_alga(self):
        return self.alga * self.stazs

janis = Darbinieks("01", "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks("02", "Ēriks", 2000, "Tirgotājs",	30)
anna = Darbinieks("03", "Anna",  500,  "Laborante",	2)
karlis = Darbinieks("04", "Kārlis", 9001, "Direktors", 36)

print(janis)
print(janis.izmaksata_alga())