#class VardsViens:
    # def vardsViens:
    # def vards_divi:

# Klase -- skice/abstrakcija, kā izvietot un strādāt ar datiem
class Automasina:
    krasa :str = ""
    marka :str = ""

    atrums :float = 0.0
    virziens_x :float = 0.0
    virziens_0 :float = 0.0

    def __init__(self, krasa, marka) -> 'Automasina':
        self.krasa = krasa
        self.marka = marka
        print(f"Izveidota klase - {self.krasa} {self.marka}")
        #print("Izveidota klase - " + self.krasa + " " + self.marka)
    def __str__(self) -> str:
        return f"Klase Automasina, satur datus par {self.krasa} {self.marka}"

    @classmethod
    def otrs_init(cls):
        return cls("!", "!!")
    
    # getters/setters
    # encapsulation
    def getAtrums(self):
        return self.atrums
    def setAtrums(self, atrums):
        self.atrums = atrums
    
    def paatrinat(self):
        self.atrums += 0.5
    def paleninat(self):
        if self.atrums > 0:
            self.atrums -= 0.5
  

# objekts = Automasina("Zals", "BMW")
# kaut_kas = Automasina("Peleks", "Audi")
# #objekts.atrums
# obj3 = Automasina.otrs_init()

# print(objekts)
# print(kaut_kas)
# print(obj3)
# print(objekts.__dict__)

# nobraukts = 0.0
# masina = Automasina("Zals", "BMW")
# while True:
#     # Input bloķē - ideālā situācijā izmantotu nebloķējošu ievadi
#     i = input()
#     if i == "w":
#         masina.paatrinat()
#     elif i == "s":
#         masina.paleninat()
    
#     nobraukts += masina.getAtrums()
#     print(f"Nobraukts: {nobraukts}, pašreizējais ātrums: {masina.getAtrums()}")    

# Uzdevums: 
# Izveidot klasi, kas aprakstītu priekšmetu e-klasē
# Vismaz 4 mainīgie, un 2 funkcijas kas strādā ar šiem datiem.
# Izveidojat objektu, un uzrakstat kodu, kas pielieto šīs funkcijas.
class Skolens:
    vards = ""
    def __init__(self, vards, uzvards):
        self.vards = vards + " " + uzvards
class Nodarbiba:
    datums :str = ""
    tema :str = ""
    def __init__(self, datums, tema):
        self.datums = datums
        self.tema = tema
class Prieksmets:
    nosaukums: str = ""
    skolotajs: str = ""
    skoleni: 'list[Skolens]' = []
    nodarbibas: 'list[Nodarbiba]' = []

    def __init__(self, nosaukums, skolotajs):
        self.nosaukums = nosaukums
        self.skolotajs = skolotajs

    def izveidotNodarbibu(self, datums, tema):
        self.nodarbibas.append(Nodarbiba(datums, tema))
    def pievienotSkolenu(self, skolens: Skolens):
        self.skoleni.append(skolens)

    def __str__(self):
        return f"Priekšmets {self.nosaukums} ar {len(self.skoleni)} skolēniem."

programmesana = Prieksmets("Programmesana I", "Ingmārs")
programmesana.pievienotSkolenu(Skolens("Jānis", "Bērziņš"))
print(programmesana)

# Uzdevums 2: 
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.