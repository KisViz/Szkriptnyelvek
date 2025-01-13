# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def kerekit(szam):

    if int(szam) == szam:
        return int(szam)
    else:
        return int(szam) + 1


def szekem(sorfolyt):

    sor = kerekit(sorfolyt / 14)

    oldal = None
    if (sorfolyt % 14) > 7 or (sorfolyt % 14) == 0:
        oldal = "bal"
    else:
        oldal = "jobb"

    szam = None
    if oldal == "jobb":
        szam = -1 * ( (sorfolyt % 14) - 8)
    else:
        if sorfolyt % 14 != 0:
            szam = ((sorfolyt % 14) - 7)
        else:
            szam = 7


    return f"{sor}. sor, {oldal} {szam}. szek"

#------------------------------------------------------------------------

# for i in range(1,99):
#     print(szekem(i))