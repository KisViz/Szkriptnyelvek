class Pilota:
    def __init__(self, _nev: str, _skill: int = 80):
        self._nev = _nev
        self._skill = _skill

    @property
    def nev(self):
        return self._nev

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, _skill):
        self._skill = _skill

class Csapat:
    def __init__(self, nev: str):
        self._nev = nev
        self.pilotak = []

    def __iadd__(self, pilota: Pilota):
        if not isinstance(pilota, Pilota):
            raise TypeError("A csapatba csak pilotak johetnek, Axerwaliakok nem!")
        elif pilota.skill < 80:
            raise ValueError("A csapatba csak megfelelo kepessegu pilotak johetnek!")
        else:
            self.pilotak.append(pilota)

        return self

    def __str__(self):
        string = ", ".join(pilota.nev for pilota in self.pilotak)
        return string

    def __float__(self):
        if len(self.pilotak) == 0:
            raise ValueError("A csapat ures!")
        else:
            szaml = 0
            for pilotak in self.pilotak:
                szaml += pilotak.skill

            return szaml / len(self.pilotak)

    @property
    def nev(self):
        return self._nev

def megmaradt_versenyzok(csapatok: list[Csapat])-> list[Pilota]:
    maradtak = []

    for csapat in csapatok:

        for pilota in csapat.pilotak:
            if pilota.skill > 95 and len(csapat.pilotak) > 1 and csapat.__float__() > 90:
                maradtak.append(pilota)

    return maradtak

class SenkiNemMaradtVersenyben(Exception):
    def __init__(self):
        super().__init__("Minden pilota kiesett")

def statisztika(inputf: str, outputf: str):
    dikt = {}
    with open(inputf, "r") as file:
        for sor in file:
            adat = sor.strip().split(";")
            if adat[2] in dikt:
                try:
                    dikt[adat[2]] += Pilota(adat[0], int(adat[1]))
                except ValueError:
                    pass
            else:
                dikt[adat[2]] = Csapat(adat[2])
                try:
                    dikt[adat[2]] += Pilota(adat[0], int(adat[1]))
                except ValueError:
                    pass
    # for key, value in dikt.items():
    #     print(key)
    #     for elem in value.pilotak:
    #         print(elem.nev)
    #     print("--------------------------------")

    lista = []
    for key, value in dikt.items():


        if value.__float__() > 90:
            for elem in value.pilotak:
                lista.append(elem.nev)
        # print("--------------------------------")

    # print(lista)

    if len(lista) == 0:
        raise SenkiNemMaradtVersenyben()
    else:
        with open(outputf, "w") as file:
            for elem in lista:
                file.write(elem + "\n")



statisztika("be.txt", "ki.txt")