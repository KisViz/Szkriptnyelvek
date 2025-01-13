class Loot:
    def __init__(self, nev, meret = 1, ertek = 1):
        self.nev = nev  # a loot neve (pl. 'ősgyökér')
        self.meret = meret  # a loot mérete (cm^3-ben, a táskába pakoláshoz hasznos)
        self.ertek = ertek  # a loot értéke (hány $-ért lehet eladni)

    def __str__(self):
        return f"{self.nev} ({self.meret}) -> {self.ertek} $"

class Taska:
    def __init__(self, kapacitas: int):
        self.lootok = []
        self.kpacitas = kapacitas
        self.foglalt = 0

    def targyat_elrak(self, loot: Loot):
        if self.foglalt + loot.meret <= self.kpacitas:
            self.lootok.append(loot)
            self.foglalt += loot.meret

class VeryBigTaska(Taska):
    def __init__(self, kapacitas):
        super().__init__(kapacitas)

    def targyat_elrak(self, loot: Loot):
        self.lootok.append(loot)

    def __add__(self, other: Taska):
        uj = VeryBigTaska(self.kpacitas + other.kpacitas)
        uj.lootok = self.lootok + other.lootok
        return uj
