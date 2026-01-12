#

'''szoveg = input("írj be egy mondatot:").lower()
foujszoveg= ""
r karakter in szoveg:
    if karakter == "a": ujszoveg += "4"
    elif karakter =="e": ujszoveg +="3"
    elif karakter =="i": ujszoveg +="1"
    elif karakter ==  "o": ujszoveg +="0"
    else: ujszoveg += karakter
print(ujszoveg)'''

'''prim=True
szam=int(input("adj meg egy egész száot:"))
if szam<0:
    print("A szám negatív,nem prím")
elif szam==0:
    print("A szám nulla,nem prím")
elif szam==1:
    print("A szám egy,nem prím")
if szam==2:
    print("A szám kettő,prím")
else: 
    for oszto in range(2, szam//2 + 1):
        if szam % oszto == 0:
            prim =False
            break
if prim:
    print(f"A {szam} prím!")
else:
    print(f"A {szam} nem prím!")'''

import random
szamlalo=0
for perc in range (1,13):
    pulzus=random.randint(110,190)
    if pulzus <140:
        zona = "Bemelegítő zóna"
    elif 140<=pulzus<= 165:
        zona="zsírégető zóna"
    else:
        szamlalo += 1
        zona="ANAEROB zóna"
    print(f"{perc}. perc:{pulzus} bpm - {zona}")
    print(f"Veszélyes zónába léptél {szamlalo}alkalommal")

hp = 300
for i in range(1,6):
    sebzes = random.randint(20,100)
    kritikus= random.randint(1,5)
    if kritikus == 5:
        sebzes = sebzes * 2
    elif kritikus == 1:
        sebzes =0
        print("melléütés")
    hp = hp-sebzes
    print(f"a hős {sebzes} sebzett ezért a sarkánynak {hp}-ja van")
    if hp <= 0:
        print("győzelem")
        break
if hp > 0:
    print("A hős meghalt")





