const fs = require('fs');
const content = fs.readFileSync('c:\\Users\\abhil\\Desktop\\website\\games.js', 'utf8');
const lines = content.split('\n');
const targets = [8, 20, 25, 32, 39, 58, 60, 78, 89, 102, 112, 115];

targets.forEach(ln => {
    const line = lines[ln - 1];
    // Truncate the line to avoid huge base64
    console.log(`${ln}: ${line.substring(0, 200)}`);
});
