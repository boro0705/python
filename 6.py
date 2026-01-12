import random
fejek= random.randint(1,9)
szinek=("zöld", "piros","fekete")
szin= random.choice(szinek)
if fejek == 1 and szin == "zőld":
    print("Szia Süsü!")
elif fejek in (1,2,3,4):
    print(f"A {szin} sárkány gyenge")
elif fejek in (5,6,7):
    print(f"a {szin} sáárkány közepes erejű")
else:
    print(f"A {szin} sárkány félelmetes")
          
#2
kincsek = ("arany", "ezüst", "semmi") 
kincs = random.choice(kincsek)
kulcs = random.randint(1,5)
if kulcs < 3:
    print("A kulcs túl gyenge a láda zárva marad")
elif kincs == "semmi":
    print("A láda üres")
else:
    print(f"a láda tartalma {kincs}")

#3
karakterek= ("lovag", "kereskedő", "paraszt")
karakter= random.choice(karakterek)
hid = random.randint(50,500)
suly = random.randint(70,120)
if hid < suly :
    print("A híd leszakadt")
elif hid >= suly and (hid-suly) <= 10 :
    print(f"A híd recseg, de a {karakter} átér")
else:
    print(f"a {karakter} biztonságban átért")

#4
meseszamok = (3,7,9,12)
meseszam = random.choice(meseszamok)
jutalmak = ("drágakő", "arany", "ezüst")
jutalom = random.choice(jutalmak)
if meseszam %2 == 0:
    print(f"Blablabla, és a jutalmad {jutalom}")
elif meseszam in (3,9):
    print(f"kisebb próba vár rád, de {jutalom} a jutalom")
else:
    print(f"hét próbán kell keresztülmenned az életedért")

#5
specialitasok = ( "tűz", "víz" "föd")
varazslo1= random.choice(specialitasok)
varazslo2 = random.choice(specialitasok)
if varazslo1 == "tűz" and varazslo2 == "föld" or varazslo1 == "víz" and varazslo2 == "tűz"  or varazslo1 == "föld" and varazslo2 == "víz":
    print("Az első varázsó győzött")
elif  varazslo1 == varazslo2:
    print("aA varázslók nem bírtak egymással")
else:
    print("a második varázsló győzött")

