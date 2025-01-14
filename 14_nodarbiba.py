# Uzdevums 2: 
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.
class Spuldze:
    elektrības_patēriņs :float = 0.0
    krāsa :str = ""
    ieslēgts :bool = False
class Lampa:
    spuldze: Spuldze = None
    krāsa :str = ""
    ieslēgts :bool = False

# Polimorfisms
from enum import Enum
class Krāsa(Enum):
    SARKANA = 1,
    ZAĻA = 2

class Transportlīdzeklis:
    krasa :Krāsa = ""
    marka :str = ""

    atrums :float = 0.0

    def __init__(self):
        print("???")

    def paatrinat(self):
        self.atrums += 0
    def paleninat(self):
        if self.atrums > 0:
            self.atrums -= 0

class Automašīna(Transportlīdzeklis):
    def __init__(self):
        print("!!!")
        super().__init__()
    
    def paatrinat(self):
        self.atrums += 0.5
    def paleninat(self):
        if self.atrums > 0:
            self.atrums -= 0.5

class Lidmašīna(Transportlīdzeklis):
    spārnu_skaits = 4

    def paatrinat(self):
        self.atrums += 4
    def paleninat(self):
        if self.atrums > 0:
            self.atrums -= 4


kaut_kas = Transportlīdzeklis()
masina1 = Automašīna()
masina1.krasa = Krāsa.SARKANA
print(masina1.krasa)
print(masina1.krasa.value)
print(masina1.krasa.name)
masina1.paatrinat()
# Interface pattern
print(masina1.atrums)
lidmasina = Lidmašīna()
lidmasina.paatrinat()
print(lidmasina.atrums)

# Uzdevums: Izveidojiet bāzes klasi, un mantojošo klasi. 
# Tēma: Pēc brīvas izvēles.
# Bāzes klasei divus mainīgos, vienu funkciju (var būt primitīva funkc. ar print())
# Mantojošā klase - vismaz viens unikāls mainīgais, pārrakstām kādu funkciju

# Uzdevums i/ni: Izveidot programmu
# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt un/vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50
# Izveidojat apakšklasi "Krājkonts" (manto no "Bankas konts").
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju,
#   lai tā kopā ar izņemto naudu izņem vēl 5%
#   (t.i. izņemot €100, izņems €105).
# Izveidojat objektus no šīm klasēm
# 
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100),
#   izsaucat izņemšanas funkciju €60.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €90
# Izvadat abu kontu atlikumus