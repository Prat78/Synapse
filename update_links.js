const fs = require('fs');
const gamesPath = 'c:\\Users\\abhil\\Desktop\\website\\games.js';
const content = fs.readFileSync(gamesPath, 'utf8');

const oldOrigin = 'https://clever.pbseducation1914.org/';
const newOrigin = 'https://muddy-dust-5dcd.pratyush-singh365.workers.dev/';

const updatedContent = content.split(oldOrigin).join(newOrigin);

fs.writeFileSync(gamesPath, updatedContent);
console.log('Successfully updated games.js links.');
