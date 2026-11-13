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

if len(autok) > 0:
    leggyorsabb = autok[0]
    legtobbet_futott = autok[0]

    for auto in autok:
        if auto["gyorsulas"] < leggyorsabb["gyorsulas"]:
            leggyorsabb = auto
        if auto["km"] > legtobbet_futott["km"]:
            legtobbet_futott = auto

    print("Leggyorsabb:", leggyorsabb["marka"], leggyorsabb["tipus"])
    print("Ideje:", leggyorsabb["gyorsulas"], "s")
    print("Legtöbbet futott:", legtobbet_futott["marka"], legtobbet_futott["tipus"])
    print("Kilométer:", legtobbet_futott["km"])
else:
    print("Üres a garázs.")
