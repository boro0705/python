print("hajrá fradi")

import random
kocka = random.randint(1,6)
lehetőségek = (1,2,3,4,5,6)
kocka2 = random.choice(lehetőségek)
print(f"Az első kocka értéke {kocka}") 
else:
    print("páratlan a dobás eredménye")

#2
tipp = input("fej vagy írás?").lower()
#fej; írás; Fej; Írás; FEJ; ÍRÁS
oldalak = ("fej", "írás")
erme = random.choice(oldalak)
if tipp == erme :
    print("Nyertél egy fantasztikus dk órát")
else:
    print("vesztettél")
#3
jegy= random.randint(1,5)
szoveges = ("elégtelen" , "elégséges","közepes","jó", "jeles")
print(f"az osztályzatod {jegy} ({szoveges[jegy-1]})")

#4
meseszam = random.randint(1,10)
if meseszam in (3,7,9):
    print(f"A véletlen egy meseszámot sodort eléd")
else:
    print("A mesék a gyerekeknek valók")

#5
allatok = ("kutya", "macska", "ló", "tehén")
valasztas = random.choice(allatok)
if valasztas == "kutya" or valasztas == "macska":
    print(f"A {valasztas} háziállat")
else:
    print(f"a {valasztas} haszonállat")

#6
