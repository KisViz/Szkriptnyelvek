function atszallasokSzama(str) {
    if (str.split(',').length < 2) {
        return 0;
    }
    return (
        str.split(',').length - 2
    )
}

// console.log(atszallasokSzama('Budapest, Owando'))

function koltes(tomb) {
    let szaml = 0;

    for (let elem of tomb) {
        if (typeof elem === 'number') {
            szaml += elem;
        }
    }

    return szaml;
}

// console.log(koltes([5000, 1500, "cica", 520, "400", 1000]))
// console.log(koltes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

function poszt(tomb, celpont) {
    tomb.push(celpont);
    tomb.unshift(celpont);
    return tomb;
}

// console.log(poszt(["Híres piac", "Kicsi Piramis"], "Járdasziget"));

function kigyoFight(obj) {
    let szaml = 0;
    let nev = '';

    for (let elem in obj) {
        if (obj[elem] > szaml) {
            szaml = obj[elem];
            nev = elem;
        }
    }

    return nev;
}

/*console.log(kigyoFight({
    bemelegites: 2,
    wave1: 11,
    wave2: 20,
    ultimate_wave: 33,
    wave4: 21,
    final_wave: 15
}))*/

function minimalisHadsereg(obj) {
    let tomb = [];

    for (let elem in obj) {
        tomb.push(Math.sqrt(obj[elem]));
    }

    let szaml = 1;

    for (let elem of tomb) {
        szaml *= elem;
    }

    return Math.ceil(szaml);
}

/*console.log(minimalisHadsereg({
    Dora: 6,
    Fanni: 17,
    Krisztina: 5,
    Dorottya: 3
}))*/

function pokgyujtes(obj) {
    let szaml = 0;

    for (let elem in obj) {
        szaml += Math.min(...obj[elem]);
    }

    return szaml;
}

// console.log(Math.min(...[5, 7, 3, 8]))

/*console.log(pokgyujtes({
    aranyhomokPiramis: [5, 7, 3, 8],
    smaragdcsucsPiramis: [7, 5, 7, 4],
    sarkanyszemPiramis: [5],
    rubinboritasuPiramis: [1, 1, 1, 1]
}))*/

function bemutatkozas(tomb) {
    tomb.sort();
    return tomb.join(', ');
}

// console.log(["Krisztina", "Dora", "Fanni", "Dorottya"].sort())
// console.log(bemutatkozas(["Krisztina", "Dora", "Fanni", "Dorottya"]))