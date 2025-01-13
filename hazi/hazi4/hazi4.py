# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

class Palack():

    def __init__(self, ital: str, max_urtartalom: int, _jelenlegi_urtartalom: int = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = _jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, ertek):
        if ertek > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        else:
            self._jelenlegi_urtartalom = ertek
            if ertek == 0:
                self.ital = None

    def suly(self):
        return self.max_urtartalom/35 + self._jelenlegi_urtartalom

    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other):
        if not isinstance(other, Palack):
            return False

        return self.max_urtartalom == other.max_urtartalom and self.jelenlegi_urtartalom == other.jelenlegi_urtartalom and self.ital == other.ital

    def __iadd__(self, other):
        if not isinstance(other, Palack):
            return self

        if self.ital is None:
            self.ital = other.ital

        self.jelenlegi_urtartalom = self.jelenlegi_urtartalom + other.jelenlegi_urtartalom

        if self.ital != other.ital and self.jelenlegi_urtartalom > 0 and other.jelenlegi_urtartalom > 0:
            self.ital = "keverek"
        else:
            self.ital = other.ital

        return self

class VisszavalthatoPalack(Palack):

    def __init__(self, ital: str, max_urtartalom: int, _jelenlegi_urtartalom: int = 1, palackdij: int = 25):
        super().__init__(ital, max_urtartalom, _jelenlegi_urtartalom)
        self.palackdij = palackdij

    def __str__(self):
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self.jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

class Rekesz():

    def __init__(self, max_teherbiras: int):
        self.max_teherbiras = max_teherbiras
        self.palackok = []

    def suly(self):

        szaml = 0
        for elem in self.palackok:
            szaml += elem.suly()

        return szaml

    def uj_palack(self, palack: Palack):

        if self.suly() + palack.suly() <= self.max_teherbiras:
            self.palackok.append(palack)

    def osszes_penz(self):

        szaml = 0
        for elem in self.palackok:
            if isinstance(elem, VisszavalthatoPalack):
                szaml += elem.palackdij

        return szaml

