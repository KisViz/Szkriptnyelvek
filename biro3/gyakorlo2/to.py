def figyelmeztetes():
    print("VIGYAZZ!")

def hangok(hanyszor):
    print("FORDULJ VISSZA!\n" * hanyszor)

def kabat(taska):
    return "kabat" in taska

def vizen_jaras(viz):
    if type(viz) != str:
        return False


    tilde = 0

    for elem in viz:
        if elem == '~':
            tilde += 1

    return tilde * 2 >= len(viz)

def meow_szobor(szoveg, kisbetuE = False):
    if kisbetuE:
        szoveg = szoveg[::-1]
        return szoveg.lower()
    else:
        return szoveg[::-1]

def tunderek(csapatok):
    szaml = 0
    for elem in csapatok:
        szaml += int(elem)

    return szaml

def csapdak(hossz, tavolsag):
    hossz = hossz * 100

    lista = [150]
    hossz -= 150

    for elem in range(hossz // tavolsag):
        lista.append(lista[-1] + tavolsag)

    return lista

def templomtanc(lista):
    if lista is None:
        return []

    uj = []

    for elem in lista:
        if elem [0:5] == "szent":
            uj.append(elem.strip())

        elif len(elem) >= 5:
            ujszo = ""
            for betu in elem:
                if betu not in "öüóeuioőúűaéáí":
                    ujszo += betu
            uj.append(ujszo)

    uj.sort()
    return uj



# print("szent" == "szent kenyér"[0:5])
# print(100 // 150)
# print(100 % 150)