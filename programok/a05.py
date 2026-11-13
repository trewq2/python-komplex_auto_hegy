sor = "Mercedes;C 200;fekete;7.5;125000;2018;jó"
adatok = sor.strip().split(";")
print(adatok)

marka = adatok[0]
tipus = adatok[1]
gyorsulas = float(adatok[3])
km = int(adatok[4])

print(marka, tipus)
print(f"Egy 100 km-es út után: {km + 100} km")
print(f"Gyorsulás: {gyorsulas:.1f} s")
