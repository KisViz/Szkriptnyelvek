# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def exponens(szoveg:str, szoszam: int = 1, kitevo: int = 1):
    return str(szoveg) * szoszam ** kitevo if kitevo > 0 else str(szoveg) * szoszam

# print(exponens("alma", 2, 2))
# print(exponens("alma", 2, 2) == "almaalmaalmaalma")
# print(exponens("körte", 3, 0))
# print(exponens("körte", 3, 0) == "körtekörtekörte")
# print(exponens(10, 2, 3))
# print(exponens(10, 2, 3) == "1010101010101010")

def kodolo(szoveg: str):
    kodok = {
        "a": "#",
        "e": "##",
        "i": "###",
        "o": "####",
        "u": "#####"
    }

    uj = ""
    for elem in szoveg:
        if elem in kodok:
            uj += kodok[elem]
        else:
            uj += elem

    return uj

# print(kodolo("alma"))
# print(kodolo("alma") == "#lm#")
# print(kodolo("gumiabroncs"))
# print(kodolo("gumiabroncs") ==  "g#####m####br####ncs")
# print(kodolo("istálló"))
# print(kodolo("istálló") == "###stálló")