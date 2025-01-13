# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

def nyertes_korok(adam, ellenfel):
    if (len(adam) != len(ellenfel)) or (not adam or not ellenfel):
        return -1
    else:
        adam_nyert = 0
        for i in range(0,len(adam)):
            if adam[i] > ellenfel[i]:
                adam_nyert += 1

    return adam_nyert