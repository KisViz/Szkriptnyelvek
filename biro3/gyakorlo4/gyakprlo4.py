class Idogep():
    def __init__(self, vissza_ido = 1000):
        self.vissza_ido = vissza_ido

    def __str__(self):
        return f"Az idogep ennyit fog visszautazni az idoben: {self.vissza_ido}"

class Dinoszaurusz():
    def __init__(self, _fajta: str, _magassag):
        self._fajta = _fajta
        if _magassag < 0:
            self._magassag = _magassag * -1
        else:
            self._magassag = _magassag

        if _fajta[-3:] == "rex" or _magassag > 500:
            self._veszelyes = True
        else:
            self._veszelyes = False

    @property
    def fajta(self):
        return self._fajta

    @fajta.setter
    def fajta(self, _fajta):
        self._fajta = _fajta

    @property
    def magassag(self):
        return self._magassag

    @magassag.setter
    def magassag(self, _magassag):
        if _magassag > 0:
            self._magassag = _magassag

    @property
    def veszelyes(self):
        return self._veszelyes

    @veszelyes.setter
    def veszelyes(self, _veszelyes):
        self._veszelyes = _veszelyes

    def __iadd__(self, other: int):
        self._magassag += other
        return self

    def __eq__(self, other):
        if not isinstance(other, Dinoszaurusz):
            return False
        else:
            return self._magassag == other._magassag and self._veszelyes == other._veszelyes and self._fajta == other._fajta

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

    def targyat_elrak(self, loot):
        if loot.meret <= self.kpacitas:
            self.lootok.append(loot)
            self.kpacitas -= loot.meret




idoggep = Idogep(70000000)