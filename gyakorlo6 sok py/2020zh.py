from webbrowser import Error


def meccseredmenyek(eredmenyek: list):
    #Barcelona;Ferencváros;5-1
    dikt = {}
    for elem in eredmenyek:
        meccs = elem.split(';')
        if meccs[0] not in dikt:
            dikt[meccs[0]] = int(meccs[2].split('-')[0])
        else:
            dikt[meccs[0]] += int(meccs[2].split('-')[0])

        if meccs[1] not in dikt:
            dikt[meccs[1]] = int(meccs[2].split('-')[1])
        else:
            dikt[meccs[1]] += int(meccs[2].split('-')[1])

    return dikt

# print(meccseredmenyek([
# 'Barcelona;Ferencváros;5-1',
# 'Ferencváros;Barcelona;2-1',
# 'Barcelona;Juventus;1-0',
# 'Juventus;Barcelona;0-0'
# ]))

class Vizsga():
    def __init__(self, _targy):
        self._targy = _targy

        self.kerdesek = []
        self.pontok = []

    @property
    def targy(self):
        return self._targy

    @targy.setter
    def targy(self, targy):
        if not isinstance(targy, str) or len(targy) < 3:
            raise ValueError("A targy legalabb 3 karakter hosszu string legyen!")

        self._targy = targy

    def kerdest_felvesz(self, kerdes: str, pontszam: int):
        if isinstance(kerdes, str) and isinstance(pontszam, int):
            self.kerdesek.append(kerdes)
            self.pontok.append(pontszam)

    def osszpontszam(self):
        return  sum(self.pontok)

    def __iadd__(self, other):
        if not isinstance(other, Vizsga):
            raise TypeError("bajsz")
        else:
            for i in range(0,len(other.kerdesek)):
                if other.kerdesek[i] not in self.kerdesek:
                    self.kerdest_felvesz(other.kerdesek[i], other.pontok[i])

        return self

    def __str__(self):
        vege = f"{self.targy}\n"

        for i in range(0,len(self.kerdesek)):
            vege += f"{self.kerdesek[i]} ({self.pontok[i]} pont)\n"

        vege += f"Osszesen: {self.osszpontszam()}"

        return vege.strip()

    def __eq__(self, other):
        return self.targy == other.targy and self.pontok == other.pontok and self.kerdesek == other.kerdesek


# Teszt 1: Sikeres objektum létrehozás
vizsga1 = Vizsga("Matematika")
assert vizsga1.targy == "Matematika", "Hibás tárgy érték"
print("Teszt 1 sikeres: Objektum létrehozás")

# Teszt 2: Kivétel rövid tárgynévnél
try:
    vizsga2 = Vizsga("Hu")
except ValueError as e:
    assert str(e) == "A targy legalabb 3 karakter hosszu string legyen!", "Hibás kivételszöveg"
    print("Teszt 2 sikeres: Rövid tárgynév kivétel")

# Teszt 3: Kérdés felvétele és pontszám hozzáadása
vizsga1.kerdest_felvesz("Mi az a deriválás?", 10)
assert vizsga1.kerdesek == ["Mi az a deriválás?"], "Hibás kérdés felvétele"
assert vizsga1.pontok == [10], "Hibás pontszám felvétele"
print("Teszt 3 sikeres: Kérdés és pontszám felvétele")

# Teszt 4: Összpontszám kiszámítása
vizsga1.kerdest_felvesz("Mi az a integrálás?", 15)
assert vizsga1.osszpontszam() == 25, "Hibás összpontszám"
print("Teszt 4 sikeres: Összpontszám kiszámítása")

# Teszt 5: Két vizsga összeadása (+= operátor)
vizsga2 = Vizsga("Matematika")
vizsga2.kerdest_felvesz("Mi az a deriválás?", 10)
vizsga2.kerdest_felvesz("Mi az a valószínűség-számítás?", 20)

vizsga1 += vizsga2
assert len(vizsga1.kerdesek) == 3, "Hibás kérdésszám az összeadás után"
assert vizsga1.pontok == [10, 15, 20], "Hibás pontszám az összeadás után"
print("Teszt 5 sikeres: Vizsgák összeadása")

# Teszt 6: Szöveges megjelenítés (__str__)
print(vizsga1)

expected_str = ("Matematika\n"
    "Mi az a deriválás? (10 pont)\n"
                "Mi az a integrálás? (15 pont)\n"
                "Mi az a valószínűség-számítás? (20 pont)\n"
                "Osszesen: 45")
assert str(vizsga1) == expected_str, "Hibás szöveges megjelenítés"
print("Teszt 6 sikeres: Szöveges megjelenítés")

# Teszt 7: Két vizsga egyenlősége (__eq__)
vizsga3 = Vizsga("Matematika")
vizsga3.kerdest_felvesz("Mi az a deriválás?", 10)
vizsga3.kerdest_felvesz("Mi az a integrálás?", 15)
vizsga3.kerdest_felvesz("Mi az a valószínűség-számítás?", 20)

assert vizsga1 == vizsga3, "A két vizsga nem egyenlő, de annak kellene lennie"
print("Teszt 7 sikeres: Vizsgák egyenlősége")

