# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def utolso_x_szo(szoveg: str, szam: int):
    if not isinstance(szoveg, str) or not isinstance(szam, int) or len(szoveg.strip().split()) < szam or szam <= 0:
        return "-"

    uj = szoveg.split()

    vege = []
    irasjel = "!.,?"
    for szo in uj:
        for betu in szo:
            if betu in irasjel:
                return "-"

        vege.append(szo)

    mondat = []
    for i in range(0,len(vege)):
        if i >= len(vege) - szam:
            mondat.append(vege[i])

    aha = " ".join(mondat)
    aha += "."
    return aha.capitalize()


# print(utolso_x_szo('én vagyok a legnagyobb           rajongód', 55))
# print(utolso_x_szo('vigyázni kell magamra nincs b terv', 4))
# print(utolso_x_szo('na most figyeld öcsikesz azarát metriosz-zintosz', 2))

def karakter_modusz(szoveg: str):
    if not isinstance(szoveg, str) or len(szoveg) == 0 or "uwu" in szoveg:
        return  {"hibas" : -1}

    dikt = {}
    for elem in szoveg:
        if elem != " " and elem != "\n":
            if elem not in dikt:
                dikt[elem] = 1
            else:
                dikt[elem] += 1

    maxszam = 0
    maxbetu = ""
    for kulcs, ertek in dikt.items():
        if maxszam < ertek:
            maxszam = ertek
            maxbetu = kulcs

    return {maxbetu: maxszam}

# print(karakter_modusz("aaabbc"))
# print(karakter_modusz('mondtam, fuss el, szedd a lábad, jól elbújtál, nem talállak '))
# print(karakter_modusz('megvárom veled a buszt uwu de csak ha szeretnéd owo'))

class Cipo():
    def __init__(self, marka: str,meret: int, _ar: int = 10000):
        self.marka = marka
        self.meret = meret

        if not isinstance(_ar, int):
            self._ar = 10000
        else:
            if _ar > 0:
                self._ar = _ar
            else:
                self._ar = 10000

        self.matricak = []

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, ar):
        if not isinstance(ar, int):
            self._ar = 10000
        else:
            if ar > 0:
                self._ar = ar
            else:
                self._ar = 10000

    def matrica_hozzaadas(self, szoveg: str):
        if not isinstance(szoveg, str):
            raise ValueError("Hibas matrica!")

        uj = ""
        uj += szoveg[0: len(szoveg): 2] #lehet nem kell a -1

        if uj not in self.matricak:
            self.matricak.append(uj)

    def matrica_torles(self, eredeti: str):
        if not isinstance(eredeti, str):
            raise ValueError("Hibas matrica!")

        uj = ""
        uj += eredeti[0: len(eredeti): 2] #lehet nem kell a -1

        if uj in self.matricak:
            self.matricak.remove(uj)

    def __str__(self):
        if len(self.matricak) == 0:
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft es meg se lett meg sertve matricakkal."

        return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft. {len(self.matricak)} db matrica van rajta.\nNev szerint: " + ", ".join([matrica for matrica in self.matricak])+ "."

    def __iadd__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")

        for matrica in other.matricak:
            self.matricak.append(matrica) # lehet bajsz

        self.ar = self.ar + int(other.ar * 0.7)

        return self

    def __eq__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")

        return self.ar == other.ar and self.marka == other.marka



# egy_cipo = Cipo("Nike", 35, 5000)
# egy_masik_cipo = Cipo("Adidas", 36, 5005)
# egy_cipo.ar = -1
# egy_masik_cipo.matrica_hozzaadas("premiumkakaoscsigaa")
# egy_masik_cipo.matrica_hozzaadas("premiumkakaoscsigaa")
# egy_masik_cipo.matrica_hozzaadas("Kekwm")
# egy_cipo += egy_masik_cipo
# print(egy_cipo) # Az uj Nike markaju cipo, EU 35 meretu cipo ara jelenleg
# #13503 Ft. 2 db matrica van rajta.
# # Nev szerint: Valami, Kekw.
# print(egy_cipo == egy_masik_cipo) # False