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

def kilometer_osszeg(jarmuvek):
    osszeg = 0
    for auto in jarmuvek:
        osszeg = osszeg + auto["km"]
    return osszeg

def kilometer(auto):
    return auto["km"]

def kategoria(km):
    if km < 100000:
        return "keveset futott"
    elif km < 200000:
        return "közepesen futott"
    else:
        return "sokat futott"

print("Autók száma:", len(autok))
osszes_km = kilometer_osszeg(autok)
print("Összes kilométer:", osszes_km)
if len(autok) > 0:
    print(f"Átlagos kilométeróra: {osszes_km / len(autok):.1f} km")
    gyorsulas_osszeg = 0
    leggyorsabb = autok[0]
    legtobbet_futott = autok[0]
    for auto in autok:
        gyorsulas_osszeg = gyorsulas_osszeg + auto["gyorsulas"]
        if auto["gyorsulas"] < leggyorsabb["gyorsulas"]:
            leggyorsabb = auto
        if auto["km"] > legtobbet_futott["km"]:
            legtobbet_futott = auto
    print(f"Átlagos gyorsulási idő: {gyorsulas_osszeg / len(autok):.2f} s")
    print("Leggyorsabb:", leggyorsabb["marka"], leggyorsabb["tipus"])
    print("Legtöbbet futott:", legtobbet_futott["marka"], legtobbet_futott["tipus"])
else:
    print("Üres a garázs, nincs átlag vagy szélsőérték.")

rendezett = sorted(autok, key=kilometer)
with open("garazs_jelentes.txt", "w", encoding="utf-8") as fajl:
    for auto in rendezett:
        besorolas = kategoria(auto["km"])
        sor = f"{auto['marka']};{auto['tipus']};{auto['km']};{besorolas}"
        print(sor)
        fajl.write(sor + "\n")
print("Elkészült a garazs_jelentes.txt fájl.")
