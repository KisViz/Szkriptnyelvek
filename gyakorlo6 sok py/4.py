# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

class Konyv():
    def __init__(self, _cim: str, _oldalszam: int = 100):
        self._cim = _cim
        self._oldalszam = _oldalszam

    @property
    def cim(self):
        return self._cim

    @property
    def oldalszam(self):
        return self._oldalszam

    @oldalszam.setter
    def oldalszam(self, _oldalszam):
        self._oldalszam = _oldalszam

class Kategoria():
    def __init__(self, nev):
        self._nev = nev
        self.konyvek = []

    def __iadd__(self, other: Konyv):
        if not isinstance(other, Konyv):
            raise TypeError("A kategóriába csak könyvek kerülhetnek!")
        elif other.oldalszam < 100:
            raise ValueError("Csak megfelelő hosszúságú könyvek kerülhetnek be!")
        else:
            self.konyvek.append(other)
        return self

    @property
    def nev(self):
        return self._nev


def kiemelkedo_konyvek(kategoriak: list[Kategoria]):
    lista = []

    for elem in kategoriak:
        # print(elem.konyvek)
        for konyv in elem.konyvek:

            # print(elem.nev,len(elem.konyvek),[konyv._cim for konyv in elem.konyvek])
            if konyv.oldalszam >= 200 and len(elem.konyvek) > 1:
                lista.append(konyv)

    return lista

class SemmiNemMaradtAKonyvtarban(Exception):
    def __init__(self):
        super().__init__(" Minden könyv kiesett.")

def statisztika(adatok: list):
    lista = []

    for elem in adatok:
        if elem[2] not in lista:
            lista.append(Kategoria(elem[2]))

        try:
            for kateg in lista:
                if kateg.nev == elem[2]:
                    kateg += Konyv(elem[0], elem[1])
        except Exception:
            continue

    vege = kiemelkedo_konyvek(lista)
    if len(vege) == 0:
        raise SemmiNemMaradtAKonyvtarban()

    return vege


# k1 = Konyv("A Gyűrűk Ura", 450)
# k2 = Konyv("Harry Potter", 300)
# k3 = Konyv("Rövid regény", 80)
# k4 = Konyv("Mert többen nincsenek")
#
# kat = Kategoria("Fantasy")
# kat += k1
# kat += k2
# kat += k4
# # print(kat) # Output: A Gyűrűk Ura, Harry Potter
#
# kategoriak = [kat]
# kiemeltek = kiemelkedo_konyvek(kategoriak)
# for konyv in kiemeltek:
    # print(konyv.cim) # Output: A Gyűrűk Ura, Harry Potter

# adatok = [
# ("Könyv1", 150, "Tudomány"),
# ("Könyv2", 180, "Irodalom"),
# ("Könyv3", 200, "Tudomány"),
# ("Könyv4", 220, "Irodalom"),
# ("Könyv5", 80, "Művészet"), # Túl rövid, nem kerül be
# ]
#
# # for elem in adatok:
# #     print(elem)
# vege = statisztika(adatok)
#
# for elem in vege:
#     print(elem.cim)