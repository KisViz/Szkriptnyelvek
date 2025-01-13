// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

function lama(nev, kor = 5) {
    if (nev === undefined) {
        return "Nincsen neve szegény párának!";
    }

    if (nev.endsWith("láma")) {
        return  "Ez egy igazi láma!";
    }

    if (kor <= 2) {
        return  `${nev} még gyerek, csak ${kor} éves!`
    }

    if (kor >= 15) {
        return `${nev} már egy bölcs öreg, megérte ${kor} éves kort!`
    }

    for (let i = 0; i < kor; i++) {
        nev += "láma"
    }

    return `${nev} egy igazi láma lett!`
}

console.log(lama("Kiraláma"))
console.log(lama("Kira", 2))
console.log(lama("Kira"))