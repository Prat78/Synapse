const fs = require('fs');
const readline = require('readline');

async function audit() {
    const fileStream = fs.createReadStream('c:\\Users\\abhil\\Desktop\\website\\games.js');
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    console.log("STATUS OF ALL GAMES:");
    for await (const line of rl) {
        const keyMatch = line.match(/^\s*"([^"]+)":\s*\{/);
        if (keyMatch) {
            const key = keyMatch[1];
            const hasDesc = line.includes('"description":');
            console.log(`${hasDesc ? '[YES]' : '[NO ]'} - ${key}`);
        }
    }
}

audit();
