// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

function matek(param) {
    if (param === undefined) {
        return 0;
    }

    if (typeof param === "string") {
        return 1;
    }

    if (Number.isInteger(param)) {
        if (param % 2 === 0) {
            return param ** param;
        } else {
            return (param - 1) ** 2;
        }
    }

    return null;
}

// console.log(matek());
// console.log(matek("5"));
// console.log(matek(10));
// console.log(matek(9));
//
// console.log(matek());                     // 0
// console.log(matek("5"));            // 1
// console.log(matek(10));             // 10000000000
// console.log(matek(7));              // 36 (6^2)
// console.log(matek(true));           // null
// console.log(matek({}));             // null
// console.log(matek(3.14));           // null