const fs = require('fs');
const content = fs.readFileSync('c:\\Users\\abhil\\Desktop\\website\\games.js', 'utf8');
const gamesMatch = content.match(/var games = (\{[\s\S]*\});/);
if (gamesMatch) {
    try {
        // Since it's a JS file, not necessarily JSON, we might need a simpler regex for keys
        const keys = [];
        const regex = /"([^"]+)":\s*\{/g;
        let match;
        while ((match = regex.exec(content)) !== null) {
            keys.push(match[1]);
        }
        console.log(keys.join('\n'));
    } catch (e) {
        console.error(e);
    }
} else {
    console.log("No games object found");
}
