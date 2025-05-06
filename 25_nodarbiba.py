# Chinook db fails: https://s.ayy.lv/chinook

import sqlite3
con = sqlite3.connect("chinook.sqlite")
cur = con.cursor()

# 1. Uzdevums
# Iegūt no tabulas "Employee" visus cilvēku vārdus, uzvārdus un e-pastus.
# cur.execute("SELECT FirstName, LastName, Email FROM Employee")
# print(cur.fetchall())

# 2. Uzdevums
# Iegūt māksliniekus/grupas no tabulas "Artist" kuriem nosaukumā (kolona "Name") ir vārds "Black".
# cur.execute("SELECT Name FROM Artist WHERE \"Name\" LIKE \"%Black%\"")
# print(cur.fetchall())

# 3. Uzdevums
# Iegūt pirmos 3 ierakstus no tabulas "InvoiceLine" kur kolonas "InvoiceId" vērtība ir 3
# 1. Variants
# cur.execute("SELECT * FROM InvoiceLine WHERE InvoiceId == 3 LIMIT 3")
# print(cur.fetchall())
# 2. Variants
# cur.execute("SELECT * FROM InvoiceLine WHERE InvoiceId == 3")
# print(cur.fetchmany(3))

# 4. Uzdevums 
# Izvadīt dziesmas nosaukumu no tabulas "Track" un tā žanru (tabula "Genre" ir saistīta ar Track.GenreId)
# cur.execute("SELECT Track.Name, Genre.Name FROM Track INNER JOIN Genre ON Track.GenreId == Genre.GenreId")
# print(cur.fetchall())

# 5. Uzdevums
# Izvadat no tabulas "Customer" informāciju pa to cik klienti ir katram atbalsta personālam (Id tiek glabāts kolonā "SupportRepId", Personāla informācija ir tabulā "Employee"). Izvade - Darbinieka vārds, klientu skaits.
# Izvadīt formātā
# Vārds: <Employee.FirstName>
# Skaits: <COUNT>
# cur.execute("SELECT Employee.FirstName, COUNT(*) FROM Customer INNER JOIN Employee ON Customer.SupportRepId == Employee.EmployeeId GROUP BY Customer.SupportRepId")
# result = cur.fetchall()
# for value in result:
#     print(f"Vārds: {value[0]}\nSkaits: {value[1]}")

# 6. Uzdevums
# Dots apraksts: "Preci apraksta unikāls identifikators, tās nosaukums, tā cena, un svars."
# Izveidojat:

# * Klases kas atbilst šim aprakstam.
# * Izveidot tabulas šīm klasēm.

class Prece:
    def __init__(self, id, nosaukums, cena, svars):
        self.id = id
        self.nosaukums = nosaukums
        self.cena = cena
        self.svars = svars
cur.execute("CREATE TABLE IF NOT EXISTS \"Prece\" (\
	\"Id\"	INTEGER NOT NULL UNIQUE,\
	\"Nosaukums\"	TEXT,\
	\"Cena\"	REAL,\
	\"Svars\"	REAL,\
	PRIMARY KEY(\"Id\" AUTOINCREMENT)\
);")

cur.close()
con.commit()
con.close()