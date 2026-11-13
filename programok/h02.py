hegyek = []
with open("hegyek.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        if sor.strip() == "":
            continue
        adatok = sor.strip().split(";")
        hegy = {
            "nev": adatok[0],
            "hegyseg": adatok[1],
            "magassag": int(adatok[2])
        }
        hegyek.append(hegy)

osszeg = 0
for hegy in hegyek:
    osszeg = osszeg + hegy["magassag"]

print("Magasságok összege:", osszeg, "m")
if len(hegyek) > 0:
    print(f"Átlagmagasság: {osszeg / len(hegyek):.1f} m")
else:
    print("Nincs adat.")
