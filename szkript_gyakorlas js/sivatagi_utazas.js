function atszallasokSzama(varosok) {
    if (varosok.split(", ").length < 2) {
        return 0;
    } else {
        return varosok.split(', ').length - 2;
    }
}

// console.log(atszallasokSzama("BudapeBudapest, Tebriz, Pleiku, Drezda, Owandost, Tebriz, Pleiku, Drezda, Owando"))
// console.log(atszallasokSzama("BudapeBudapest, Owando"))

function koltes(tomb) {
    let szml = 0;
    for (let elem of tomb) {
        if (typeof elem === "number") {
            szml += elem;
        }
    }

    return szml;
}

// console.log(koltes(([5000, 1500, "cica", 520, "400", 1000])))

function poszt(tomb, celpont) {
    tomb.push(celpont);
    tomb.unshift(celpont);

    // console.log(tomb);
}

// poszt(["Híres piac", "Kicsi Piramis"], "Járdasziget")

function kigyoFight(object) {
    let nev = "", szam = 0;

    for (let elem in object) {
        if (object[elem] > szam) {
            nev = elem;
            szam = object[elem];
        }
    }

    return nev;
}

/*
console.log(kigyoFight({
    bemelegites: 2,
    wave1: 11,
    wave2: 20,
    ultimate_wave: 33,
    wave4: 21,
    final_wave: 15
}))*/

function minimalisHadsereg(object) {
    let szaml = 1;
    for (let elem in object) {
        szaml *= Math.sqrt(object[elem]);
    }

    return Math.ceil(szaml);
}

/*
console.log(minimalisHadsereg({
    Dora: 6,
    Fanni: 17,
    Krisztina: 5,
    Dorottya: 3
}))*/

function pokgyujtes(object) {
    let szaml = 0;
    for (let elem in object) {
        szaml += Math.min(...object[elem]);
    }

    return szaml;
}

// console.log(Math.min([5, 7, 3, 8]))
// console.log(Math.min(...[5, 7, 3, 8]))
// console.log(Math.min(5, 7, 3, 8))


/*
console.log(pokgyujtes({
    aranyhomokPiramis: [5, 7, 3, 8],
    smaragdcsucsPiramis: [7, 5, 7, 4],
    sarkanyszemPiramis: [5],
    rubinboritasuPiramis: [1, 1, 1, 1]
}))*/

function bemutatkozas(nevek) {
    return nevek.sort().join(", ");
}

// console.log(bemutatkozas(["Budapest", "Piramis", "Budapest"]))
// console.log(bemutatkozas(["Krisztina", "Dora", "Fanni", "Dorottya"]))