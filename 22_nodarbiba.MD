# Lasāmviela

1. Datumi https://www.sqlite.org/lang_datefunc.html

# Uzdevumi

* Piemēra datu bāze "Chinook": https://s.ayy.lv/chinook (lejupielādējat to - "View Raw")

1. Uzrakstat vaicājumu, kas izvada visus rēķinus (`Invoice`) kuru identifikators ir lielāks par 400, un kuru vērtība (kolona `Total`) ir lielāka par 5.00.
```sql
SELECT * FROM "Invoice" WHERE InvoiceId > 400 AND Total > 5.00;
```

2. Uzrakstat vaicājumu, kas izvada visus rēķinus (Tabula `Invoice`) no 2009. gada līdz 2011. gadam (kolona `InvoiceDate`).
```sql
-- Datumu funkcija: datetime('2025-01-01 00:00:00');

-- Pārbaudīt vērtības diapazonā:
-- WHERE <expression> AND <expression>
-- WHERE <value> BETWEEN <val1> AND <val2>
SELECT * FROM Invoice WHERE InvoiceDate BETWEEN datetime('2009-01-01 00:00:00') AND datetime('2011-01-01 00:00:00')
```
2.1. Izmainat iepriekšējo vaicājumu, lai izvadītu šajā laika posmā izrakstīto rēķinu skaitu
```sql
SELECT count(*) FROM Invoice WHERE InvoiceDate BETWEEN datetime('2009-01-01 00:00:00') AND datetime('2011-01-01 00:00:00')
```

3. Uzrakstat vaicājumu, kas izvada cik katrā atskaņošanas sarakstā ir dziesmas (tabula `PlaylistTrack`). Pietiek, ka parāda playlist identifikatoru un dziesmu skaitu (pagaidām nav jātaisa join lai izvadītu nosaukumu).
```sql
SELECT PlaylistId, count(TrackId) FROM PlaylistTrack GROUP BY PlaylistId
```

3.1. Papildinat iepriekšējo vaicājumu, lai identifikatora vietā tiktu izvadīts playlist nosaukums (Tabula `Playlist`).
```sql
SELECT b.name, count(a.TrackId) FROM PlaylistTrack a
INNER JOIN Playlist b ON a.PlaylistId == b.PlaylistId
GROUP BY a.PlaylistId
```

4. Uzrakstat vaicājumu, kas izvada cik rēķini (tabula `Invoice`) ir katrā valstī (Kolona `BillingCountry`). Rezultātiem vajadzētu būt sakārtotiem no lielākā uz mazāko.

```sql
SELECT BillingCountry, count(BillingCountry) FROM Invoice GROUP BY BillingCountry ORDER BY count(BillingCountry) DESC
```

# i/ni darbs
Dotas 15min. 3 Vaicājumi - jāatbilst nosacījumiem!

1. Uzrakstat vaicājumu, kas izvada visus māksliniekus (tabula `Artist`) kuru nosaukumā ir vārds "Black" (kolona `Name`)
2. Uzrakstat vaicājumu, kas izvada nosaukumu un garumu (sekundēs) visām dziesmām (tabula `Track`), kuras ir garākas par 1min (kolona - Miliseconds). Piezīme - tabulā dati ir milisekundēs, izvadē jāpārveido uz sekundēm.
3. Uzrakstīt vaicājumu, kas izvada visas dziesmu (tabula `Track`) cenu grupas (hint - tādas ir divas, kolona `UnitPrice`), un cik daudz dziesmas ir šajā grupā.

Iesniegt e-klasē pie šīs stundas. Iesniegt kā .txt vai .sql failu.