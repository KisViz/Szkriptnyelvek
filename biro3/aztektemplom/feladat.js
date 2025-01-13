function toronyMegnyito() {
    console.log("A torony elkeszult!")
}
// toronyMegnyito()

function epites(szam) {
    if (typeof(szam) == "number") {
        for (let i = 0; i < szam; i++) {
            console.log("*epit*")
        }
    }
}

// epites(3)
// epites("asd")

function szemuvegVasar(hany, nem, bevetel) {
    return parseInt(nem) * parseInt(bevetel);
}

// console.log(szemuvegVasar(2, 2.5, 9.9999))

function karbecsles(szoveg) {
    let szank= 0
    for (let i of szoveg) {
        if (parseInt(i) === 1) {
            szank++
        }
    }

    return szank;
}

// console.log(karbecsles("001100010"))

function templomEpites(hosszu, tomor, terv) {
    if(terv === undefined) {
        return undefined
    }

    if (terv.length < 10) {
        return false;
    }

    let hsz = 0, tsz = 0;

    for (let elem of terv) {
        if (elem.toUpperCase() === "H") {
            hsz++;
        } else if (elem.toUpperCase() === "T") {
            tsz++;
        }
    }

    // console.log(tsz, hsz)
    // console.log(tomor >= tsz)
    // console.log(hosszu, hsz, hosszu >= hsz)
    return (tomor >= tsz && hosszu >= hsz)
}

// console.log(templomEpites(9, 4, "HHTHtQtHhhPTHH"))

function celpont(szoveg) {
    return (szoveg.includes("acelcipo") || szoveg.includes("boxkesztyu") || szoveg.includes("hegedu"))
}

// console.log(celpont("kes, szablya, pisztoly, atombomba, granat"))
// console.log(celpont("hegedutok-autogumi-ragaszto-ollo"))

function templomot_megved(erkezok, aiModell) {
    const bemenet = erkezok.trim();

    const aiEredmeny = aiModell(bemenet);

    if (
        aiEredmeny.startsWith('L') ||
        aiEredmeny.endsWith('L') ||
        aiEredmeny.includes('L4N70K') ||
        (aiEredmeny.endsWith('L4N7') && aiEredmeny.startsWith('0K'))
    ) {
        return true;
    }

    return false;
}
