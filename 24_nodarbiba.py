# Pārkopēt Lietotāja klasi
# Iepriekšējās stundas kods: http://s.ayy.lv/11-4-23
# Lasāmviela: jaucējfunkcijas: https://en.wikipedia.org/wiki/Hash_function

import sqlite3
class Lietotajs:
    def __init__(self, id, lietotajvards, parole, epasts):
        self.id = id
        self.lietotajvards = lietotajvards
        self.parole = parole
        self.epasts = epasts

    def uz_ievietosanas_vaicajumu(self):
        return (self.lietotajvards, self.parole, self.epasts)
    
    @classmethod
    def no_vaicajuma(cls, *args):
        args = args[0]
        return cls(args[0], args[1], args[2], args[3])

    
    def __str__(self):
        return f"<{self.id}> {self.lietotajvards} - {self.epasts}"
    
db = sqlite3.connect("23_nodarbiba.db")
cur = db.cursor()
query = 'CREATE TABLE IF NOT EXISTS "Lietotajs" (\
	"Id"	INTEGER NOT NULL UNIQUE,\
	"Lietotajvards"	TEXT NOT NULL UNIQUE,\
	"Parole"	TEXT NOT NULL,\
	"Epasts"	TEXT,\
	PRIMARY KEY("Id" AUTOINCREMENT)\
);'
cur.execute(query)

def izveidot_lietotaju(cur :sqlite3.Cursor) -> Lietotajs:
    lietotajvards = input("Lietotajvards: ")
    parole = input("Parole: ") # TODO: Paroles jaukšana
    epasts = input("Epasts: ")
    
    # TODO: Kļūdas pārbaude - lietotājs jau eksistē, vai nevar ievietot
    query = "INSERT INTO Lietotajs (lietotajvards,parole,epasts) VALUES (?,?,?)"
    cur.execute(query, (lietotajvards, parole, epasts))

    # TODO: Kļūdas pārbaude - vai tas neatbilst ievietotajam
    query = "SELECT * FROM Lietotajs ORDER BY Id DESC LIMIT 1"
    cur.execute(query)
    result = cur.fetchall()
    if len(result) > 0:
        lietotajs = Lietotajs.no_vaicajuma(result[0])
    return lietotajs

# Uzdevums (i/ni):
# Pievienot profila funkcionalitāti.
# 1. Izveidot jaunu tabulu (Profils) - 
# Lauki - Id, LietotajaId, Vards, Uzvards, ParMani
# LietotajaId vajadzētu būt saistīts ar Lietotajs.Id (ON DELETE CASCADE)

# Ja lietotājs programmā ir autentificējies, tad
# Lietotājam vajadzētu varēt izvadīt savu profilu (ja tāds ir).
# Lietotājam vajadzētu varēt izveidot vai izmainīt (ja tāds ir) savu profilu.

def autentificet_lietotaju(cur :sqlite3.Cursor) -> Lietotajs:
    lietotajvards = input("Lietotajvards: ")
    parole = input("Parole: ") # TODO: Paroles jaukšana
    query = "SELECT * FROM Lietotajs WHERE Lietotajvards = ? AND Parole = ?"
    cur.execute(query, (lietotajvards, parole))
    result = cur.fetchall()
    if len(result) > 0:
        return Lietotajs.no_vaicajuma(result[0])
    else:
        return None

lietotajs = None
while True:
    print("Izvēlne: ")
    print("-- 1. Izveidot lietotāju")
    print("-- 2. Autentificēt lietotāju")
    print("-- 0. Iziet")
    ievade = int(input("Ievade: "))

    if ievade == 0:
        break
    elif ievade == 1:
        lietotajs = izveidot_lietotaju(cur)
        print(lietotajs)
    elif ievade == 2:
        lietotajs = autentificet_lietotaju(cur)
        if lietotajs == None:
            print("Lietotājvārds vai parole neeksistē!")
        else:
            print(lietotajs)


cur.close()
db.commit()
db.close()