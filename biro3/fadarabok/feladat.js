function multFelidezes(tomb, uj_fa, fgv) {
    tomb.push(uj_fa);
    fgv(tomb)
}

class Fadarab {
    constructor(szin, nev, emlekek = []) {
        this._nev = nev;
        this._szin = szin;
        this._emlekek = emlekek;
    }

    get nev() {
        return this._nev;
    }

    set nev(value) {
        this._nev = value;
    }

    get szin() {
        return this._szin;
    }

    set szin(value) {
        this._szin = value;
    }

    get emlekek() {
        return this._emlekek;
    }

    emleketHozzaad(emlekek) {
        if (emlekek instanceof Array) {
            for (let emlek of emlekek) {
                this._emlekek.push(emlek);
            }
        } else {
            this._emlekek.push(emlekek);
        }
    }

    emlekekSzama(emlek_tipus) {
        let szama = 0;
        for (let emlek of this._emlekek) {
            if (emlek.tipus === emlek_tipus) {
                szama++;
            }
        }
        return szama;
    }
}

class FadarabCsoport {
    constructor(nev, fa) {
        this.nev = nev;
        this._tagok = new Map();
        this._tagok.set("aldozofa", fa);
    }

    get nev() {
        return this._nev;
    }

    set nev(value) {
        this._nev = value[0].toUpperCase() + value.slice(1);
    }

    munkakor(kor) {
        return this._tagok.has(kor) ? this._tagok.get(kor).nev : undefined;

    }

    termeszetiJeloles(fa, munka) {
        if (typeof fa !== "object" || fa === null || typeof fa.nev !== "string") {
            console.log("A fadarab sajnos nem ert ide idoben, mert egy farkas megragcsalta.");
        } else {
            this._tagok.set(munka, fa);
        }
    }

    termeszetiRituale(munka) {
        if (munka === "aldozofa") {
            console.log("nem-nem, rossz kisfiu!");
        } else if (this._tagok.has(munka)) {
            this._tagok.delete(munka);
        }
    }
}

class FenyofadarabCsoport extends FadarabCsoport {}