# Dokumentācija: https://docs.python.org/3/library/sqlite3.html
# SQL Injekcijas piemēri: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
import sqlite3

# Glabājam datu bāzi operatīvajā atmiņā
# db = sqlite3.connect(":memory:")

#db = sqlite3.connect("23_nodarbiba.db")
#cur = db.cursor()
#cur.close()
#db.commit()
#db.close()

#db = sqlite3.connect("23_nodarbiba.db")
#cur = db.cursor()

#cur.execute(query) # Palaiž vaicājumu

#Identifikators = input("Ievade: ") 
#query = "SELECT * FROM Tabula WHERE Id == ?"
#rezultati = cur.execute(query, (Identifikators, ))

# Alternatīva
#query = f"SELECT * From Tabula WHERE Lauks LIKE ':nosaukums'"
#rezultati = cur.execute(query, ({"nosaukums": Identifikators}))
# Ievade
#vertiba = input("Ievade: ")
#vertiba2 = input("Ievade 2: ")
#query = f"INSERT INTO Tabula (Lauks) VALUES (?)"
#cur.execute(query, (vertiba,)) # Komats pēc str vērtības - lai izveidotu tuple
# Ļauj palaist vienu vaicājumu vairākas reizes ar dažādiem parametriem
#cur.executemany(query, ((vertiba,), (vertiba2,)))

#query = "SELECT * FROM Tabula"
#cur.execute(query)
#rezultati = cur.fetchall() # Iegūst vaicājuma rezultātu, atgriež Tuple
# cur.fetchmany(4) # Atgriež noteiktu skaitu rezultātu
# cur.fetchone() # Atgriež vienu vērtību
#for rezultats in rezultati:
#    print(rezultats)

#cur.close()
#db.commit()
#db.close()

#  ==============================
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

lietotajs = Lietotajs(1, "lietotajs2", "******", "pasts@pasts.com")

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

# Ievietojam datus
query = "INSERT INTO Lietotajs (Lietotajvards, Parole, Epasts) VALUES (?,?,?)"
cur.execute(query, lietotajs.uz_ievietosanas_vaicajumu())

# Iegūstam datus
query = "SELECT * FROM Lietotajs"
cur.execute(query)
for row in cur.fetchall():
    iegutais_lietotajs = Lietotajs(row[0], row[1], row[2], row[3])
    iegutais_lietotajs = Lietotajs.no_vaicajuma(row)
    print(iegutais_lietotajs)


#query = "Update Lietotajs Set 'Lietotajvards' = 'Vertiba' WHERE Id == 1"
# ...

# Dzēšam datus
#query = "DELETE FROM Lietotajs WHERE ID == 1"
#cur.execute(query)

# Dzēst tabulu
query = "DROP TABLE Lietotajs"
cur.execute(query)

cur.close()
db.commit()
db.close()