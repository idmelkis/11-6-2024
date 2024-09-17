#nosaukums = 0
# nat. skaitļi (int)
# daļskaitļi (float)
# teksts (str)
#a = "teksts"
# simbols (chr)
#b = 'c'
# saraksti [] (list)
# loģiskie (true/false)(1/0) (bool)

#print("Kaut kāds teksts: " + str(nosaukums))
# str()
#int("asd")

#a = 1 + 2
#a += 2 # a = a + 2
#a -= 2 # a = a - 2

#print("Rinda1\nRinda2")
# print("""Rinda1
# Rinda2
# Rinda3""")

"""
Rinda1
Rinda2
Rinda3
"""

# ctrl + /
# alt: ctrl + k + c
# Rinda1
# Rinda1
# Rinda1

# mainigais = 123
# print("Kaut kāds teksts: " + str(mainigais) + "!")
# print(f"Kaut kāds teksts: {mainigais}!") # Formatēta izvade
#print(b"\xff\xf8\x00\x00\x00\x00\x00\x00!") # Binārā izvade
#print(u"āī📙📙📙!") # Ļauj izmantot unicode (piem. Emoji)
#print(r"\n\\!") # Teksts netiek apstrādāts (tieša izvade)

#saraksts = [ '2', '1', '3', 123, True ]
#otrs_saraksts = ('2', '1', '3', 123, True) # Tuple
#saraksts[1] = '3'
#otrs_saraksts[1] = '3' # Kļūda
#teksts = f"213{123}"
# teksts[0] = '2' # Kļūda
#teksts[:1] # izvada "21"

# x = input("Ievade: ")
# x = int(x)
# ==, is - vienāds ar
# !=, <> (vairs neatbalsta), not - nav vienāds
# >= - lielāks & vienāds
# > - lielāks
# <= - mazāks & vienāds
# < - mazāks
#if x > 10:
#    print("Jā")
#if not "" is "1":
#    print("Jā")
#if not x == 1:
#if x != 1:
#if 1 <> 0:
#print(x)

# Uzdevums: Kalkulators
# Ievade: divi skaitļi, darbība
# Izvade: Darbības rezultāts
iev1 = int(input("Pirmais skaitlis: "))
iev2 = int(input("Otrais skaitlis: "))
iev3 = input("Darbība: ")
if iev3 == "+":
    print(f"{iev1} + {iev2} = {iev1+iev2}")
# ... -, *, /