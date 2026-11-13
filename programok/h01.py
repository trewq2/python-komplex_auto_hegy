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

print("Csúcsok száma:", len(hegyek))
for hegy in hegyek:
    print(hegy["nev"], hegy["hegyseg"], hegy["magassag"], "m")
