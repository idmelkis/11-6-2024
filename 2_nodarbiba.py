# x = 1
# match x:
#     case 1:
#         print("!")
#     case 2:
#         print("1")
# if x == 1:
#     print("!")
# elif x == 2:
#     print("1")

# Komentāri: Iezīmējat tekstu un nospiežat 
# ctrl + /

#saraksts = [ '2', '1', '3' ] 
#saraksts.append("jauna vērtība")
#print(saraksts)
#print(saraksts[1:2])

# Apvienot sarakstu
#print(",".join(saraksts) + "!")  # => "2,1,3!"

# while <loģiskā pārbaude>
# x = 0
# while x <= 4:
#     x += 1
#     if x == 1:
#         continue # Uzsāk nākošo iterāciju
#     if x == 3:
#         break # Apstādina ciklu
#     print(x)
#else:
#    print("Beigas!")


# for x in range(0,10):
#     print(x)
saraksts = [ '0', '1', '2', '3', '4' ] 

for x in saraksts[::2]: # Katra otrā vērtība
    print(x)

# Uzdevums: Uzrakstīt while ciklu, kas izvada katru otro vērtību
# no saraksta "saraksts".
x = 0
while x < len(saraksts):
    print(saraksts[x])
    x += 2

print("===")
for i in range(6): # 0 - 5
    print(i)
print("===")

# Uzdevums: uzrakstīt for UN while ciklus,
# kuros sarakstā _ievada_ 5 vērtības.
saraksts = []
for i in range(6): # 0 - 5 
    saraksts.append(input("For ievade: "))

skaititajs = 0
while skaititajs < 6: # 0 - 5
    saraksts.append(input("While ievade: "))
    skaititajs +=1

print(saraksts)