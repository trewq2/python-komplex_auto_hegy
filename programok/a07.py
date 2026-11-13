# Beolvassuk és eltároljuk az autók adatait.
autok = []
with open("autok.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        if sor.strip() == "":
            continue  # Az üres sort kihagyjuk.
        adatok = sor.strip().split(";")
        auto = {
            "marka": adatok[0],
            "tipus": adatok[1],
            "szin": adatok[2],
            "gyorsulas": float(adatok[3]),
            "km": int(adatok[4]),
            "evjarat": int(adatok[5]),
            "allapot": adatok[6]
        }
        autok.append(auto)

print("Autók száma:", len(autok))
print("Első márka:", autok[0]["marka"])
