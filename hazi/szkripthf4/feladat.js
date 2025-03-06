// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

class Nyuszi {

    constructor(repa = 0) {
        this._repa = repa;
        this.vendegek = [];
    }

    get repa() {
        return this._repa;
    }

    ultet(repa = 1) {
        this._repa += repa;
    }

    vendeg(vendeg) {
        if (typeof vendeg === 'string') {
            this.vendegek.push(vendeg);
        }
    }

    etet() {
        while (this.vendegek.length > 0 && this._repa > 0) {
            this._repa--;
            this.vendegek.shift();
        }
    }
}


/*// nincs répája Nyuszinak.
var nyusz = new Nyuszi(0);
//ültet egy répát.
nyusz.ultet(2);
console.log(nyusz.repa); // 1.
console.log(nyusz.vendegek); //még nincs vendége az eredmény [].
// nyusz.vendeg('Robert Gida'); // Róbert Gida megérkezik Nyuszihoz.
nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
console.log(nyusz.vendegek); //['Robert Gida', 'Malacka']
nyusz.etet(); // Mivel van egy 1 répa, Robert Gida kap egyet és utána haza megy.
// Malackának már nem jutott répa, ezért neki várnia kell.
console.log(nyusz.repa) // 0
console.log(nyusz.vendegek); // ['Malacka']*/
