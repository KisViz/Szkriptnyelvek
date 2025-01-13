function toronyMegnyito() {
    console.log("A torony elkeszult!");
}

function epites(szam) {
    if (typeof szam === "number") {
        for (let i = 0; i < szam; i++) {
            console.log("*epit*");
        }
    }
}

function szemuvegVasar(emberszam, nemvetteeszre, bevetelszem) {
    return Math.floor(nemvetteeszre) * Math.floor(bevetelszem);
}

function karbecsles(string) {
    let szaml = 0;
    for (let elem of string) {
        if (elem === "1") {
            szaml++;
        }
    }
    return szaml;
}

function templomEpites(hosszu, tomor, terjvrajz) {
    if (terjvrajz === undefined) {
        return undefined;
    }

    let H = 0, T = 0;
    for (let elem of terjvrajz) {
        if (elem.toUpperCase() === "H") {
            H++;
        } else if (elem.toUpperCase() === "T") {
            T++;
        }
    }

    return terjvrajz.length > 10 && H <= hosszu && T <= tomor;
}

function celpont(targyak) {
    return (targyak.includes("acelcipo") || targyak.includes("boxkesztyu") || targyak.includes("hegedu"));
}

// console.log(celpont("kes, szablya, pisztoly, atombomba, granat"));
// console.log(celpont("hegedutok-autogumi-ragaszto-ollo"));

function templomot_megved(adatok, AI) {
    let uj = AI(adatok.trim());

    let dupla = uj + uj;

    return ((uj.startsWith("L") || uj.endsWith("L")) && dupla.includes("L4N70K"))
}