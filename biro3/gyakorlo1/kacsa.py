def kacsak():
    print("kacsaaaaaak!!!")

def kacsava_valas(ertek):
    if ertek:
        print("Kacsava valas sikeres!")
    else:
        print("Kacsava valas egyelore varat magara!")

def uszoverseny(en, mozes):
    if en > mozes:
        print("Az uj kacsa diadalmaskodott")
    elif en < mozes:
        print("Mozes uszasban verhetetlen")
    else:
        print("Mindket kacsa egyforman jo uszo")

def kenyerboss():
    ero = int(input())
    kitartas = int(input())
    intelligencia = int(input())

    return ero + kitartas + intelligencia

def csali(ut):
    if type(ut) == str:
        return len(ut)
    else:
        return None

def lakoma():
    fej = int(input())
    test = int(input())
    kar = int(input())
    lab = int(input())

    lab = lab * 2
    kar = kar * 2

    maxTerfogat = max(fej,test,kar,lab)

    if maxTerfogat == fej:
        return "fej"
    elif maxTerfogat == test:
        return "test"
    elif maxTerfogat == kar:
        return "kar"
    else:
        return "lab"

