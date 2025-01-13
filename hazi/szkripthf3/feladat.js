// Nev: Tóth-Vizhuzó Albert Pál
// Neptun: G9V7JU
// h: h378775

function betuszaml(str) {
    let szaml = 0;
    let abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for (let betu of str) {
        if (abc.includes(betu)) {
            szaml++;
        }
    }

    return szaml;
}

function clear(tomb) {
    if (!tomb || !Array.isArray(tomb)) {
        return 0;
    }

    let vege = [];

    for (let elem of tomb) {
        if (typeof elem === 'number') {
            vege.unshift(elem);
        }

        if (typeof elem === 'string' && elem.length >= 1 && betuszaml(elem) >= 1) {
            // console.log(elem.slice(0,2));
            vege.unshift(elem.slice(0,2).toUpperCase());
        }
    }

    return vege;
}

// console.log(clear());
// console.log(clear( [2,5,3,'heyho',null,7,'d011234356']));
console.log(clear( ['h',3,5,7]));

