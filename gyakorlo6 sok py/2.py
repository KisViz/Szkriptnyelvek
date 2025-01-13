# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def minta_egyezesek(elso: dict, masodik: dict):
    if len(elso) == 0 and len(masodik) == 0:
        return 0

    szaml = 0
    if len(masodik) == len(elso):
        for kulcs, ertek in elso.items():
            try:
                if masodik[kulcs] == elso[kulcs]:
                    szaml += 1
            except Exception:
                return -1
    else:
        return -1
    return szaml

# print(minta_egyezesek({"10:00": 33, "11:30": 66, "13:00": 132}, {"10:00": 33, "11:30": 63,
# "13:00": 132}))
# print(minta_egyezesek({"10:00": 33, "11:30": 66, "13:00": 132}, {"10:00": 33, "11:00": 66,
# "13:00": 132}))
# print(minta_egyezesek({"10:00": 33, "11:30": 66, "13:00": 132}, {}))