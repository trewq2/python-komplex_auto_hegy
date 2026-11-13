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

def magassag(hegy):
    return hegy["magassag"]

rendezett = sorted(hegyek, key=magassag, reverse=True)
with open("magas_hegyek.txt", "w", encoding="utf-8") as fajl:
    for hegy in rendezett:
        if hegy["magassag"] >= 900:
            fajl.write(f"{hegy['nev']};{hegy['hegyseg']};{hegy['magassag']}\n")

print("Elkészült a magas_hegyek.txt fájl.")
