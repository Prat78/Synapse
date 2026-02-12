const fs = require('fs');
const content = fs.readFileSync('c:\\Users\\abhil\\Desktop\\website\\games.js', 'utf8');
const regex = /"([^"]+)":\s*\{\s*("description":\s*"[^"]*",\s*)?"link":/g;
let match;
const gamesWithDesc = [];
const gamesWithoutDesc = [];

// Simpler approach: find each key and check if "description" follows the opening brace
const lines = content.split('\n');
lines.forEach(line => {
    const keyMatch = line.match(/^\s*"([^"]+)":\s*\{/);
    if (keyMatch) {
        const key = keyMatch[1];
        if (line.includes('"description":')) {
            gamesWithDesc.push(key);
        } else {
            gamesWithoutDesc.push(key);
        }
    }
});

console.log("GAMES WITH DESCRIPTIONS:");
console.log(gamesWithDesc.join(', '));
console.log("\nGAMES WITHOUT DESCRIPTIONS:");
console.log(gamesWithoutDesc.join(', '));
