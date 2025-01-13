def bolygo(lista):
    return len(lista)

def kalozok(lista):

    for i in range(len(lista)):
        lista[i] += ", a veszedelmes"

def benepesites(lista):
    dikt = {}

    for i in range(len(lista)):
        valasztott = lista[i].split(";")
        dikt[valasztott[1]] = 0

    for i in range(len(lista)):
        valasztott = lista[i].split(";")
        dikt[valasztott[1]] += 1
    return dikt

def csata(lista):
    uj = []
    for i in range(1,len(lista),2):
        uj.append(lista[i])
    return uj

def verseny(lista):
    dikt = {}

    for i in range(len(lista)):
        dikt[lista[i]] = 0

    for i in range(len(lista)):
        dikt[lista[i]] += 1

    szaml = 0
    for elem in dikt.values():
        if elem == 2:
            szaml += 1

    return szaml

def foci(dikt):
    gyartasiSzam = ""
    legugyesebb = -1

    for szam, lista in dikt.items():
        lista.remove(max(lista))
        lista.remove(min(lista))

        szaml = 0
        for elem in lista:
            szaml += elem

        szaml = szaml / len(lista)

        if szaml > legugyesebb:
            legugyesebb = szaml
            gyartasiSzam = szam

    return gyartasiSzam


# nevek = { "KX8-3YZ6": [0.17, 0.88, 0.53, 0.63], "VF3-1XJ7": [0.55, 0.74, 0.23, 0.11], "SD1-7MV8": [0.54, 0.99, 0.53, 0.51, 0.54] }
# print(foci(nevek))