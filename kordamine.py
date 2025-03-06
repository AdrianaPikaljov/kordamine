#for – повторяет что-то определенное количество раз.
#if – проверяет условие.
#else – выполняет код, если if не сработал.
#while – повторяет код, пока условие истинное.
#try-except – ловит ошибки, чтобы программа не ломалась.
#while True – бесконечный цикл, который нужно прерывать (break).

#3 variant ülesanne 1
n = int(input("sisesta mittu korda korrata (1-9): "))
if n < 1 or n > 9:# kontrollime kas arv on õige
    print("viga, sisesta arv 1 - 9")
else:
   maja = '''  -----
 |  O  |
 !  -  !
  -----'''

for i in range(n):
            print(maja)
            print(" ")
            


#ulesanne 2
print(" ")
try:
    aste= int(input("sisestage aste: "))
    n = int(input("sisesta arv: "))
    if aste < 1:
        print("viga")
    else:
        maxnum = n ** 3 #predel otsime
        i = 1 #alustame 1
        while i **aste <= maxnum: #kuni i ne bydet aste <= n3
            print(f"{i}**{aste} = {i **aste}")
            i += 1 #suurendame i
except:
    print("viga")

#ulesanne 3
print("")
import random

opilased = random.randint(5, 30) #gen arv
sumhinn =0 #muutuja hinnete summa selleks et summa tulemust salvestada

for i in range(opilased):
    hinne = random.randint(1, 100) #gen hinne
    sumhinn += hinne #lisame hinne hinnete summale

kesk= sumhinn / opilased #keskhinne
print(f"opilasi on {opilased} ja hinded {hinne} ")
print("keskhinne on:",kesk)



 #ulesanne 4
print("")
vanus=1 #alg vanus
kingitus=1 #alg kingitus
while kingitus<=100: #poka summa ei uletanud 100 dol
    vanus+=1 #suurendame vanust 
    kingitus+=vanus #lisame kingituseks praegune vanus
    print(f"ma saan sel aastal {vanus} vana ja ma saan sel aastal {kingitus} dollarit")
print(f"aastaks {vanus} ületab kingitus 100 dollarit.")

#ulesanne 5
print("")
a=0 #essa arv
b=1 #teine arv
for i in range(9): #kordame 9 korda 
    print(a, end=" ") #naitame tegev arvu
    v=a #maletab vanat tahendust a
    a=b #b on nyyd same nagu a
    b=v+b #b on nyyd summa
