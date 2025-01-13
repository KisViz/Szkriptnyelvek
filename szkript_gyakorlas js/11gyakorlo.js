function isDisarium(ertek) {
    if (typeof ertek !== "number" || ertek < 0) {
        return undefined;
    }

    let szaml = 0;
    for (let i = 1; i <= ertek.toString().length; i++) {
        szaml += Math.pow(Number(ertek.toString()[i - 1]), i);
        // console.log(szaml);
    }

    return szaml === ertek;
}

// console.log(isDisarium(175));
// console.log(isDisarium(42));

function letterCombinations(digits) {
    if (typeof digits !== 'string' || !/^[2-9]+$/.test(digits)) {
        return [];
    }

    const phoneMap = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    };

    const combinations = (index, path) => {
        if (index === digits.length) {
            return [path];
        }

        const letters = phoneMap[digits[index]];
        let result = [];
        for (const letter of letters) {
            result = result.concat(combinations(index + 1, path + letter));
        }
        return result;
    };

    return combinations(0, '');
}

//nem en irtam meg
console.log(letterCombinations('532'));

class Savanyusag {


    constructor(minosegetMegorzi, nyitva, hozzavalok) {
        this.minosegetMegorzi = minosegetMegorzi;
        this.nyitva = nyitva;
        this.hozzavalok = hozzavalok;

        this._tipus = hozzavalok[0];
        for (let elem of hozzavalok) {
            if (elem !== this._tipus) {
                this._tipus = "csalamade";
                break
            }
        }
    }


    get tipus() {
        return this._tipus;
    }

    set tipus(value) {
        if (this.hozzavalok.includes(value)) {
            this._tipus = value;
        }
    }

    szavatos(ev, honap, nap) {
        let uj = ev * 365 + honap * 28 + nap;
        let jelenlegi = this.minosegetMegorzi[0] * 365 + this.minosegetMegorzi[1] * 28 + this.minosegetMegorzi[2]
        return jelenlegi > uj;
    }

    fedeletElcsavar() {
        this.nyitva = !this.nyitva;
    }

    osszeont(savanyusag) {
        if (!(savanyusag instanceof Savanyusag)) {
            return "HIBA! Nem savanyusag!";
        }

        if (!savanyusag.nyitva || !this.nyitva) {
            return "HIBA! A savanyusag fedele zarva van!"
        }

        for (let elem of savanyusag.hozzavalok) {
            this.hozzavalok.push(elem);
        }

        if (!(this.szavatos(savanyusag.minosegetMegorzi))) {
            this.minosegetMegorzi = savanyusag.minosegetMegorzi;
        }

        this._tipus = this.hozzavalok[0];
        for (let elem of this.hozzavalok) {
            if (elem !== this._tipus) {
                this._tipus = "csalamade";
                break
            }
        }

        return "Savanyusagok osszeontve!"
    }

    info() {
        return `Savanyitott ${this.tipus}, aminek a fedele ${this.nyitva ? "nyitva" : "zarva"}`
    }

    hozzavalokatTobbszoroz(szam) {
        let uj = [];
        for (let elem of this.hozzavalok) {
            for (let i = 0; i < szam; i++) {
                uj.push(elem);
            }
        }

        this.hozzavalok = uj;
    }
}