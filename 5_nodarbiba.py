# Spēle: Uzmini skaitli
# Uzdevums: Spēle "Uzmini skaitli"
# Spēle uzģenerē nejaušu skaitli izmantojot sekojošo kodu:
# import random
# skaitlis = random.randint(0, 100)
# #import math
# #math.sqrt()

# # Ciklā: Lietotājs ievada skaitli (input).
# # Programma pārbauda vai skaitlis ir uzminēts, 
# # ja nav pasaka vai ievadītais # skaitlis ir lielāks, 
# #   vai mazāks par nejaušo skaitli.
# # Visas lietotāja ievades (minējumus) jāsaglabā sarakstā
# # Kad lietotājs ir uzminējis skaitli - 
# # Izvadīt 'Uzvara'
# # Izvadīt minējumu skaitu (len(...)), lietotāja minējumus
# ievade = -1
# skaitli = []
# while True: # ievade != skaitlis:
#     ievade = int(input("Skaitlis:"))
#     skaitli.append(ievade)
#     if ievade < skaitlis:
#         print("Ievade ir mazāka")
#     elif ievade > skaitlis:
#         print("Ievade ir lielāka")
#     else:
#         print("Uzvara")
#         print(f"Spēle beidzās pēc {len(skaitli)} minējumiem. Minējumi:")
#         print(skaitli)
#         break

def nosaukums(param):
    pass
def pirmaisVards(param):
    pass

def pirmais_vards(param:int=2,
                  kautkas:str="",
                  saraksts:'list[int]'=[]) -> int:
    """Apraksta funkcijas darbību"""
    print(kautkas)
    print(saraksts)
    return param
rezultats = pirmais_vards(6, saraksts=[123])
print(rezultats)

# def bezgaliga_ievade(viens_mainigais:int, *mainigie, kautkas_cits) -> None:
#     print(mainigie)
# bezgaliga_ievade(1,2,3,4,5,6,7,8,9,kautkas_cits=2)
# print(1, 2, 3, 4, 5, sep=",")

x = 2
x = 9
def funkcija() -> None:
    print("!")
def funkcija() -> None:
    print("Nodefinēta pa jaunu!")
funkcija()

# Uzdevums
# Lietotājs ievada vairākus skaitļus:
def skaitluIevade() -> 'list[int]':
    skaitli = []
    while True:
        ievade = input("Skaitlis:")
        if ievade.isdigit():
            skaitli.append(int(ievade))
        else:
            break
    return skaitli
# Jāuzraksta funkcija, kas saskaita skaitļu summu sarakstā un izsaucat to
# izmantojot funkcijas skaitluIevade izvadi.
def sumList(saraksts:'list[int]') -> None:
    summa = 0
    for iii in saraksts:
        summa += iii
    return summa

# ievaditie_skaitli = skaitluIevade()
# print(ievaditie_skaitli)
# rezultats = sumList(ievaditie_skaitli)
# print(rezultats)
print(sumList(skaitluIevade()))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada lielāko skaitli
def findMax(*skaitli):
    max_num = skaitli[0]
    for iii in skaitli:
        if max_num < iii:
            max_num = iii
    return max_num
print(findMax(1,3,6,8,222,8,4,32,84)) # == 222

# Rekursija: Funkcija, kas izsauc pati sevi:
# Funkcija izvada skaitļus no n (ievade) līdz 0 skaitot uz leju
# Paskatīsimies pēc KD
# def recurse(param1):
#     print(param1)
#     if param1 > 0:
#         return recurse(param1-1)
#     elif param <= 0:
#         return 0

# Funkcija funkcijā
# Lūdzu tā nedarīt
# def funkcija1():
#     def funkcija2():
#         print("Sveiki no funkcijas 2!")
#     funkcija2() # Zem funkcijas - tiks izsaukta
# funkcija2() # Kļūda!

# Globālo mainīgo izvade
# Lūdzu tā nedarīt
# a = 10
# def funkcija():
#     global a
#     print(a) # 10