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

if len(hegyek) > 0:
    magas = hegyek[0]
    alacsony = hegyek[0]
    for hegy in hegyek:
        if hegy["magassag"] > magas["magassag"]:
            magas = hegy
        if hegy["magassag"] < alacsony["magassag"]:
            alacsony = hegy
    print("Legmagasabb:", magas["nev"], magas["magassag"], "m")
    print("Legalacsonyabb a fájlban:", alacsony["nev"], alacsony["magassag"], "m")
else:
    print("Nincs adat.")
