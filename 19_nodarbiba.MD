# Lasāmviela
* Foreign keys: https://www.sqlite.org/foreignkeys.html (4.3. sekcija)
* Indeksi: https://www.sqlitetutorial.net/sqlite-index/
* Transactions: https://www.sqlite.org/lang_transaction.html

# Vaicājumi

Lai atrastu dokumentāciju, meklēja Google "Vaicājuma_tips" + SQLite, piemēram "INSERT SQlite".

* Tabulas Izveide: CREATE TABLE
* Datu ievietošana tabulā: INSERT
* Atjaunināšana: UPDATE
* Dzēšana: DELETE
* Tabulas dzēšana: DROP TABLE
* Datu iegūšana: SELECT

Komentāri:
```sql
-- Vienas rindas komentārs
/*
Vairāku rindu
komentārs
*/
```

Tabulas izveide:
```sql
CREATE TABLE "T2" (
	"T2_ID"	INTEGER NOT NULL UNIQUE,
	"Lauks1"	TEXT,
	"Lauks2"	INTEGER,
	PRIMARY KEY("T2_ID" AUTOINCREMENT)
);
```

Tabulas izveide ar foreign key:
```sql
CREATE TABLE "T2" (
	"T2_ID"	INTEGER NOT NULL UNIQUE,
	"Lauks1"	TEXT DEFAULT 'Std vērtība',
	"Lauks2"	INTEGER,
	"T1_ID"	INTEGER,
	PRIMARY KEY("T2_ID" AUTOINCREMENT),
	CONSTRAINT "Nosaukums" FOREIGN KEY("T1_ID") REFERENCES "T1"("T1_ID") ON DELETE RESTRICT
);
```

Datu ievietošana tabulā:
```sql
INSERT INTO "T1" ( "Lauks1" ) VALUES ( "Vērtība1" ); -- Viena vērtība/kol
INSERT INTO "T1" ( "Lauks2", "Lauks1" ) VALUES ( "Vērtība1", "Vērtība2" ), ( "Vērtība1", "Vērtība2" ); -- Vairākas vērtības & vairākas kol.
```

Datu atjaunināšana
```sql
-- Loģiskie salīdzinājumi zem WHERE == != > < <= >=
UPDATE "T1" SET "Lauks1" = "Jaunā vērtība 1!" WHERE "T1_ID" == 5; -- Vienas kolonas atjaunināšana
UPDATE "T1" SET ("Lauks1", "Lauks2") = ("Jaunā vērtība 1!", "Jaunā vērtība 2!") WHERE "T1_ID" == 5; -- Vairāku kolonu atjaunināšana
```

Nākošajā nodarbībā - SELECT, GROUP BY utt.