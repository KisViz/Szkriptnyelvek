def is_disarium(szam: int):
    szoveg = str(szam)

    szaml = 0
    for i in range(1,len(szoveg) + 1):
        szaml += int(szoveg[i - 1]) ** i

    return szaml == int(szam)

# print(is_disarium(42))

def letter_combinations(szoveg: str):
    billentyuzet = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    if not szoveg:
        return []

    kombinaciok = ['']

    for szam in szoveg:
        # print("szam:",szam)
        uj_kombinaciok = []
        for komb in kombinaciok:
            # print("komb:",komb)
            for betu in billentyuzet[szam]:
                # print("betu:",betu)
                uj_kombinaciok.append(komb + betu)
                # print("uj_kombinaciok:",uj_kombinaciok)
        kombinaciok = uj_kombinaciok

    return kombinaciok

# print(letter_combinations("532"))

class Savanyusag():
    def __init__(self, minoseget_megorzi: tuple, nyitva: bool, elemek: list):
        self.minoseget_megorzi = minoseget_megorzi
        self.nyitva = nyitva
        self.elemek = elemek

        dikt = {}
        for elem in elemek:
            if elem not in dikt:
                dikt[elem] = 1
            else:
                dikt[elem] += 1

        if len(dikt) > 1:
            self._tipus = "csalamade"
        else:
            self._tipus = elemek[0]

    @property
    def tipus(self):
        return self._tipus

    @tipus.setter
    def tipus(self, tipus: str):
        if tipus in self.elemek:
            self._tipus = tipus

    def szavatos(self, ev, ho, nap):
        return self.minoseget_megorzi[0] == ev and self.minoseget_megorzi[1] == ho and self.minoseget_megorzi[2] == nap

    def fedel_csavar(self):
        self.nyitva = not self.nyitva

    def __iadd__(self, other):
        if not isinstance(other,Savanyusag):
            return self

        if not self.nyitva:
            raise Exception("A savanyusag fedele zarva van!")
        if not other.nyitva:
            raise Exception("A masik savanyusag fedele zarva van!")

        for elem in other.elemek:
            self.elemek.append(elem)

        dikt = {}
        for elem in self.elemek:
            if elem not in dikt:
                dikt[elem] = 1
            else:
                dikt[elem] += 1

        if len(dikt) > 1:
            self._tipus = "csalamade"
        else:
            self._tipus = self.elemek[0]

        self.minoseget_megorzi = min(self.minoseget_megorzi, other.minoseget_megorzi)

        return self

    def __str__(self):
        return f"Savanyitott {self.tipus}, aminek a fedele" + "nyitva" if self.nyitva else "zarva" + "."

    def __imul__(self, szam: int):
        # for elem in self.elemek:
        #     for i in range(szam):
        #         self.elemek.append(elem)
        self.elemek *= szam
        return self

    def __eq__(self, other):
        return self.tipus == other.tipus and self.elemek == other.elemek and self.minoseget_megorzi == other.minoseget_megorzi and self.nyitva == other.nyitva and sorted(self.elemek) == sorted(other.elemek)
