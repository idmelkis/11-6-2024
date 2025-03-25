# Lasāmviela

* Agregātfunkcija - https://www.sqlite.org/lang_aggfunc.html 
* Wildcard simbols - https://en.wikipedia.org/wiki/Wildcard_character
* Attiecību tipi - https://www.geeksforgeeks.org/relationships-in-sql-one-to-one-one-to-many-many-to-many/

# Vaicājumi

DELETE - Datu dzēšana
```sql
DELETE FROM "T1" WHERE "T1_ID" == 6;
```

DROP TABLE - Tabulu dzēšana
```sql
DROP TABLE "T3";
```

SELECT - Datu iegūšana
```sql
-- "*" = visas kolonas (wildcard simbols)
SELECT * FROM "T1";
-- Salīdzinājumi - > < != == AND, OR, LIKE, NOT
SELECT * FROM "T1" WHERE "T1_ID" > 5 OR "T1_ID" < 3; 
SELECT * FROM "T1" WHERE "Lauks1" LIKE "vērtība%"; -- Vai sākas ar vārdu "vērtība"
SELECT * FROM "T1" WHERE "Lauks1" LIKE "%vērtība"; -- Vai beidzas ar vārdu "vērtība";
SELECT DISTINCT "Lauks1" FROM "T1"; -- Unikālas vērtības kolonā "Lauks1"
SELECT "Lauks1" FROM "T1" LIMIT 3; -- Pirmās trīs vērtības
-- Sakārtošanas secības - ASC - augoša, DESC - dilstoša
SELECT "T1_ID", "Lauks1" FROM "T1" ORDER BY "Lauks1" DESC; -- Sakārto pēc kolonas "Lauks" dilstoši
SELECT "Lauks1", "T1_ID" FROM "T1"; -- SELECT Kolonas izvada tādā secībā, kā ievadat. Dati tiks sakārtoti pēc primārās atslēgas - ja eksistē.
SELECT "Lauks1", count("Lauks1") FROM "T1" GROUP BY "Lauks1"; -- Izskaita duplikātās vērtības 
```

# Uzdevumi

Uzdevums: uzrakstīt SQL vaicājumus, lai 
* izveidotu sekojošo klasi kā tabulu, 
* un uzrakstīt vaicājumus lai ievietotu tabulā apakšā esošos datus.

```py
class Darbinieks:
    id :int
    vards :str
    alga :float
    amats :str
    nostradats :int

janis = Darbinieks(1, "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks(2, "Ēriks", 2000, "Tirgotājs", 30)
anna = Darbinieks(3, "Anna",  500,  "Laborante", 2)
karlis = Darbinieks(4, "Kārlis", 9001, "Direktors", 36)
```

Risinājums:

```sql
CREATE TABLE IF NOT EXISTS "Darbinieks" (
    Id INTEGER NOT NULL UNIQUE,
    Vards TEXT,
    Alga REAL,
    Amats TEXT,
    Nostradats INTEGER,
    PRIMARY KEY ("ID" AUTOINCREMENT)
);
INSERT INTO "Darbinieks" ("Vards", "Alga", "Amats", "Nostradats") VALUES ("Jānis", 1000, "Slotas operators", 24), ("Ēriks", 2000, "Tirgotājs", 30),
("Anna", 500, "Laborante", 2), ("Kārlis", 9001, "Direktors", 36);
```

Uzdevums (turpinājums): 
* Izveidot tabulu projekts, kurš satur informāciju par projekta nosaukumu un identifikatoru.
* Realizēt darbinieku saistību ar vairākiem projektiem (many-to-many attiecība).

```sql
CREATE TABLE IF NOT EXISTS "Projekts" (
    Id INTEGER NOT NULL UNIQUE,
    Nosaukums TEXT,
    PRIMARY KEY ("ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "DarbiniekaProjekts" (
    DarbinieksId INTEGER NOT NULL UNIQUE,
    ProjektsId INTEGER NOT NULL UNIQUE,
    CONSTRAINT "Darbinieks" FOREIGN KEY("DarbinieksId") REFERENCES "Darbinieks"("Id"),
    CONSTRAINT "Projekts" FOREIGN KEY("ProjektsId") REFERENCES "Projekts"("Id")
);
```

Nākošajā stundā - Risinājums uzdevumam, Joins, Unions, Praktiskie uzdevumi 