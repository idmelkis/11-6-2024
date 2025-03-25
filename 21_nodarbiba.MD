# Lasāmviela

* JOIN tipi - https://www.sqlite.org/syntax/join-operator.html

![](https://miro.medium.com/v2/resize:fit:720/0*Nrjozs1i0XIiACKd.png)

# Vaicājumi
UNION - Apvieno rezultātus no diviem vaicājumiem.  
! Vaicājumu rezultātam vajag būt vienādam kolonu skaitam.
```sql
SELECT "Id", "Vards" FROM "Darbinieks"
UNION
SELECT * FROM "Projekts";
```

JOIN - Apvieno rezultātus no divām tabulām.
```sql
SELECT * FROM "Darbinieks" A INNER JOIN "Projekts" B ON A."Id" == B."Id"; -- Izvada rindas, kur tabulā A un B ir vienādi Id.
SELECT * FROM "Darbinieks" A LEFT JOIN "Projekts" B ON A."Id" == B."Id"; -- Izvada visas rindas no tabulas A, un, ja ir atbilstošas vērtības tabulā B, tās arī tiek izvadītas. Ja nav - tabulas B kolonu vērtības ir NULL.
SELECT * FROM "Darbinieks" A RIGHT JOIN "Projekts" B ON A."Id" == B."Id"; -- Izvada visas rindas no tabulas B, un, ja ir atbilstošas vērtības tabulā A, tās arī tiek izvadītas. Ja nav - tabulas A kolonu vērtības ir NULL.
SELECT * FROM "Darbinieks" A FULL JOIN "Projekts" B ON A."Id" == B."Id"; -- Izvada visas rindas no tabulas A, un B. Ja ir vienādi identifikatori, vērtības abām tabulām tiek izvadītas vienā rindā, ja nav - tiek izvadīts ieraksts no tabulas, un otras tabulas kolonās ir NULL.
SELECT * FROM "Darbinieks" A CROSS JOIN "Projekts" B; -- Tiek izvadīti visi ieraksti no tabulas A vairākas reizes - katram tabulas A ierakstam blakus tiek pievienots ieraksts no tabulas B, piem ja tabulā A ir 1 ieraksts un tabulā B ir 3 ieraksti, tad rezultātā būs 3 rindas - 1A-1B, 1A-2B, 1A-3B.

-- Ar joiniem var izmantot visus tos pašus filtrus kurus ar citiem vaicājumiem, piem.
SELECT A.Vards as "Darbinieka Vārds", B.Nosaukums
FROM "Darbinieks" A
INNER JOIN "Projekts" B
ON A."Id" == B."Id"
WHERE A.Id == 1;
```

# Uzdevumi

* Piemēra datu bāze "Chinook": https://s.ayy.lv/chinook (lejupielādējat to - "View Raw")

1. Uzdevums - Uzrakstīt vaicājumu, kas izvada Albumus (`Album`) ar to autoriem (`Artist`).
```sql
SELECT Album.Title, Artist.Name
FROM Album
INNER JOIN Artist
ON Album.ArtistId == Artist.ArtistId;
```

2. Izveidot kopiju tabulai Genre, pārkopēt datus no oriģinālās tabulas. Hint - Pie INSERT VALUES var izmantot SELECT vaicājumus.

```sql
CREATE TABLE IF NOT EXISTS "Genre_2" (
	"GenreId"	INTEGER NOT NULL,
	"Name"	NVARCHAR(120),
	CONSTRAINT "PK_Genre" PRIMARY KEY("GenreId")
);

INSERT INTO "Genre_2" SELECT * FROM "Genre";
```

Nākošajā stundā:

3. Uzrakstat vaicājumu, kas izvada visus rēķinus (`Invoice`) kuru identifikators ir lielāks par 400, un kuru vērtība (kolona `Total`) ir lielāka par 5.00.