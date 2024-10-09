# Uzdevums:
# Uzrakstīt programmu, kurā lietotājs ievada skaitli, un programma
# izvadīs rindas ar asteriskiem (*) - sākot ar vienu asterisku pirmajā
# rindā un par vienu vairāk katrā nākošajā

# piem. ievade 4
# Izvade:
# *
# **
# ***
# ****
ievade = int(input("Skaitlis: "))
for iii in range(1, ievade+1):
    print("*" * iii)

# Spēle: Uzmini skaitli
# Spēle uzģenerē nejaušu skaitli:
import random
x = random.randint(1, 100) # Nejaušs skaitlis no 1 līdz 100
# Ciklā: Lietotājs ievada skaitli (input).
# Programma pārbauda vai skaitlis ir uzminēts, 
# ja nav pasaka vai ievadītais # skaitlis ir lielāks, 
#   vai mazāks par nejaušo skaitli.
# Visas lietotāja ievades (minējumus) jāsaglabā sarakstā
# Kad lietotājs ir uzminējis skaitli - 
# Izvadīt 'Uzvara'
# Izvadīt minējumu skaitu (len(...)), lietotāja minējumus