"""import random
import time
for szam in range(10,0, -1):
    time.sleep(1)
    if szam >= 6:
        print(szam)
    elif szam in range(1,6):
        print(f"{szam} rendszerellenörzés")
        if random.randint(1,10) == 1:
                print("MEGHIBÁSODÁS")
                break
    if szam == 1 : 
         print("kilövés")    """

"""import random
hatos=0
for i in range(50):
     dobas= random.randint(1,6)
     if  dobas == 6:
        hatos += 1
if hatos >= 10:
          print("szerencsés napod van")
elif hatos <= 5:
      print("szerensérlen napod van")
else:
     print("átlagos napod van ")"""

"""import random
import string
kisbetuk= string.ascii_lowercase
szamok= string.digits
irasjelek=string.punctuation

gyuras= kisbetuk + szamok + irasjelek
jelszo = ""
for i in range (12):
   jelszo +=  random.choice(gyuras)
print(f" a titkosügynök jelszava {jelszo}")
"""
import random
fagy = 0
osszeg = 0
for nap in range(1,32):
    homerseklet= random.randit(-5,15)
    osszeg +=homerseklet
    if homerseklet < 0:
        print(f"{nap}. {homerseklet}fok volt")
        fagy += 1
print(f"Fagyos napok száma{fagy}")
print(f" átlaghőmérséklet {összeg / nap}")