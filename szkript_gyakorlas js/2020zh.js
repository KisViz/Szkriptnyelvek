function paritas(szoveg) {
    if (szoveg === "" || typeof szoveg !== "string") {
        return undefined;
    }

    szoveg = szoveg.split(";");
    let paros = 0, paratlan = 0;
    for (let elem of szoveg) {
        let adott = Number(elem);
        if (isNaN(adott)) {
            continue;
        }

        if (elem % 2 === 0) {
            paros++;
        } else {
            paratlan++;
        }
    }

    return {paros: paros,
            paratlan: paratlan};
}

// console.log(paritas('7;4;1;2;5'));
// console.log(paritas('10;20;30;40;50;60;70'));
// console.log(paritas(false));
// console.log(paritas(""));

class Laptop {
    constructor(marka, toltottseg = 50) {
        this.marka = marka;
        this._toltottseg = toltottseg;
        this.gamingLaptop = false;
    }

    get toltottseg() {
        return this._toltottseg;
    }

    set toltottseg(value) {
        this._toltottseg = Math.max(0, Math.min(value, 100));
    }

    programotFuttat(program) {
        if (program === "Skype" || program === "Discord" || program === "Chrome") {
            this.toltottseg -= 10;
        } else {
            this.toltottseg -= 3;
        }
    }

    gamingAtallit() {
        this.gamingLaptop = !this.gamingLaptop;
    }

    info() {
        return `${this.marka} laptop, toltottsege: ${this._toltottseg}, gaming laptop: ${this.gamingLaptop ? "igen" : "nem"}`
    }
}

let laptop = new Laptop("Lenovo", 80);
laptop.toltottseg = 30;
laptop.gamingAtallit();
console.log(laptop.info()); // Lenovo laptop, toltottsege: 30, gaming
// laptop: igen
laptop.programotFuttat("Discord");
laptop.programotFuttat("Counter Strike");
console.log(laptop.toltottseg); // 17