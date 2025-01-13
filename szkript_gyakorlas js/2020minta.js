function tokeletes(szam) {
    if (typeof szam !== "number") {
        return false;
    }

    let szaml = 0;
    for (let i = 1; i < szam ; i++) {
        if (szam % i === 0) {
            szaml += i;
        }
    }

    return szaml === szam;
}

// console.log(tokeletes(6)) // true
// console.log(tokeletes(28)) // true
// console.log(tokeletes(16)) // false
// console.log(tokeletes("szoveg")) // false

class Webbongeszo {
    constructor(memoria = 8192) {
        this.lapok = [];
        this.memoria = memoria;
        this._memoria_fogysztas = 0;
    }


    get memoria_fogysztas() {
        return this._memoria_fogysztas;
    }

    set memoria_fogysztas(value) {
        this._memoria_fogysztas = Math.max(0,Math.min(this.memoria, value));
    }

    ujLap(url) {
        this.lapok.push(url);
        this.memoria_fogysztas += Math.floor(Math.random() * (1500 - 100 + 1)) + 100;
    }

    lapBezar() {
        this.lapok.pop();
        this.memoria_fogysztas -= Math.floor(Math.random() * (1000 - 30 + 1)) + 30;
    }

    panik() {
        this.lapok = [];
        this.memoria_fogysztas = 10;
    }
}

function tesztWebbongeszo() {
    // Tesztesetek Webbongeszo osztályhoz
    const bongeszo = new Webbongeszo();

// Kezdő állapot
    console.log("Kezdeti állapot:");
    console.log("Lapok:", bongeszo.lapok);
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

// Új lap hozzáadása
    bongeszo.ujLap("https://example.com");
    console.log("\n1. Lap hozzáadása:");
    console.log("Lapok:", bongeszo.lapok);
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

    bongeszo.ujLap("https://another-example.com");
    console.log("\n2. Lap hozzáadása:");
    console.log("Lapok:", bongeszo.lapok);
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

// Lap bezárása
    bongeszo.lapBezar();
    console.log("\n1. Lap bezárása:");
    console.log("Lapok:", bongeszo.lapok);
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

// Pánik gomb
    bongeszo.panik();
    console.log("\nPánik gomb lenyomása:");
    console.log("Lapok:", bongeszo.lapok);
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

// Szélsőséges memóriafogyasztás beállítása
    bongeszo.memoria_fogysztas = -500; // Teszt negatív érték
    console.log("\nNegatív memóriafogyasztás beállítása:");
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

    bongeszo.memoria_fogysztas = 10000; // Teszt túl nagy érték
    console.log("\nTúl nagy memóriafogyasztás beállítása:");
    console.log("Memóriafogyasztás:", bongeszo.memoria_fogysztas);

}

// Tesztelés futtatása
// tesztWebbongeszo();
