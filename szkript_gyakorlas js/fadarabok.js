function multFelidezes(fadarabok, uj_fadarab, fgv) {
    fadarabok.push(uj_fadarab);
    fgv(fadarabok);
}

class Fadarab {
    constructor(szin, nev, emlekek = []) {
        this._szin = szin;
        this._nev = nev;
        this._emlekek = emlekek;
    }


    get szin() {
        return this._szin;
    }

    set szin(value) {
        this._szin = value;
    }

    get nev() {
        return this._nev;
    }

    set nev(value) {
        this._nev = value;
    }

    get emlekek() {
        return this._emlekek;
    }

    emleketHozzaad(emlek) {
        // if (emlek instanceof Array) ...
        if (Array.isArray(emlek)) {
            for (let elem of emlek) {
                this._emlekek.push(elem);
            }
        } else {
            this._emlekek.push(emlek);
        }
    }

    emlekekSzama(emlek_tipus) {
        let szaml = 0;
        for (let elem of this._emlekek) {
            if (elem.tipus === emlek_tipus) {
                szaml++;
            }
        }
        return szaml;
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