// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

function ragcsak(tomb, index) {
    if (tomb.length <= 1) {
        return undefined;
    }

    if (typeof index !== "number") {
        return null;
    }

    let uj = [];
    for (let i = index; i < tomb.length; i++) {
        uj.push(tomb[i]);
    }

    return uj.join("; ");
}

// console.log(ragcsak([],2))
// console.log(ragcsak(["ropi", "keksz"],"index"))
// console.log(ragcsak(["chips", "ropi", "nachos", "popcorn", "keksz"],2))

function egyetemistak(object) {
    const requiredProperties = ["nev", "eletkor", "informatikus_szakos", "programok"];

    for (let prop of requiredProperties) {
        if (!(prop in object)) {
            return `Nincs ${prop} property-je az egyetemistának!`;
        }
    }

    if (object.informatikus_szakos === false) {
        return {nev: object.nev, eletkor: object.eletkor,  informatikus_szakos: true, programok: object.programok};
    }

    if (object.programok.includes("kocsmázik") || object.programok.includes("romkocsmázik")) {
        return  `${object.nev}, aki ${object.eletkor} éves és informatika szakos, péntekenként sajnos tanulás helyett kocsmázik...`
    } else {
        return `${object.nev}, aki ${object.eletkor} éves és informatika szakos, péntekenként ${object.programok.join(", ")} és nem kocsmázik.`
    }
}

console.log(egyetemistak({nev: "Tibike", eletkor: 22, programok: ["tanul", "rajzol"]}))
console.log(egyetemistak({nev: "Tibike", eletkor: 22, informatikus_szakos: false, programok: ["tanul", "rajzol"]} ))
console.log(egyetemistak({nev: "Tibike", eletkor: 22, informatikus_szakos: true, programok: ["tanul", "rajzol"]}))