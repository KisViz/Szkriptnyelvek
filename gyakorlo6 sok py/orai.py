#1
def reverse_normalize(szoveg: str):
    szoveg = szoveg[::-1]
    szoveg = szoveg.split()
    return " ".join(szoveg)

# print(reverse_normalize(" ez egy             minta         szoveg))

#2
def eminem(szoveg: str):
    szoveg = szoveg.replace(" ", "")
    return szoveg.capitalize()

# print(eminem(" ez egy             minta         szoveg"))

#3
def statisztika(szoveg: str):
    szoveg = szoveg.replace(" ", "")

    dit = {}
    for betu in szoveg:
        if betu not in dit:
            dit[betu] = 1
        else:
            dit[betu] += 1

    return dit

print(statisztika(" ez egy      vvvvvv       minta         szoveg"))

#4
def winner_betu(szoveg: str):
    dikt = statisztika(szoveg)
    maxszam = 0
    maxbetu = ""
    for betu, szam in dikt.items():
        if szam > maxszam:
            maxszam = szam
            maxbetu = betu

    return maxbetu

print(winner_betu(" ez egy      vvvvvv       minta         szoveg"))

#5
class Asvanyviz():
    def __init__(self, marka, urtartalom, _ph = 5):
        self.marka = marka
        self.urtartalom = urtartalom
        self._ph = _ph
        self.asvanyi_anyagok = []

    @property
    def ph(self):
        return self._ph

    @ph.setter
    def ph(self, ph):
        if ph < 0:
            self._ph = 5
        else:
            self._ph = ph

    def asvanyi_anyag_hozzaad(self, szoveg: str):
        if not isinstance(szoveg, str):
            raise ValueError("Ne mergezd az ivovizet")
        else:
            self.asvanyi_anyagok.append(szoveg)

    def __iadd__(self, other):
        self.urtartalom += other.urtartalom

        for elem in other.asvanyi_anyagok:
            self.asvanyi_anyag_hozzaad(elem)

        return self

    def __str__(self):
        if len(self.asvanyi_anyagok) > 0:
            return f"{self.marka} viz, {self.urtartalom} literes, {self.ph} értékkel rendelkezik és ilyen ásványi anyagok vannak benne: " + ", ".join([anyag for anyag in self.asvanyi_anyagok])
        else:
            return f"{self.marka} viz, {self.urtartalom} literes, {self.ph} értékkel rendelkezik és nincs benne ásványi anyag."



# av1 = Asvanyviz("Márka1", 1)
# av2 = Asvanyviz("Márka2", 2)
# av1.asvanyi_anyag_hozzaad("Kalcium")
# av2.asvanyi_anyag_hozzaad("Magnézium")
#
# av1 += av2
#
# print(av1)
#
# av1.ph = -3
# print(av1.ph)
#
# av1.ph = 7
# print(av1.ph)
#
# av2.asvanyi_anyag_hozzaad("Kacsa")
# av1 += av2
#
# print(av1)
