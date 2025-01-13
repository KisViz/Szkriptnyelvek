def beolvas(utvonal):
    kulcsok=""
    sor=""
    lista_ki=[]
    with open(utvonal,"r",encoding='utf-8') as file:
        kulcsok = file.readline().strip().split(',')
        #print(kulcsok)
        for sor in file:
            sor=sor.strip().split(',')
            for i in range(len(sor)):
                sor[i]=sor[i].strip()
            #print(sor)
            dikt={}
            dikt["Team"]=sor[0]
            dikt["FDCOUK"] = sor[1]
            dikt["City"] = sor[2]
            dikt["Stadium"] = sor[3]
            dikt["Capacity"] = sor[4]
            dikt["Latitude"] = sor[5]
            dikt["Longitude"] = sor[6]
            dikt["Country"] = sor[7]
            #print(dikt)
            lista_ki.append(dikt)
    #print("\n\n")
    #print(lista_ki)
    return lista_ki

def legnagyobb_stadion(utvonal):
    lista=beolvas(utvonal)
    #print(lista)
    maxi=0
    nev=""
    varos=""
    with open("tamas.txt","w",encoding='utf-8') as file:
        for stadion in lista:
            if int(stadion["Capacity"])>maxi:
                maxi=int(stadion["Capacity"])
                nev=stadion["Stadium"]
                varos=stadion["City"]
        if maxi==0:
            print("Nincs (Nincs)",file=file)
        else:
            print(f"{nev} ({varos})",file=file)

def osszes_arena(utvonal):
    lista=beolvas(utvonal)
    with open("tamas_park.csv","w",encoding='utf-8') as file:
        print("Stadium,City,Country,Big",file=file)
        for stadion in lista:
            if stadion['Stadium'].endswith("Arena"):
                nagy=True
                if int(stadion["Capacity"])>50000:
                    nagy=True
                else:
                    nagy=False
                print(f"{stadion['Stadium']},{stadion['City']},{stadion['Country']},{nagy}",file=file)

def osszes_park(utvonal):
    lista=beolvas(utvonal)
    with open("tamas_park.csv","a",encoding='utf-8') as file:
        for stadion in lista:
            if stadion['Stadium'].endswith("Park"):
                nagy = True
                if int(stadion["Capacity"]) > 20000:
                    nagy = True
                else:
                    nagy = False
                print(f"{stadion['Stadium']},{stadion['City']},{stadion['Country']},{nagy}", file=file)

def varosok_szama(utvonal, *orszagok):
    lista=beolvas(utvonal)
    if len(orszagok)==0:
        raise Exception("Nincs megadva egy orszag sem!")
    with open("tamas_varosok.txt","w",encoding='utf-8') as file:
        for orszag in orszagok:
            print(f"{orszag} varosai:",file=file)
            tomb = []
            for stadion in lista:
                if stadion['Country']==orszag:
                    if stadion['City'] not in tomb:
                        tomb.append(stadion['City'])
            tomb.sort()
            for varos in tomb:
                print(f"\t{varos}",file=file)
            print("----------",file=file)



legnagyobb_stadion("stadium.csv")
osszes_arena("stadium.csv")
osszes_park("stadium.csv")
varosok_szama("stadium.csv", "Germany", "Spain", "Hungary")
