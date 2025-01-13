# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

#Team,FDCOUK,City,Stadium,Capacity,Latitude,Longitude,Country
#  0     1     2     3       4        5         6        7

def legnagyobb_stadion(utvonal: str):
    with open(utvonal, 'r') as file:
        tmp = file.readline()

        ures = False
        if not tmp:
            ures = True

        legtobb = 0
        legtobb_nev = ''
        legtobb_varos = ''
        for line in file:
            tmp = line.split(",")
            if int(tmp[4].strip()) > legtobb:
                legtobb = int(tmp[4].strip())
                legtobb_nev = tmp[3].strip()
                legtobb_varos = tmp[2].strip()


        with open("legnagyobb.txt", 'w') as ki:
            if ures or legtobb == 0:
                ki.write(f"Nincs (Nincs)\n")
            else:
                ki.write(f"{legtobb_nev} ({legtobb_varos})\n")

# legnagyobb_stadion("stadium.csv")

def osszes_arena(utvonal: str):
    with open(utvonal, 'r') as file:
        tmp = file.readline()

        uj = ["Stadium,City,Country,Big"]
        for line in file:
            tmp = line.split(",")
            if tmp[3].strip().endswith("Arena"):
                uj.append(f"{tmp[3].strip()},{tmp[2].strip()},{tmp[7].strip()},{int(tmp[4].strip()) > 50000}")

    with open("arena_park.csv", 'w') as ki:
        for line in uj:
            ki.write(line + "\n")

# osszes_arena("stadium.csv")

def osszes_park(utvonal: str):
    with open(utvonal, 'r') as file:
        tmp = file.readline()

        uj = []
        for line in file:
            tmp = line.split(",")
            if tmp[3].strip().endswith("Park"):
                uj.append(f"{tmp[3].strip()},{tmp[2].strip()},{tmp[7].strip()},{int(tmp[4].strip()) > 20000}")

    with open("arena_park.csv", 'a') as ki:
        for line in uj:
            ki.write(line + "\n")

# osszes_park("stadium.csv")

#Team,FDCOUK,City,Stadium,Capacity,Latitude,Longitude,Country
#  0     1     2     3       4        5         6        7
def varosok_szama(utvonal: str, *varos: str):
    if not varos:
        raise Exception("Nincs megadva egy orszag sem!")

    varosok = []

    for elem in varos:
        varosok.append(elem)

    dikt = {}
    with open(utvonal, 'r') as file:
        tmp = file.readline()

        for line in file:
            tmp = line.split(",")

            if tmp[7].strip() not in dikt:
                dikt[tmp[7].strip()] = [tmp[2].strip()]
            else:
                if tmp[2].strip() not in dikt[tmp[7].strip()]:
                    dikt[tmp[7].strip()].append(tmp[2].strip())

    with open("varosok.txt", 'w') as ki:
        for varos in varosok:
            ki.write(f"{varos} varosai:\n")

            for kulcs, ertek in dikt.items():
                if kulcs == varos:

                    for elem in sorted(ertek):
                        ki.write(f"\t{elem}\n")

            ki.write("----------\n")



# varosok_szama("stadium.csv", "Germany", "Spain", "Hungary", "Bela")

