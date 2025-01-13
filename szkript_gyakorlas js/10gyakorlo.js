// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

class Hallgato {

    constructor(neptun, felev = 1) {
        this.neptun = neptun;
        this._felev = felev;
        this.jegyek = [];
    }


    get felev() {
        return this._felev;
    }

    set felev(value) {
        if (value > this._felev && Number.isInteger(value)) {
            this._felev = value;
        }
    }

    zarthelyi(nev, orak_szama) {
        if (nev === "kalkulus") {
            this.jegyek.push(1);
        } else {
            let jegy = Number.parseInt(Math.sqrt(this.felev * orak_szama));

            if (jegy <= 5) {
                this.jegyek.push(jegy);
            } else {
                this.jegyek.push(5);
            }
        }
    }

    felevVege() {
        let atlag = 0;

        if (this.jegyek.length > 0) {
            for (let jegy of this.jegyek) {
                atlag += jegy;
            }

            atlag = atlag / this.jegyek.length;
        }

        return `Neptun: ${this.neptun}, ${this.felev}. felev, ${atlag} atlag`
    }
}

// const hallgato = new Hallgato('NEP234');
// console.log(hallgato.felev); // 1
// hallgato.felev = 3;
// hallgato.zarthelyi('kalkulus', 4); // Kalkulusból 1-est kapott
// hallgato.zarthelyi('szkriptnyelvek', 6); // Itt 4-est kapott
// console.log(hallgato.felevVege()); // "Neptun: NEP234, 3. felev, 2.5 atlag"

class TTIKHallgato extends Hallgato {
    constructor(neptun, hAzonosito, felev = 1) {
        super(neptun, felev);
        this.hAzonosito = hAzonosito;
    }

    zarthelyi(nev, orak_szama) {
        if (nev === "kalkulus") {
            this.jegyek.push(5);
        } else {
            let jegy = Number.parseInt(Math.sqrt(this.felev * orak_szama));

            if (jegy <= 5) {
                this.jegyek.push(jegy);
            } else {
                this.jegyek.push(5);
            }
        }
    }

    felevVege() {
        let atlag = 0;

        if (this.jegyek.length > 0) {
            for (let jegy of this.jegyek) {
                atlag += jegy;
            }

            atlag = atlag / this.jegyek.length;
        }

        return `Neptun: ${this.neptun}, ${this.felev}. felev, ${atlag} atlag (h: ${this.hAzonosito})`
    }
}