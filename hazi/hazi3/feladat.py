# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def hogolyo_csata(lista: list):
    stat = {}
    for kor in lista:
        for jatekos, adatok in kor.items():
            if jatekos not in stat:
                stat[jatekos] = {
                    'eldobott_hogolyok': 0,
                    'talalt': 0,
                    'fejtalalat': 0
                }

            stat[jatekos]['eldobott_hogolyok'] += adatok.get('eldobott_hogolyok', 0)
            stat[jatekos]['talalt'] += adatok.get('talalt', 0)
            stat[jatekos]['fejtalalat'] += adatok.get('fejtalalat', 0)

    return stat

def hogolyo_pontossag(stat: dict):
    for nev, adatok in stat.items():
        if adatok['eldobott_hogolyok'] > 0:
            stat[nev]['pontossag'] = adatok.get('talalt') / adatok.get('eldobott_hogolyok')
        else:
            stat[nev]['pontossag'] = 0

    return stat

def hogolyo_piros_lap(stat: dict):
    piroslap = []
    for nev, adatok in stat.items():
        fejtarany = adatok.get('fejtalalat') / adatok.get('talalt') if adatok.get('talalt') > 0 else 0
        if adatok.get('pontossag') >= 0.7 and  fejtarany >= 0.5:
            piroslap.append(nev)

    return piroslap