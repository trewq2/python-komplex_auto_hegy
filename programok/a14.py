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

def kategoria(km):
    if km < 100000:
        return "keveset futott"
    elif km < 200000:
        return "közepesen futott"
    else:
        return "sokat futott"

for auto in autok:
    besorolas = kategoria(auto["km"])
    print(auto["marka"], auto["tipus"], "–", besorolas)
