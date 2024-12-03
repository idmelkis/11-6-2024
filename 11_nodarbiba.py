# Uzdevums: Izveidojat mapē "mape" failus ar nosaukumiem no 0 līdz 100
# import os
# import random

# if not os.path.isdir("mape"):
#     os.mkdir("mape")

# faila_nosaukums = random.randint(0, 100)
# nejausa_vertiba = random.randint(0, 100)

# print(f"Fails: {faila_nosaukums}; {nejausa_vertiba}")

# for i in range(0, 101):
#     with open(f"mape\\{i}", "w") as f:
#         if i == faila_nosaukums:
#             f.write(str(nejausa_vertiba))

# while True:
#     lietotaja_ievade = input("Minējums: ")
#     if int(lietotaja_ievade) != nejausa_vertiba:
#         print('Nepareizi')
#     else:
#         print('Pareizi!')
#         break

# Uzdevums: Izmainīt šo (^) programmu lai kādā no izveidotajiem failiem (nejauši izvēlēts)
# ierakstītu vērtību uz labu laimi. Pēc tam prasīt lietotājam ievadīt
# šo vērtību un izvadīt, vai ievade bija pareiza, vai nepareiza.

# for file in os.listdir("mape"):
#     os.remove(f"mape\\{file}")
# os.rmdir("mape")


# Uzdevums: Atverat failu 11_nodarbiba_1.txt
# Izvadat vārdu skaitu failā.
# Vārdi ir atdalīti ar atstarpi (split).
with open("11_nodarbiba_1.txt", "r", encoding="UTF-8") as file:
    saturs = file.read()
    # 1. var - sadalam
    #print(f"Garums: {len(saturs.split(' '))}")
    # 2. var - skaitam atstarpes
    atstarpes = 0
    for char in saturs:
        if char == " ":
            atstarpes += 1
    print(atstarpes + 1)

# Uzdevums:
# atverat failu 11_nodarbiba_1.txt
# izveido jaunu failu ar to pašu nosaukumu + "_uppercase"
#  (piem. fails.txt -> fails_uppercase.txt). 
#  11_nodarbiba_1.txt -> 11_nodarbiba_1_uppercase.txt
# otrajā failā saglabājat pirmā faila saturu pārveidojot 
# visus burtus par lielajiem. (mainigais.upper())
faila_nosaukums = "11_nodarbiba_1.txt"
with open(faila_nosaukums, "r", encoding="UTF-8") as file:
    # Variants kas strādā ar punktiem:
    #otra_faila_nosaukums = ".".join(faila_nosaukums.split(".")[:-1])+"_uppercase.txt"
    faila_saturs = file.read()

    otra_faila_nosaukums = faila_nosaukums.split(".")[0]+"_uppercase.txt"
    with open(otra_faila_nosaukums, "w", encoding="UTF-8") as file2:
        file2.write(faila_saturs.upper())

# Faila 11_nodarbiba_1.txt saturs -- Jāizveido pašam, saturu varat 
# sarakstīt paši, vai atverat vietni www.lipsum.com un 
# spiežat pogu "Generate Lorem Ipsum" un iekopējat to failā.