# saraksts = []
# kortezs = () (set)

# Atslēgu <=> Vērtību
vardnica = {
    "atslega": "vertiba",
    1: "",
}
print(vardnica["atslega"])
print(vardnica[1])

atslēga = "vecums"
vērtība = 18
cilveks = {
    "Vārds": "...",
    "Uzvārds": "...",
    atslēga: vērtība
}
#print(vardnica[atslēga])

# Uzdevums: Izmantot vārdnīcas lai pārveidotu tekstā burtus 
# āēīū formā bez garumzīmes, t.i. aeiu
burti = {
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ū": "u",
}
def changeLetter(text):
    result = ""
    for letter in text:
        if letter in burti:
            result += burti[letter]
        else:
            result += letter
    return result
print(changeLetter("Vējš"))
print(changeLetter("Mašīna"))
print(changeLetter("Skolēns"))

print(burti.keys())
print(burti.values())
print(burti.items())
for j,k in burti.items():
    print(f"Atslēga: {j}, Vērtība: {k}")

burti["ō"] = "o"
burti.update({"ž": "z", "ķ": "k"})
print(burti)

# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas 
# ir ar ciklu atslēgās ievietoti skaitļi no 1 līdz n 
# (lietotāja ievadīts skaitlis) un vērtības ir šis skaitlis kvadrātā.
ievade = int(input("Skaitlis: "))
saraksts = {}
for iii in range(1, ievade+1):
    saraksts[iii] = iii * iii
    #saraksts.update({iii: iii*iii})
print(saraksts)

# Uzdevums: Pacelt vērtības iekš vārdnīcas kvadrātā
# Hint: Vajadzēs izmantot vienu no šīm funkcijām
# print(burti.keys())
# print(burti.values())
# print(burti.items())
vardnica = {
    1: 1,
    "a": 2,
    3: 3
}
# Piem. 
# vardnica = {
#     1: 1,
#     "a": 4,
#     3: 9
# }
# 
for j,k in vardnica.items():
    vardnica[j] = vardnica[j] * vardnica[j]
print(vardnica)

# Uzdevums:
# Ar vienu vai vairākiem cikliem apvienot vārdnīcas 
# iekš mainīgā dict3
dict1 = {
    1: 10,
    2: 20,
    3: 30
}
dict2 = {
    4: 40,
    5: 50,
    6: 60
}
dict3 = { 
    # ...
}
for j,k in dict1.items():
    dict3[j] = k
for j,k in dict2.items():
    dict3[j] = k
print(dict3)
#VAI
# for i in (dict1, dict2):
#     dict3.update(i)