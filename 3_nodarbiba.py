# Uzdevums:
# Uzrakstat while ciklu, kas izvada skaitļus no 0
# līdz 10, izlaižot skaitļus 4 un 6
# x = 0
# while x <= 10:
#   if x == 4 or x == 6:
#     x += 1
#     continue
#   print(x)
#   x += 1

# Uzdevums:
# Uzrakstīt ciklu, kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Attiecīgi, ja skaitlis dalās ar 3 un 5, izvada FizzBuzz
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat to
# % - Modulus (izvada dalīšanās atlikumu)
# 4 % 2 == 0
for iii in range(1, 101):
    #print(f"Skaitlis: {iii}, dalot ar 3 atlikums ir {iii%3}")
    if iii % 3 == 0 and iii % 5 == 0:
        print("FizzBuzz")
    elif iii % 3 == 0:
        print("Fizz")
    elif iii % 5 == 0:
        print("Buzz")
    else:
        print(iii)

# Uzdevums:
# Uzrakstīt ciklu, kas
# ļauj lietotājam ievadīt vērtību
# saglabā to
# izvada visu ievadīto skaitļu tekošo 
#   vidējo vērtību
#piem.
#Iterācija 1: ievada 2, izvada 2
#Iterācija 2: ievada 4, izvada 3 (2, 4)
#Iterācija 3: ievada 10, izvada 5.3 (2, 4, 10)
#...
skaitli = []
while True:
    skaitli.append(int(input("Skaitlis"))) # Ievade un saglabāšana
    # Aprēķins:
    # Variants 1 (tie kas atceras sum komandu):
    print(sum(skaitli) / len(skaitli))
    
    # Variants 2 (tie kas neatcerās sum komandu):
    summa = 0
    for iii in skaitli:
        summa += iii
    print(summa / len(skaitli))