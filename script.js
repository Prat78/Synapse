
// ===========================
// Game Data & Config
// ===========================

if (typeof games !== 'undefined' && typeof GAMES === 'undefined') {
    // 1. Define specific name corrections (Key -> Nice Name)
    const NAME_CORRECTIONS = {
        "1v1-lol": "1v1.LOL",
        "10 minutes til ldawn": "10 Minutes Till Dawn",
        "achieve unlocked": "Achievement Unlocked",
        "bad time simulator": "Bad Time Simulator (Sans)",
        "baldis-basics": "Baldi's Basics",
        "Bendy and the ink machiene": "Bendy and the Ink Machine",
        "bloonstd2": "Bloons TD 2",
        "bloonstd3": "Bloons TD 3",
        "bloonstd5": "Bloons TD 5",
        "bloonstd6": "Bloons TD 6",
        "basket-random": "Basket Random",
        "basketballstars": "Basketball Stars",
        "bitlife": "BitLife",
        "bopcity": "Bop City",
        "cookierun": "Cookie Run",
        "cookie-clicker": "Cookie Clicker",
        "cut the rpoe": "Cut the Rope",
        "dadish": "Dadish",
        "dadish2": "Dadish 2",
        "dadish3": "Dadish 3",
        "drift hunters": "Drift Hunters",
        "drive-mad": "Drive Mad",
        "ducklife1": "Duck Life 1",
        "fnaf": "Five Nights at Freddy's",
        "fnaf2": "Five Nights at Freddy's 2",
        "fnaf3": "Five Nights at Freddy's 3",
        "fnaf4": "Five Nights at Freddy's 4",
        "flappybird": "Flappy Bird",
        "footballbros": "Football Bros",
        "fruitninja": "Fruit Ninja",
        "geometry-dash": "Geometry Dash",
        "goi": "Getting Over It",
        "gtag": "Gorilla Tag",
        "GTA Vice city": "GTA Vice City",
        "gunspin": "Gun Spin",
        "happywheels": "Happy Wheels",
        "jetpackjoyride": "Jetpack Joyride",
        "minecraft": "Minecraft",
        "motox3m": "Moto X3M",
        "melon-playground": "Melon Playground",
        "ovo": "OvO",
        "OvO2": "OvO 2",
        "pacman": "Pac-Man",
        "paperio2": "Paper.io 2",
        "polytrack": "PolyTrack",
        "papasbakeria": "Papa's Bakeria",
        "papasburgeria": "Papa's Burgeria",
        "papascheeseria": "Papa's Cheeseria",
        "papasdonuteria": "Papa's Donuteria",
        "papasfreezeria": "Papa's Freezeria",
        "papaspizza": "Papa's Pizzeria",
        "ragdoll-archers": "Ragdoll Archers",
        "retro-bowl": "Retro Bowl",
        "roblox": "Roblox",
        "rooftop-snipers": "Rooftop Snipers",
        "slope": "Slope",
        "subway-surfers": "Subway Surfers",
        "tanuki-sunset": "Tanuki Sunset",
        "temple-run-2": "Temple Run 2",
        "vex3": "Vex 3",
        "vex4": "Vex 4",
        "vex5": "Vex 5",
        "vex6": "Vex 6",
        "vex7": "Vex 7",
        "watergirl-1": "Fireboy & Watergirl 1",
        "watergirl-2": "Fireboy & Watergirl 2",
        "watergirl-3": "Fireboy & Watergirl 3",
        "watergirl-4": "Fireboy & Watergirl 4",
        "wordle": "Wordle"
    };

    // 2. Define Popularity Order (Highest priority first)
    const POPULAR_KEYS = [
        "gta",
        "minecraft",
        "roblox",
        "1v1-lol",
        "subway-surfers",
        "fnaf",
        "slope",
        "retro-bowl",
        "geometry-dash",
        "happywheels",
        "cookie-clicker",
        "bitlife",
        "paperio2",
        "pacman",
        "bloonstd6",
        "bloonstd5",
        "angry birds",
        "bad piggies",
        "cut the rpoe",
        "cut the rope",
        "doodle jump",
        "flappybird",
        "fruitninja",
        "jetpackjoyride",
        "baldis-basics",
        "basket-random",
        "drift hunters",
        "drive-mad",
        "motox3m",
        "polytrack",
        "balatro",
        "ovo",
        "vex",
        "stickman",
        "run 3",
        "gtag",
        "papas"
    ];

    const sortedKeys = Object.keys(games).sort((a, b) => {
        const aLower = a.toLowerCase();
        const bLower = b.toLowerCase();

        let aIndex = POPULAR_KEYS.findIndex(p => aLower.includes(p));
        let bIndex = POPULAR_KEYS.findIndex(p => bLower.includes(p));

        if (aIndex === -1) aIndex = 9999;
        if (bIndex === -1) bIndex = 9999;

        if (aIndex !== bIndex) {
            return aIndex - bIndex;
        }
        return aLower.localeCompare(bLower);
    });

    window.GAMES = sortedKeys.map((key, index) => {
        const gameData = games[key];
        const link = typeof gameData === 'object' ? gameData.link : gameData;
        const customThumb = typeof gameData === 'object' ? gameData.thumb : null;

        let title = key;
        if (NAME_CORRECTIONS[key]) {
            title = NAME_CORRECTIONS[key];
        } else {
            title = key.split(/[-_]/).map(word =>
                word.charAt(0).toUpperCase() + word.slice(1)
            ).join(' ');
        }

        return {
            id: index,
            name: title,
            category: 'Unblocked',
            link: link,
            thumb: customThumb || 'https://games-f518e.web.app/' + key + '/icon.png',
            description: 'Play ' + title + ' unblocked and free!'
        };
    });
}

// ===========================
// AI Configuration
// ===========================
let HF_API_URL = "https://ai.pratyush-singh365.workers.dev/generate";
let sessionId = crypto.randomUUID();

async function sendChat() {
    const input = document.getElementById("chatInput");
    const msg = input.value.trim();
    if (!msg) return;

    addMessage(msg, "user");
    input.value = "";

    const countEl = document.getElementById("messageCount");
    if (countEl) countEl.textContent = parseInt(countEl.textContent) + 1;

    const typingIndicator = document.getElementById("typingIndicator");
    if (typingIndicator) typingIndicator.classList.remove("hidden");

    const c = document.getElementById("chatMessages");
    const t = document.getElementById("typingIndicator");
    const aiDiv = document.createElement("div");
    aiDiv.className = "flex items-start";
    aiDiv.innerHTML =
        '<div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center"><i class="fas fa-robot text-sm"></i></div>' +
        '<div class="ml-3 w-full"><div class="chat-bubble-ai p-6 max-w-3xl"><p class="streamText font-inter text-lg leading-relaxed tracking-wide text-gray-100"></p></div></div>';
    if (c) {
        if (t) c.insertBefore(aiDiv, t);
        else c.appendChild(aiDiv);
    }
    const streamText = aiDiv.querySelector(".streamText");

    try {
        const response = await fetch(HF_API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                prompt: msg,
                session_id: sessionId,
                max_tokens: 300
            })
        });

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let done = false;

        while (!done) {
            const { value, done: doneReading } = await reader.read();
            done = doneReading;
            if (value) {
                const chunk = decoder.decode(value, { stream: true });
                streamText.textContent += chunk;
                if (c) c.scrollTop = c.scrollHeight;
            }
        }

    } catch (err) {
        console.error(err);
        if (streamText) streamText.textContent = "The servers are probably asleep at this time😴, let them rest....";
    } finally {
        if (typingIndicator) typingIndicator.classList.add("hidden");
    }
}

function resetSession() {
    sessionId = crypto.randomUUID();
    const c = document.getElementById("chatMessages");
    if (c) c.innerHTML = ''; // Start fresh
    console.log('New session started:', sessionId);
}

function addMessage(text, sender) {
    var c = document.getElementById("chatMessages");
    var t = document.getElementById("typingIndicator");
    var d = document.createElement("div");

    d.className = "flex items-start " + (sender === "user" ? "justify-end" : "");

    if (sender === "user") {
        d.innerHTML =
            '<div class="mr-3"><div class="chat-bubble-user p-4 max-w-md"><p>' + text + '</p></div></div>' +
            '<div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center"><i class="fas fa-user text-sm"></i></div>';
    } else {
        d.innerHTML =
            '<div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center"><i class="fas fa-robot text-sm"></i></div>' +
            '<div class="ml-3"><div class="chat-bubble-ai p-4 max-w-md"><p>' + text + '</p></div></div>';
    }

    if (c) {
        if (t) c.insertBefore(d, t);
        else c.appendChild(d);
        c.scrollTop = c.scrollHeight;
    }
}

// ===========================
// State Variables
// ===========================
var currentCategory = 'all';
var searchQuery = '';

// ===========================
// Initialization Function
// ===========================
function init() {
    // 1. Initialize Background Effects (Always run)
    createMatrixRain();
    createStars();
    setupAnimations();

    // 2. Handle Loading Screen Logic - Checking Session Immediately
    const loadingScreen = document.getElementById("loadingScreen");
    const alreadyLoaded = sessionStorage.getItem('siteLoaded');

    if (alreadyLoaded) {
        // Site already loaded in this session: Hide loader immediately
        if (loadingScreen) {
            loadingScreen.style.display = 'none';
        }
    } else {
        // First load: Play animation sequence

        // Text Animation Logic (only run if needed)
        const loadingStatuses = [
            'LOADING NEURAL NETWORK...',
            'INITIALIZING AI CORE...',
            'CONNECTING TO SERVERS...',
            'DECRYPTING DATA STREAMS...',
            'CALIBRATING INTERFACE...',
            'SYSTEM READY...'
        ];
        let statusIndex = 0;
        const statusEl = document.getElementById('loadingStatus');

        if (statusEl) {
            const statusInterval = setInterval(() => {
                statusIndex = (statusIndex + 1) % loadingStatuses.length;
                statusEl.textContent = loadingStatuses[statusIndex];
            }, 400);

            setTimeout(() => clearInterval(statusInterval), 2500);
        }

        // Fade Out Animation
        setTimeout(() => {
            if (loadingScreen) {
                loadingScreen.style.opacity = "0";
                loadingScreen.style.transition = "opacity 0.5s ease";
                setTimeout(() => {
                    loadingScreen.style.display = "none";
                }, 500);
            }
        }, 2500);

        // Mark site as loaded
        sessionStorage.setItem('siteLoaded', 'true');
    }

    // 3. Initialize App Logic
    renderCategories();
    renderGames();
    setupEvents();
    setupChatroomEvents();

    // Load ads on initial page load
    initAdSystem();

    // Initialize Firebase for global announcements (for ALL users)
    initFirebaseForAnnouncements();

    // Page specific init
    const chatroomPage = document.getElementById('chatroomPage');
    if (chatroomPage && !chatroomPage.classList.contains('hidden')) {
        initFirebase();
        if (isFirebaseInitialized) {
            switchRoom('chatroom1');
            setupImageUpload();
        }
    }

    const feedbackPage = document.getElementById('feedbackPage');
    if (feedbackPage && !feedbackPage.classList.contains('hidden')) {
        initFirebase();
        if (isFirebaseInitialized) initFeedback();
    }
}

// ===========================
// Matrix Rain
// ===========================
function createMatrixRain() {
    const container = document.getElementById('matrixRain');
    if (!container) return;

    const chars = '01アイウエオカキクケコサシスセソ';

    for (let i = 0; i < 20; i++) {
        const drop = document.createElement('div');
        drop.className = 'matrix-drop';
        drop.style.left = (Math.random() * 100) + '%';
        drop.style.animationDuration = (Math.random() * 5 + 3) + 's';
        drop.style.animationDelay = (Math.random() * 5) + 's';
        drop.textContent = chars[Math.floor(Math.random() * chars.length)];
        container.appendChild(drop);
    }
}

// ===========================
// Stars
// ===========================
function createStars() {
    var bg = document.getElementById("parallaxBg");
    if (!bg) return;

    for (var i = 0; i < 100; i++) {
        var s = document.createElement("div");
        s.className = "star";
        s.style.width = Math.random() * 3 + "px";
        s.style.height = s.style.width;
        s.style.left = Math.random() * 100 + "%";
        s.style.top = Math.random() * 100 + "%";
        s.style.animationDelay = Math.random() * 5 + "s";
        bg.appendChild(s);
    }

    for (var i = 0; i < 50; i++) {
        var particle = document.createElement("div");
        particle.className = "particle";
        particle.style.width = Math.random() * 4 + 1 + "px";
        particle.style.height = particle.style.width;
        particle.style.left = Math.random() * 100 + "%";
        particle.style.top = Math.random() * 100 + 100 + "%";
        particle.style.opacity = Math.random() * 0.5 + 0.1;
        particle.style.animationDelay = Math.random() * 10 + "s";
        particle.style.animationDuration = Math.random() * 10 + 15 + "s";
        bg.appendChild(particle);
    }

    for (var i = 0; i < 3; i++) {
        var nebula = document.createElement("div");
        nebula.className = "nebula";
        nebula.style.width = Math.random() * 300 + 200 + "px";
        nebula.style.height = nebula.style.width;
        nebula.style.left = Math.random() * 100 + "%";
        nebula.style.top = Math.random() * 100 + "%";

        if (i === 0) {
            nebula.style.background = "radial-gradient(circle, rgba(59, 130, 246, 0.3), transparent)";
        } else if (i === 1) {
            nebula.style.background = "radial-gradient(circle, rgba(139, 92, 246, 0.3), transparent)";
        } else {
            nebula.style.background = "radial-gradient(circle, rgba(236, 72, 153, 0.2), transparent)";
        }

        bg.appendChild(nebula);
    }
}

// ===========================
// Categories & Games
// ===========================
function renderCategories() {
    if (typeof GAMES === 'undefined') return;
    const container = document.getElementById("categoryFilter");
    if (!container) return;

    var cats = ['all'];
    GAMES.forEach(g => {
        if (cats.indexOf(g.category) === -1) cats.push(g.category);
    });

    var html = '';
    cats.forEach(cat => {
        var active = cat === currentCategory ? 'active' : '';
        var label = cat === 'all' ? 'All Games' : cat;
        html += '<button class="cat-btn ' + active + '" onclick="filterCategory(\'' + cat + '\')">' + label + '</button>';
    });

    container.innerHTML = html;
}

function filterCategory(cat) {
    currentCategory = cat;
    renderCategories();
    renderGames();
}

function getGameImageUrl(g) {
    if (g.thumb) return g.thumb;
    var key = (g.name || '').toLowerCase().replace(/ /g, '-');
    return 'https://games-f518e.web.app/' + key + '/icon.png';
}

function renderGames() {
    const container = document.getElementById("gamesGrid");
    if (!container) return;

    if (typeof GAMES === 'undefined') {
        container.innerHTML = '<p class="text-gray-400 col-span-full text-center">No games found. Check games.js file.</p>';
        return;
    }

    var filtered = GAMES.filter(g => {
        var matchesCat = currentCategory === 'all' || g.category === currentCategory;
        var matchesSearch = searchQuery === '' || (g.title || g.name || '').toLowerCase().includes(searchQuery.toLowerCase());
        return matchesCat && matchesSearch;
    });

    var html = '';
    filtered.forEach(g => {
        var idx = GAMES.indexOf(g);
        var img = getGameImageUrl(g);

        html += '<div class="game-card glassmorphism rounded-2xl overflow-hidden" onclick="playGame(' + idx + ')">';
        html += '<div class="relative overflow-hidden">';
        html += '<img src="' + img + '" alt="' + (g.title || g.name).replace(/'/g, "&apos;") + '" class="w-full h-48 object-cover" onerror="this.src=\'https://via.placeholder.com/400x200/1e293b/3b82f6?text=' + encodeURIComponent(g.title || g.name).replace(/'/g, "%27") + '\'">';
        html += '<div class="absolute top-4 right-4"><span class="bg-primary/80 text-white px-3 py-1 rounded-full text-xs">' + g.category + '</span></div>';
        html += '<div class="play-overlay"><div class="play-icon"><i class="fas fa-play"></i></div></div>';
        html += '</div>';
        html += '<div class="p-6">';
        html += '<h3 class="text-xl font-semibold mb-2">' + (g.title || g.name) + '</h3>';
        html += '<p class="text-gray-400 text-sm mb-4">' + (g.description || 'Click to play this game!') + '</p>';
        html += '<span class="text-primary font-semibold">Play Now →</span>';
        html += '</div></div>';
    });

    container.innerHTML = html;
}

function playGame(i) {
    var g = GAMES[i];
    if (!g) return;
    sessionStorage.setItem('currentGame', JSON.stringify(g));
    window.location.href = 'play.html';
}

// ===========================
// Events
// ===========================
function setupEvents() {
    // Note: data-page logic removed as we are using MPA with hrefs.
    // Keeping this cleaner for mobile menu only if needed.

    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", () => {
            const m = document.getElementById("mobileMenu");
            if (m) m.classList.toggle("hidden");
        });
    }

    const tryAI = document.getElementById("tryAI");
    if (tryAI) {
        tryAI.addEventListener("click", () => {
            window.location.href = 'chat.html';
        });
    }

    const sendMessage = document.getElementById("sendMessage");
    if (sendMessage) sendMessage.addEventListener("click", sendChat);

    const chatInput = document.getElementById("chatInput");
    if (chatInput) {
        chatInput.addEventListener("keypress", e => {
            if (e.key === "Enter") sendChat();
        });
    }

    const gameSearch = document.getElementById("gameSearch");
    if (gameSearch) {
        gameSearch.addEventListener("input", e => {
            searchQuery = e.target.value;
            renderGames();
        });
    }
}

// ===========================
// Firebase & Chatroom
// ===========================
const firebaseConfig = {
    apiKey: "AIzaSyB4p6X2u5thYySUjgCnjQeYZYQ87xg-xds",
    authDomain: "chatroom-f1e6b.firebaseapp.com",
    databaseURL: "https://chatroom-f1e6b-default-rtdb.firebaseio.com",
    projectId: "chatroom-f1e6b",
    storageBucket: "chatroom-f1e6b.firebasestorage.app",
    messagingSenderId: "663028089072",
    appId: "1:663028089072:web:04f2706fd3f5badf334235",
    measurementId: "G-ZT0KHEJ77Y"
};

let firebaseApp, database, storage, messagesRef, presenceRef, userPresenceRef;
let currentUser = { nickname: '', id: '' };
let currentRoom = 'general';
let lastMessageTime = 0;
let userMessageCount = 0;
let isFirebaseInitialized = false;
let selectedImage = null;
const badWords = [];
const roomTitles = {
    'chatroom1': 'Chatroom 1',
    'chatroom2': 'Chatroom 2',
    'chatroom3': 'Chatroom 3',
    'chatroom4': 'Chatroom 4',
    'chatroom5': 'Chatroom 5'
};

function initFirebase() {
    if (isFirebaseInitialized) return;
    try {
        firebaseApp = firebase.initializeApp(firebaseConfig);
        database = firebase.database();
        storage = firebase.storage();
        isFirebaseInitialized = true;
        setupUser();
        setupGlobalAnnouncementListener();
    } catch (error) {
        console.error('Firebase init error:', error);
    }
}

function initFirebaseForAnnouncements() {
    if (isFirebaseInitialized) return;
    try {
        firebaseApp = firebase.initializeApp(firebaseConfig);
        database = firebase.database();
        storage = firebase.storage();
        isFirebaseInitialized = true;
        setupGlobalAnnouncementListener();
    } catch (error) {
        console.error('Firebase announcement init error:', error);
    }
}

function setupGlobalAnnouncementListener() {
    if (!database) return;
    const globalAnnouncementRef = database.ref('global_announcements');
    let lastAnnouncementTimestamp = 0;

    globalAnnouncementRef.on('value', (snapshot) => {
        if (!snapshot.exists()) return;
        const announcement = snapshot.val();
        if (announcement.timestamp && announcement.timestamp > lastAnnouncementTimestamp) {
            lastAnnouncementTimestamp = announcement.timestamp;
            showGlobalAnnouncement(announcement);
        }
    });
}

function showGlobalAnnouncement(announcement) {
    const announcementEl = document.getElementById('globalAnnouncement');
    const textEl = document.getElementById('announcementText');
    if (!announcementEl || !textEl) return;

    let displayText = announcement.text;
    if (announcement.adminName) {
        displayText = `<strong>From ${announcement.adminName}:</strong> ${announcement.text}`;
    }
    textEl.innerHTML = displayText;
    announcementEl.classList.add('active');

    playAnnouncementSound();

    setTimeout(() => {
        closeGlobalAnnouncement();
    }, 15000);
}

function closeGlobalAnnouncement() {
    const announcementEl = document.getElementById('globalAnnouncement');
    if (announcementEl) announcementEl.classList.remove('active');
}

function playAnnouncementSound() {
    try {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        oscillator.frequency.value = 800;
        oscillator.type = 'sine';
        gainNode.gain.value = 0.1;
        oscillator.start();
        oscillator.stop(audioContext.currentTime + 0.2);
    } catch (e) { }
}

function switchRoom(room) {
    document.querySelectorAll('.room-btn').forEach(btn => btn.classList.remove('active'));
    const btn = document.querySelector(`[data-room="${room}"]`);
    if (btn) btn.classList.add('active');

    if (messagesRef) messagesRef.off();
    if (presenceRef) presenceRef.off();
    if (userPresenceRef) userPresenceRef.remove();

    currentRoom = room;
    messagesRef = database.ref(`chatroom/${room}/messages`);
    presenceRef = database.ref(`chatroom/${room}/presence`);

    const titleEl = document.getElementById('currentRoomTitle');
    if (titleEl) titleEl.textContent = roomTitles[room];

    const container = document.getElementById('chatroomMessages');
    if (container) container.innerHTML = '<div class="text-center text-gray-500 text-sm py-8"><i class="fas fa-spinner fa-spin text-2xl mb-2"></i><p>Loading messages...</p></div>';

    listenToMessages();
    setupPresence();
}

function setupUser() {
    currentUser.id = localStorage.getItem('chatroomUserId');
    if (!currentUser.id) {
        currentUser.id = 'user_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('chatroomUserId', currentUser.id);
    }

    currentUser.nickname = localStorage.getItem('chatroomNickname');
    if (!currentUser.nickname) {
        // We might not want to prompt immediately if not on chatroom page
        const countEl = document.getElementById('currentNickname');
        if (countEl) promptForNickname();
    } else {
        const nickEl = document.getElementById('currentNickname');
        if (nickEl) nickEl.textContent = currentUser.nickname;
    }

    userMessageCount = parseInt(localStorage.getItem('userMessageCount') || '0');
    const userCountEl = document.getElementById('userMessageCount');
    if (userCountEl) userCountEl.textContent = userMessageCount;

    checkBanStatus();
}

function checkBanStatus() {
    if (currentUser.id) {
        database.ref('bans/' + currentUser.id).on('value', (snapshot) => {
            if (snapshot.exists() && snapshot.val() === true) {
                const input = document.getElementById('chatroomInput');
                if (input) {
                    input.disabled = true;
                    input.placeholder = "⛔ You are banned from this chat.";
                    document.getElementById('sendChatroomMessage').disabled = true;
                    alert('⛔ You have been BANNED from the chatroom by an administrator.');
                }
            }
        });
    }
}

function promptForNickname() {
    let nickname = prompt('Enter your nickname (3-20 characters):');
    if (!nickname) nickname = 'Guest' + Math.floor(Math.random() * 9999);
    nickname = nickname.trim().substring(0, 20);
    nickname = filterProfanity(nickname);
    if (nickname.length < 3) nickname = 'Guest' + Math.floor(Math.random() * 9999);
    currentUser.nickname = nickname;
    localStorage.setItem('chatroomNickname', nickname);
    const el = document.getElementById('currentNickname');
    if (el) el.textContent = nickname;
}

function changeNickname() {
    localStorage.removeItem('chatroomNickname');
    promptForNickname();
}

function setupPresence() {
    userPresenceRef = presenceRef.child(currentUser.id);
    userPresenceRef.set({
        id: currentUser.id,
        nickname: currentUser.nickname,
        online: true,
        lastSeen: firebase.database.ServerValue.TIMESTAMP
    });
    userPresenceRef.onDisconnect().remove();

    presenceRef.on('value', (snapshot) => {
        const count = snapshot.numChildren();
        const countEl = document.getElementById('onlineCount');
        if (countEl) countEl.textContent = count;
    });
}

function listenToMessages() {
    const container = document.getElementById('chatroomMessages');
    if (!container) return;
    container.innerHTML = '';

    messagesRef.orderByChild('timestamp').limitToLast(50).on('child_added', (snapshot) => {
        const msg = snapshot.val();
        msg.id = snapshot.key;
        displayMessage(msg);
        updateTotalCount();
    });
}

function displayMessage(msg) {
    const container = document.getElementById('chatroomMessages');
    if (!container) return;

    const isOwn = msg.userId === currentUser.id;
    const msgDiv = document.createElement('div');
    msgDiv.className = 'flex items-start ' + (isOwn ? 'justify-end' : '');
    msgDiv.setAttribute('data-message-id', msg.id || '');

    const time = msg.timestamp ? new Date(msg.timestamp).toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: '2-digit'
    }) : '...';

    let messageContent = '';
    const imgSource = msg.imageData || msg.imageUrl;
    if (imgSource) {
        const safeSrc = imgSource.startsWith('data:') ? imgSource : escapeHtml(imgSource);
        messageContent = `<img src="${safeSrc}" class="image-message" onclick="window.open('${safeSrc}', '_blank')" onerror="this.onerror=null; this.src='https://placehold.co/300?text=Image+Load+Error'">`;
    }

    if (msg.text) {
        messageContent += `<p class="text-sm ${imgSource ? 'mt-2' : ''}">${escapeHtml(msg.text)}</p>`;
    }

    if (msg.type === 'system') {
        msgDiv.className = 'flex items-center justify-center my-4';
        msgDiv.innerHTML = `
            <div class="bg-gradient-to-r from-red-900/50 to-purple-900/50 border border-purple-500/30 rounded-lg px-6 py-3 w-[95%] text-center shadow-[0_0_15px_rgba(168,85,247,0.2)]">
                <div class="flex items-center justify-center text-purple-400 font-bold mb-1 tracking-widest text-xs uppercase"><i class="fas fa-bullhorn mr-2"></i> System Announcement</div>
                <p class="text-white text-md font-medium">${escapeHtml(msg.text)}</p>
                <span class="text-[10px] text-gray-400 mt-1 block">${time}</span>
            </div>`;
    } else {
        if (isOwn) {
            msgDiv.innerHTML = `
                <div class="text-right mr-3 max-w-md">
                    <div class="flex items-center justify-end mb-1">
                        <span class="text-xs text-gray-500 mr-2">${time}</span>
                        <span class="text-sm font-semibold text-primary">${escapeHtml(msg.nickname)}</span>
                    </div>
                    <div class="chat-bubble-user p-3">${messageContent}</div>
                </div>
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center flex-shrink-0"><i class="fas fa-user text-xs"></i></div>`;
        } else {
            msgDiv.innerHTML = `
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center flex-shrink-0"><i class="fas fa-user text-xs"></i></div>
                <div class="ml-3 flex-1 min-w-0">
                    <div class="flex items-center mb-1">
                        <span class="text-sm font-semibold text-secondary">${escapeHtml(msg.nickname)}</span>
                        <span class="text-xs text-gray-500 ml-2">${time}</span>
                    </div>
                    <div class="chat-bubble-ai p-3">${messageContent}</div>
                </div>`;
        }
    }
    container.appendChild(msgDiv);
    container.scrollTop = container.scrollHeight;
}

function setupImageUpload() {
    const imageUpload = document.getElementById('imageUpload');
    if (imageUpload) {
        imageUpload.onchange = handleImageSelect;
    }
}

function handleImageSelect(e) {
    const file = e.target.files[0];
    if (!file) return;
    if (file.size > 2 * 1024 * 1024) { alert('Image too large! Max 2MB'); return; }
    if (!file.type.startsWith('image/')) { alert('Please upload an image file'); return; }

    selectedImage = file;
    const reader = new FileReader();
    reader.onload = (re) => {
        const previewImg = document.getElementById('previewImg');
        const imagePreview = document.getElementById('imagePreview');
        if (previewImg) previewImg.src = re.target.result;
        if (imagePreview) imagePreview.classList.remove('hidden');
    };
    reader.readAsDataURL(file);
}

function setupChatroomEvents() {
    const sendBtn = document.getElementById('sendChatroomMessage');
    const chatInput = document.getElementById('chatroomInput');
    if (sendBtn) sendBtn.onclick = sendChatroomMessage;
    if (chatInput) {
        chatInput.addEventListener('paste', handlePaste);
        chatInput.onkeypress = (e) => {
            if (e.key === 'Enter') sendChatroomMessage();
        };
    }
}

async function sendChatroomMessage() {
    const input = document.getElementById('chatroomInput');
    const btn = document.getElementById('sendChatroomMessage');
    if (!input || !btn) return;

    const text = input.value.trim();
    if (!text && !selectedImage) {
        input.style.borderColor = 'red';
        setTimeout(() => input.style.borderColor = '', 500);
        return;
    }

    if (!messagesRef) {
        initFirebase();
        if (!messagesRef) return;
    }

    btn.disabled = true;
    const originalIcon = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';

    try {
        let imageData = null;
        if (selectedImage) {
            imageData = await new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => resolve(e.target.result);
                reader.onerror = reject;
                reader.readAsDataURL(selectedImage);
            });
        }

        const filtered = text ? filterProfanity(text) : null;
        await messagesRef.push({
            userId: currentUser.id || 'anon',
            nickname: currentUser.nickname || 'Anonymous',
            text: filtered,
            imageData: imageData,
            type: 'user',
            timestamp: firebase.database.ServerValue.TIMESTAMP
        });

        input.value = '';
        cancelImage();
        lastMessageTime = Date.now();

        userMessageCount++;
        localStorage.setItem('userMessageCount', userMessageCount);
        const countEl = document.getElementById('userMessageCount');
        if (countEl) countEl.textContent = userMessageCount;

    } catch (error) {
        console.error('Send Error:', error);
        alert('Failed to send message');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        input.focus();
    }
}

function handlePaste(e) {
    const items = (e.clipboardData || e.originalEvent.clipboardData).items;
    if (!items) return;
    for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
            const blob = items[i].getAsFile();
            if (!blob) continue;
            if (blob.size > 2 * 1024 * 1024) { alert('Image too large! Max 2MB allowed.'); continue; }

            selectedImage = blob;
            const reader = new FileReader();
            reader.onload = (re) => {
                const previewImg = document.getElementById('previewImg');
                const imagePreview = document.getElementById('imagePreview');
                if (previewImg) previewImg.src = re.target.result;
                if (imagePreview) imagePreview.classList.remove('hidden');
            };
            reader.readAsDataURL(blob);
            e.preventDefault();
            break;
        }
    }
}

function updateTotalCount() {
    if (messagesRef) {
        messagesRef.once('value', (snapshot) => {
            const countEl = document.getElementById('totalMessageCount');
            if (countEl) countEl.textContent = snapshot.numChildren();
        });
    }
}

function cancelImage() {
    selectedImage = null;
    const preview = document.getElementById('imagePreview');
    if (preview) preview.classList.add('hidden');
    const uploadInput = document.getElementById('imageUpload');
    if (uploadInput) uploadInput.value = '';
}

function filterProfanity(text) {
    if (typeof badWords === 'undefined') return text;
    let filtered = text;
    badWords.forEach(word => {
        const regex = new RegExp(word, 'gi');
        filtered = filtered.replace(regex, '*'.repeat(word.length));
    });
    return filtered;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ===========================
// Feedback
// ===========================
let feedbackRef;
let isFeedbackInitialized = false;

function initFeedback() {
    if (isFeedbackInitialized) return;
    feedbackRef = database.ref('feedback');
    isFeedbackInitialized = true;
    listenToFeedback();

    const feedbackInput = document.getElementById('feedbackText');
    if (feedbackInput) {
        feedbackInput.addEventListener('input', (e) => {
            const charCountEl = document.getElementById('charCount');
            if (charCountEl) charCountEl.textContent = e.target.value.length;
        });
    }
}

function listenToFeedback() {
    feedbackRef.orderByChild('timestamp').limitToLast(50).on('value', (snapshot) => {
        const feedbackList = document.getElementById('feedbackList');
        if (!feedbackList) return;
        feedbackList.innerHTML = '';
        if (!snapshot.exists()) {
            feedbackList.innerHTML = '<div class="text-center py-8"><p class="text-gray-500">No feedback yet. Be the first!</p></div>';
            return;
        }
        const items = [];
        snapshot.forEach((child) => { items.push({ id: child.key, ...child.val() }); });
        items.reverse().forEach(item => { displayFeedback(item); });
    });
}

function displayFeedback(item) {
    const feedbackList = document.getElementById('feedbackList');
    if (!feedbackList) return;

    const typeEmojis = { bug: '🐛 Bug Report', feature: '✨ Feature Request', improvement: '💡 Improvement', general: '💬 General', compliment: '❤️ Compliment' };
    const typeColors = { bug: 'bg-red-500/20 text-red-400', feature: 'bg-purple-500/20 text-purple-400', improvement: 'bg-yellow-500/20 text-yellow-400', general: 'bg-blue-500/20 text-blue-400', compliment: 'bg-pink-500/20 text-pink-400' };

    const time = new Date(item.timestamp).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: '2-digit', minute: '2-digit' });
    const card = document.createElement('div');
    card.className = 'glassmorphism rounded-2xl p-6 feedback-card';

    let repliesHTML = '';
    if (item.replies) {
        Object.values(item.replies).forEach(reply => {
            repliesHTML += `<div class="mt-4 ml-4 pl-4 border-l-2 border-primary/30"><div class="flex items-center mb-2"><span class="text-sm font-semibold text-primary">Developer</span></div><p class="text-gray-300 text-sm">${escapeHtml(reply.text)}</p></div>`;
        });
    }

    card.innerHTML = `<div class="flex items-start justify-between mb-3"><span class="feedback-type-badge ${typeColors[item.type]}">${typeEmojis[item.type]}</span><span class="text-xs text-gray-500">${time}</span></div><p class="text-gray-300 mb-3 whitespace-pre-wrap">${escapeHtml(item.text)}</p>${repliesHTML}`;
    feedbackList.appendChild(card);
}

function submitFeedback() {
    const typeValue = document.getElementById('feedbackType').value;
    const textValue = document.getElementById('feedbackText').value.trim();
    const btn = document.getElementById('submitFeedbackBtn');
    if (!textValue) { alert('Please write your feedback!'); return; }
    if (textValue.length < 10) { alert('Please write at least 10 characters.'); return; }

    btn.disabled = true;
    feedbackRef.push({
        type: typeValue,
        text: textValue,
        timestamp: firebase.database.ServerValue.TIMESTAMP
    }).then(() => {
        document.getElementById('feedbackText').value = '';
        alert('✅ Feedback submitted!');
    }).catch(() => {
        alert('❌ Failed to submit.');
    }).finally(() => {
        btn.disabled = false;
    });
}


// ===========================
// Ads
// ===========================
const ADSTERRA_BANNER_KEY = 'cf6a125c26299b4a476c85e2b484cb3a';
let adRefreshIntervals = {};
let isAdSystemInitialized = false;

function initAdSystem() {
    if (isAdSystemInitialized) return;
    isAdSystemInitialized = true;
    for (let i = 1; i <= 10; i++) {
        setTimeout(() => {
            refreshSingleAd(i);
            const uniqueOffset = i * 2000;
            if (adRefreshIntervals[i]) clearInterval(adRefreshIntervals[i]);
            adRefreshIntervals[i] = setInterval(() => { refreshSingleAd(i); }, 60000 + uniqueOffset);
        }, i * 800);
    }
}

function refreshSingleAd(slotId) {
    const slot = document.getElementById('ad-slot-' + slotId);
    if (!slot) return;

    slot.innerHTML = `<div class="flex items-center justify-center w-full h-full bg-dark/20 animate-pulse rounded-xl border border-white/5"><span class="text-xs text-gray-600 font-orbitron">LOADING SPONSOR...</span></div>`;

    setTimeout(() => {
        slot.innerHTML = '';
        try {
            const adWrapper = document.createElement('div');
            adWrapper.className = 'ad-container-inner';
            adWrapper.style.width = '300px';
            adWrapper.style.height = '250px';

            const options = document.createElement('script');
            options.type = 'text/javascript';
            options.text = `atOptions = { 'key' : '${ADSTERRA_BANNER_KEY}', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };`;

            const script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = `//www.topcreativeformat.com/${ADSTERRA_BANNER_KEY}/invoke.js`;
            script.async = true;
            script.onerror = function () {
                slot.innerHTML = '<div class="flex items-center justify-center w-full h-full text-xs text-gray-700">Connecting...</div>';
            };

            adWrapper.appendChild(options);
            adWrapper.appendChild(script);
            slot.appendChild(adWrapper);
        } catch (err) {
            console.error(`Failed to load Ad Slot ${slotId}:`, err);
        }
    }, 100);
}

// ===========================
// Animations
// ===========================
function setupAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('active');
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => observer.observe(el));

    setupTilt();
}

function setupTilt() {
    document.addEventListener('mousemove', (e) => {
        if (window.innerWidth < 768) return;
        const tiltCards = document.querySelectorAll('.game-card');
        tiltCards.forEach(card => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            if (x > 0 && x < rect.width && y > 0 && y < rect.height) {
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (centerY - y) / 15;
                const rotateY = (x - centerX) / 15;
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
            } else {
                card.style.transform = '';
            }
        });
    });
}

function toggleFullscreen(id) {
    var iframe = document.getElementById(id);
    if (!iframe) return;
    var container = iframe.parentElement;
    if (document.fullscreenElement) document.exitFullscreen();
    else if (container.requestFullscreen) container.requestFullscreen();
    else if (container.webkitRequestFullscreen) container.webkitRequestFullscreen();
    else if (container.msRequestFullscreen) container.msRequestFullscreen();
}

document.addEventListener("DOMContentLoaded", init);
