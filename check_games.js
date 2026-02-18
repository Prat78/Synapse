const fs = require('fs');
const content = fs.readFileSync('c:\\Users\\abhil\\Desktop\\website\\games.js', 'utf8');
const lines = content.split('\n');
const targets = ["1v1 lol", "baldis-basics", "basket-random", "bitlife", "bloonstd6", "drive-mad", "drift hunters", "geometry-dash", "motox3m", "polytrack", "run3", "slope"];

targets.forEach(target => {
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].includes(`"${target}":`)) {
            console.log(`${i + 1}: ${lines[i].substring(0, 150)}`);
            break;
        }
    }
});
