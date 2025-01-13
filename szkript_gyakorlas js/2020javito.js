function zombi(szoveg) {
    if (szoveg.length % 2 === 0 || szoveg.length < 3) {
        return "hiba";
    }

    let kozepso_index = Math.floor(szoveg.length / 2)
    let kozepso = Number(szoveg[kozepso_index]);

    let jobb = false, bal = false;
    for (let i = 0; i < kozepso_index; i++) {
        if (szoveg[i] > kozepso) {
            bal = true;
            break;
        }
    }
    for (let i = kozepso_index + 1; i < szoveg.length; i++) {
        if (szoveg[i] > kozepso) {
            jobb = true;
            break;
        }
    }

    if (jobb && bal) {
        return "mindenhonnan";
    } else if (!jobb && !bal) {
        return "sehonnan";
    } else if (jobb && !bal) {
        return "jobbrol";
    } else {
        return "balrol";
    }
}

console.log(zombi("121")); // sehonnan
console.log(zombi("222")); // sehonnan
console.log(zombi("5430162439527618053")); // sehonnan
console.log(zombi("322")); // balrol
console.log(zombi("223")); // jobbrol
console.log(zombi("323")); // mindenhonnan