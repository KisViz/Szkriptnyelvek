class Pilota:

    def __init__(self, nev:str, skill=80):
        self._nev = nev
        self._skill = skill

    @property
    def nev(self):
        return self._nev
    @property
    def skill(self):
        return self._skill
    @skill.setter
    def skill(self, skill):
        self._skill = skill

class Csapat:
    def __init__(self, nev:str):
        self.nev = nev
        self.pilotak = list()

    def __iadd__(self, pilota:Pilota):
        if not isinstance(pilota, Pilota):
            raise TypeError("A csapatba csak pilotak johetnek, Axerwaliakok nem!")
        elif pilota.skill < 80:
            raise ValueError("A csapatba csak megfelelo kepessegu pilotak johetnek!")

        self.pilotak.append(pilota)

        return self

    def __str__(self):
        return ", ".join([p.nev for p in self.pilotak])

    def __float__(self):
        if len(self.pilotak) == 0:
            raise ValueError("A csapat ures!")

        return float(sum([p.skill for p in self.pilotak])) / len(self.pilotak)

def megmaradt_versenyzok(csapatok:list):
    return [pilota for csapat in csapatok if len(csapat.pilotak) > 1 and float(csapat) > 90.0 for pilota in csapat.pilotak if pilota.skill >= 95] #bocsi

class SenkiNemMaradtVersenyben(Exception):
    def __init__(self):
        super().__init__("Minden pilota kiesett")

def statisztika(input_file, output_file):
    csapatok = list()

    with open(input_file, "r") as f:
        for line in f:
            line = [l.strip() for l in line.split(";")]
            if line[2] not in [cs.nev for cs in csapatok]:
                csapatok.append(Csapat(line[2]))
            try:
                csapatok[[cs.nev for cs in csapatok].index(line[2])] += Pilota(line[0], int(line[1]))
            except ValueError:
                continue

    maradek = megmaradt_versenyzok(csapatok)

    if len(maradek) == 0:
        raise SenkiNemMaradtVersenyben()

    with (open(output_file, "w") as f):
        f.write("\n".join([p.nev for p in maradek]))
        f.write("\n")

#statisztika("input.txt", "out.txt")