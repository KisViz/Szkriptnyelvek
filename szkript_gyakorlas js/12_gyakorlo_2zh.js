// Név: Tóth-Viizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

function cimkez(azon) {
    if (typeof azon !== 'string') {
        return "";
    }

    azon = azon.split("_");

    if (azon.length > 1 && azon[0] === "x1") {
        vege = [];
        for (let i = 0; i < azon.length; i++) {
            if (i % 2 === 1) {
                vege.push(azon[i]);
            }
        }
        return vege.join(" ");
    }

    if (azon.length > 1 && azon[0] === "x2") {
        azon[0] = "akcio"
        return azon.join(" ");
    }

    return azon.join("_").toUpperCase();
}

// console.log(cimkez('x1_uj_botmixer_szett')); // "uj szett"
// console.log(cimkez('x2_gumilabda_pottyos')); // "akcio gumilabda pottyos"
// console.log(cimkez('teli_bakancs')); // "TELI_BAKANCS"
// console.log(cimkez(42)); // ""

function atlag(tomb, korl) {
    if (!(Array.isArray(tomb)) || tomb.length === 0) {
        return null;
    }

    let szaml = 0;
    for (let elem of tomb) {
        if (Math.abs(elem) <= korl) {
            szaml += Math.abs(elem);
        } else {
            szaml += korl;
        }
    }

    return Math.round(szaml / tomb.length);
}

// console.log(atlag([1, -3, 4], 3)); // 2
// console.log(atlag([2, -3, 4], 3)); // 3
// console.log(atlag([-3, 0, -4, 9], 1)); // 1
// console.log(atlag(4, 7)); // null

class Mozi {
    constructor(nev, ferohely = 50, nyitva = false) {
        this.nev = nev;
        this.ferohely = ferohely;
        this._nyitva = nyitva;
        this.musor = {};
    }


    get nyitva() {
        return this._nyitva;
    }

    set nyitva(value) {
        if (value && this.musor.hasOwnProperty("hetfo")) {
            this._nyitva = true;
        } else {
            this._nyitva = false;
        }
    }

    google() {
        if (this.nyitva) {
            let napok = Object.keys(this.musor).join(" ");
            return `${this.nev} mozi: ${this.ferohely} ferohely, ${napok} napokon nyitva`
        } else {
            return `${this.nev} mozi: ${this.ferohely} ferohely, jelenleg zarva`
        }
    }

    ujFilm(nap, cim) {
        this.musor[nap] = cim;
    }

    bevetel(ar) {
        if (!this._nyitva) {
            return 0;
        }

        let szaml = 0;
        for (let elem in this.musor) {
            let hossz = this.musor[elem].length;
            let napi = elem === "pentek" ? ar * 0.8 : ar;
            szaml += (this.ferohely - hossz) * napi;
        }

        return szaml;
    }


    felujit() {
        this.nyitva = false;
        this.ferohely = Math.floor(this.ferohely * 1.3);
        let elsonap = Object.keys(this.musor)[0];
        delete this.musor[elsonap];
    }
}


// let m = new Mozi('Belvarosi', 40);
// m.ujFilm('szerda', 'Deadpool & Wolverine');
// m.ujFilm('hetfo', 'Lego movie');
// m.nyitva = true;
// console.log(m.musor); // { szerda: 'Deadpool & Wolverine', hetfo: 'Lego movie' }
// console.log(m.bevetel(200)); // 9600
// m.felujit();
// m.ujFilm('kedd', 'Garfield movie');
// m.ujFilm('pentek', 'Zootopia 2');
// m.nyitva = true;
// console.log(m.google()); // "Belvarosi mozi: 52 ferohely, hetfo kedd pentek
// // napokon nyitva"
// console.log(m.bevetel(200)); // 22720