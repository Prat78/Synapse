

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
        "baldis-basics": "Teacher's Basics",
        "Bendy and the ink machiene": "Ink Machine Horror",
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
        "fnaf": "Five Nights of Horror",
        "fnaf2": "Five Nights of Horror 2",
        "fnaf3": "Five Nights of Horror 3",
        "fnaf4": "Five Nights of Horror 4",
        "flappybird": "Flappy Bird",
        "footballbros": "Football Bros",
        "fruitninja": "Fruit Ninja",
        "geometry-dash": "Geometry Dash",
        "goi": "Getting Over It",
        "gtag": "Gorilla Tag",
        "GTA Vice city": "ZTA Vice City",
        "gunspin": "Gun Spin",
        "happywheels": "Happy Wheels",
        "jetpackjoyride": "Jetpack Joyride",
        "minecraft": "Minebuild",
        "motox3m": "Moto X3M",
        "melon-playground": "Melon Playground",
        "ovo": "OvO",
        "OvO2": "OvO 2",
        "pacman": "Pellet Muncher",
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
        "roblox": "Blox World",
        "rooftop-snipers": "Rooftop Snipers",
        "slope": "Slope",
        "subway-surfers": "Train Surfers",
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
        "brawl stars",
        "basketball bros",
        "bitlife",
        "1v1",
        "gta",
        "Steal a brainrot",
        "Five nights at Epsteins",
        "Wrestle bros",
        "minecraft",
        "roblox",
        "subway-surfers",
        "fnaf",
        "slope",
        "retro-bowl",
        "basketball stars",
        "geometry-dash",
        "happywheels",
        "cookie-clicker",
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

        const baseDesc = gameData.description || `Play ${title} unblocked on Synapse AI. Immerse yourself in the world of ${title}, offering high-speed gameplay and zero lag for the ultimate school-safe gaming experience. Synapse AI provides the best unblocked versions of your favorite games with artificial intelligence assistance for the perfect gaming session.`;

        return {
            id: index,
            name: title,
            category: 'Unblocked',
            link: link,
            thumb: customThumb || 'https://games-f518e.web.app/' + key + '/icon.png',
            description: baseDesc
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
                // convert double line breaks into paragraph tags
                const formattedChunk = chunk
                    .split(/\n\s*\n/)          // split at empty lines
                    .map(p => `<p>${p.trim()}</p>`)  // wrap each paragraph in <p>
                    .join('');
                streamText.innerHTML += formattedChunk;

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
// Secure Auth & Session Management
// ===========================
const AUTH_TOKEN_KEY = 'synapse_auth_token';
const AuthManager = (function () {
    let _role = 'user';
    let _token = null;

    return {
        init: () => {
            _token = sessionStorage.getItem(AUTH_TOKEN_KEY);
            _role = sessionStorage.getItem('role') || 'user';
        },
        login: (token, role) => {
            _token = token;
            _role = role;
            sessionStorage.setItem(AUTH_TOKEN_KEY, token);
            sessionStorage.setItem('role', role);
        },
        getRole: () => _role,
        isAdmin: () => (_role === 'admin' || _role === 'dev'),
        isDeveloper: () => (_role === 'dev'),
        isAuthenticated: () => !!_token && _token.length > 10
    };
})();

function isAuth() {
    return AuthManager.isAuthenticated();
}

// ===========================
// Initialization Function
// ===========================
function init() {
    // 0. Initialize Auth Manager
    AuthManager.init();

    // 0.1 Restore UI Modes if authenticated
    if (AuthManager.isAuthenticated()) {
        document.body.classList.add('admin-mode');
        if (AuthManager.isDeveloper()) {
            document.body.classList.add('dev-mode');
        }
    }

    // 1. Initialize Background Effects (Always run)
    protectSite();
    createMatrixRain();
    createStars();
    setupAnimations();
    initAdBlockDetector(); // 1.1 AdBlock Detection


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

    // Initialize Firebase for global announcements (for ALL users)
    initFirebaseForAnnouncements();

    // Initialize Chat Notifications Badge
    initChatNotifications();

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
        html += '<img src="' + img + '" alt="' + (g.title || g.name).replace(/'/g, "&apos;") + '" class="w-full h-64 object-cover" onerror="this.src=\'https://via.placeholder.com/400x200/1e293b/3b82f6?text=' + encodeURIComponent(g.title || g.name).replace(/'/g, "%27") + '\'">';
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
    document.dispatchEvent(new CustomEvent('gamesRendered'));
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
        setupUser(); // This ensures currentUser.id is generated
        setupGlobalAnnouncementListener();
    } catch (error) {
        console.error('Firebase announcement init error:', error);
    }
}

function setupGlobalAnnouncementListener() {
    if (!database) return;
    const globalAnnouncementRef = database.ref('global_announcements');

    // Initialize with current time so we only show announcements sent AFTER the page loaded
    let lastAnnouncementTimestamp = Date.now();

    globalAnnouncementRef.on('value', (snapshot) => {
        if (!snapshot.exists()) return;
        const announcement = snapshot.val();

        // Only show if the announcement is newer than our last seen/page load time
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

    messageCounter = 0;
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
    if (!currentUser.id) return;
    database.ref('bans/' + currentUser.id).on('value', (snapshot) => {
        const input = document.getElementById('chatroomInput');
        const btn = document.getElementById('sendChatroomMessage');
        if (!input || !btn) return;

        if (snapshot.exists()) {
            const expiry = snapshot.val();
            const check = () => {
                const now = Date.now();
                if (now < expiry) {
                    const remaining = Math.ceil((expiry - now) / 1000);
                    input.disabled = true;
                    btn.disabled = true;
                    input.placeholder = `⛔ Banned. Re-opens in ${remaining}s`;
                    setTimeout(check, 1000);
                } else {
                    input.disabled = false;
                    btn.disabled = false;
                    input.placeholder = "Type a message...";
                    database.ref('bans/' + currentUser.id).remove();
                }
            };
            check();
        } else {
            input.disabled = false;
            btn.disabled = false;
            input.placeholder = "Type a message...";
        }
    });
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

let messageCounter = 0;

function listenToMessages() {
    const container = document.getElementById('chatroomMessages');
    if (!container) return;
    container.innerHTML = '';

    // Remove existing listeners if any (though usually managed by switchRoom .off())
    messagesRef.orderByChild('timestamp').limitToLast(100).on('child_added', (snapshot) => {
        const msg = snapshot.val();
        msg.id = snapshot.key;
        displayMessage(msg);
        updateTotalCount();
    });

    messagesRef.on('child_removed', (snapshot) => {
        const msgId = snapshot.key;
        const msgEl = document.querySelector(`[data-message-id="${msgId}"]`);
        if (msgEl) msgEl.remove();
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
                <div class="text-right mr-3 max-w-3xl lg:max-w-4xl">
                    <div class="flex items-center justify-end mb-1">
                        <span class="text-xs text-gray-500 mr-2">${time}</span>
                        ${msg.role === 'dev' ? '<span class="role-badge dev-badge">DEVELOPER</span>' : ''}
                        ${msg.role === 'admin' ? '<span class="role-badge admin-badge">ADMIN</span>' : ''}
                        <span class="text-sm font-semibold text-primary ml-2">${escapeHtml(msg.nickname)}</span>
                    </div>
                    <div class="chat-bubble-user p-3 inline-block text-left">${messageContent}</div>
                    <div class="admin-only mt-1">
                        <button onclick="deleteMessage('${msg.id}')" class="admin-only-btn"><i class="fas fa-trash mr-1"></i>Delete</button>
                    </div>
                </div>
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center flex-shrink-0"><i class="fas fa-user text-xs"></i></div>`;
        } else {
            msgDiv.innerHTML = `
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center flex-shrink-0"><i class="fas fa-user text-xs"></i></div>
                <div class="ml-3 flex-1 min-w-0 max-w-3xl lg:max-w-4xl">
                    <div class="flex items-center mb-1">
                        ${msg.role === 'dev' ? '<span class="role-badge dev-badge">DEVELOPER</span>' : ''}
                        ${msg.role === 'admin' ? '<span class="role-badge admin-badge">ADMIN</span>' : ''}
                        <span class="text-sm font-semibold text-secondary ml-2">${escapeHtml(msg.nickname)}</span>
                        <span class="text-xs text-gray-500 ml-2">${time}</span>
                    </div>
                    <div class="chat-bubble-ai p-3 inline-block">${messageContent}</div>
                    <div class="admin-only mt-1 flex space-x-2">
                        <button onclick="deleteMessage('${msg.id}')" class="admin-only-btn"><i class="fas fa-trash mr-1"></i>Delete</button>
                        <button onclick="banUser('${msg.userId}')" class="admin-only-btn"><i class="fas fa-hammer mr-1"></i>Ban</button>
                    </div>
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
            // COMPRESSION LOGIC: Resize image before sending to save database space
            imageData = await new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = new Image();
                    img.onload = () => {
                        const canvas = document.createElement('canvas');
                        const MAX_WIDTH = 800; // Resize to max 800px wide
                        let width = img.width;
                        let height = img.height;

                        if (width > MAX_WIDTH) {
                            height *= MAX_WIDTH / width;
                            width = MAX_WIDTH;
                        }
                        canvas.width = width;
                        canvas.height = height;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, width, height);
                        resolve(canvas.toDataURL('image/jpeg', 0.6)); // Compress to 60% quality JPEG
                    };
                    img.src = e.target.result;
                };
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
            role: AuthManager.getRole(),
            timestamp: firebase.database.ServerValue.TIMESTAMP
        });

        input.value = '';
        cancelImage();
        lastMessageTime = Date.now();

        // AUTO-PRUNE: Keep the database small to avoid hit usage limits
        autoPruneMessages();

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

// Auto-cleanup system to prevent database from hitting 1GB limit
async function autoPruneMessages() {
    if (!messagesRef) return;

    try {
        // We only want to keep the latest 150 messages
        const snapshot = await messagesRef.once('value');
        const count = snapshot.numChildren();

        if (count > 150) {
            // Get the oldest messages
            const oldestQuery = messagesRef.orderByChild('timestamp').limitToFirst(count - 150);
            const oldestSnapshot = await oldestQuery.once('value');

            const updates = {};
            oldestSnapshot.forEach(child => {
                updates[child.key] = null; // Mark for deletion
            });

            await messagesRef.update(updates);
            console.log("♻️ Auto-Pruned " + (count - 150) + " old messages to save space.");
        }
    } catch (e) {
        console.error("Prune Error:", e);
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

// Reusable ad injection helper for dynamic content
function injectAdTag(element) {
    if (!element) return;
    const script = document.createElement('script');
    script.innerHTML = `(function(z){var d=document,s=d.createElement('script'),l=d.scripts[d.scripts.length-1];s.settings=z||{};s.src="https://rapid-university.com/baXKVnsLd.Gwlo0-Y_WCcf/weJmg9WuQZtU/lMkKP/T/YJ4UMvjbEa3RNYD/U/trNpj/gZy/MhTgcz0/ONQA";s.async=true;s.referrerPolicy='no-referrer-when-downgrade';l.parentNode.insertBefore(s,l);})({})`;
    element.appendChild(script);
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
        const reversedItems = items.reverse();
        reversedItems.forEach((item, index) => {
            displayFeedback(item);
            // Inject an ad every 2 feedback items
            if ((index + 1) % 10 === 0) {
                const adDiv = document.createElement('div');
                adDiv.className = 'py-4 flex justify-center border-y border-white/5 opacity-80';
                adDiv.innerHTML = `<div class="ad-container overflow-hidden"></div>`;
                feedbackList.appendChild(adDiv);
                injectAdTag(adDiv.querySelector('.ad-container'));
            }
        });
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

    card.innerHTML = `<div class="flex items-start justify-between mb-3">
        <span class="feedback-type-badge ${typeColors[item.type]}">${typeEmojis[item.type]}</span>
        <div class="flex items-center space-x-3">
            <span class="text-xs text-gray-500">${time}</span>
            <button onclick="deleteFeedback('${item.id}')" class="admin-only admin-only-btn"><i class="fas fa-trash"></i></button>
        </div>
    </div>
    <p class="text-gray-300 mb-3 whitespace-pre-wrap">${escapeHtml(item.text)}</p>${repliesHTML}`;
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



// ===========================
// Chatroom Notifications
// ===========================
let unreadCount = 0;
let lastSeenTimestamp = parseInt(localStorage.getItem('chatroom_last_seen') || Date.now());

function initChatNotifications() {
    const isChatroomPage = document.getElementById('chatroomPage') !== null;

    if (!database) {
        // Wait for Firebase to be initialized
        setTimeout(initChatNotifications, 500);
        return;
    }

    // Reset loop if on chatroom page
    if (isChatroomPage) {
        localStorage.setItem('chatroom_last_seen', Date.now());
        unreadCount = 0;
        updateBadgeUI(0);

        // Update periodic visibility to clear badge if active
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') {
                localStorage.setItem('chatroom_last_seen', Date.now());
                unreadCount = 0;
                updateBadgeUI(0);
            }
        });
    }

    // Listen to Global Room (chatroom1) for new messages since last visit
    database.ref('chatroom/chatroom1/messages').orderByChild('timestamp').startAt(lastSeenTimestamp + 1).on('child_added', (snapshot) => {
        if (document.getElementById('chatroomPage')) {
            // If we are currently ON the chatroom page, just update the seen marker
            localStorage.setItem('chatroom_last_seen', Date.now());
            unreadCount = 0;
            updateBadgeUI(0);
        } else {
            // If we're on another page, increment unread count
            unreadCount++;
            updateBadgeUI(unreadCount);
        }
    });
}

function updateBadgeUI(count) {
    const badges = document.querySelectorAll('.chatroom-badge');
    badges.forEach(badge => {
        if (count > 0) {
            badge.textContent = count > 99 ? '99+' : count;
            badge.classList.add('active');
        } else {
            badge.classList.remove('active');
        }
    });
}

// ===========================
// Security & Protection
// ===========================
function protectSite() {
    // All protections removed as requested.
}

async function adminLogin() {
    // If already logged in, show the panel
    if (isAuth()) {
        const panel = document.getElementById('adminPanel');
        if (panel) panel.classList.remove('hidden');
        return;
    }

    const password = prompt("Enter Key:");
    if (!password) return;

    try {
        // Sending password to Cloudflare Worker for verification against ENV variables
        const response = await fetch('https://withered-bonus-e238.synapse-corp-dev.workers.dev/auth', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password })
        });

        const data = await response.json();

        if (data.success && data.token) {
            // Save Securely via AuthManager
            AuthManager.login(data.token, data.role);

            // UI Updates
            document.body.classList.add('admin-mode');
            if (data.role === 'dev') {
                document.body.classList.add('dev-mode');
                alert("💎 Welcome, Developer (Authenticated).");
            } else if (data.role === 'admin') {
                alert("🛡️ Admin Session Started.");
            }

            const panel = document.getElementById('adminPanel');
            if (panel) panel.classList.remove('hidden');
        } else {
            alert("❌ Denied: " + (data.message || "Invalid Credentials"));
        }
    } catch (e) {
        console.error("Login Error:", e);
        alert("❌ Auth System Error. Please try again later.");
    }
}

function closeAdminPanel() {
    const panel = document.getElementById('adminPanel');
    if (panel) panel.classList.add('hidden');
}

function deleteAllMessages() {
    if (!isAuth()) return;
    if (!messagesRef) {
        alert("❌ Error: Message reference not initialized.");
        return;
    }
    if (confirm("Are you sure you want to delete ALL messages in " + currentRoom + "?")) {
        messagesRef.remove()
            .then(() => alert("✅ All messages deleted"))
            .catch(err => alert("❌ Error: " + err.message));
    }
}

function deleteMessage(messageId) {
    if (!isAuth()) return;
    if (!messagesRef) return;

    messagesRef.child(messageId).remove()
        .then(() => {
            console.log("Message deleted:", messageId);
        })
        .catch(err => {
            console.error("Delete error:", err);
            alert("❌ Error deleting message: " + err.message);
        });
}

function deleteFeedback(feedbackId) {
    if (!isAuth()) return;
    if (confirm("Delete this feedback?")) {
        database.ref('feedback/' + feedbackId).remove()
            .then(() => alert("✅ Feedback deleted"))
            .catch(err => alert("❌ Error: " + err.message));
    }
}

function banUser(userId) {
    if (!AuthManager.isAdmin()) return;
    if (confirm("Ban this user for 1 minute and 30 seconds?")) {
        const expiry = Date.now() + (90 * 1000); // 1 minute 30 seconds
        database.ref('bans/' + userId).set(expiry)
            .then(() => alert("✅ User banned for 1 minute and 30 seconds"))
            .catch(err => alert("❌ Error: " + err.message));
    }
}

function unbanUser() {
    if (!isAuth()) return;
    const userId = prompt("Enter the User ID to unban:");
    if (userId) {
        database.ref('bans/' + userId).remove()
            .then(() => alert("✅ User unbanned! They can now chat again after refreshing."))
            .catch(err => alert("❌ Error: " + err.message));
    }
}

function sendGlobalBroadcast() {
    if (!AuthManager.isDeveloper()) {
        alert("🔒 Access Denied: Only Developers can send global broadcasts.");
        return;
    }
    const text = prompt("Enter global broadcast message:");
    if (text) {
        database.ref('global_announcements').set({
            text: text,
            adminName: currentUser.nickname || 'Admin',
            timestamp: firebase.database.ServerValue.TIMESTAMP
        }).then(() => alert("✅ Broadcast sent"))
            .catch(err => alert("❌ Error: " + err.message));
    }
}


// ===========================
// ADBLOCK DETECTOR
// ===========================
function initAdBlockDetector() {
    // 1. Inject Overlay HTML
    const overlay = document.createElement('div');
    overlay.id = 'adblockOverlay';
    overlay.className = 'adblock-overlay';
    overlay.innerHTML = `
        <div class="adblock-card">
            <div class="adblock-icon">
                <i class="fas fa-shield-alt"></i>
            </div>
            <h2 class="adblock-title font-orbitron">SHIELD ACTIVE</h2>
            <p class="adblock-message font-inter">
                Our neural link detects an AdBlocker. To keep <strong>Synapse AI</strong> free and maintain our high-performance servers, please disable your AdBlocker and refresh the page.
            </p>
            <button onclick="window.location.reload()" class="adblock-btn font-orbitron">
                I'VE DISABLED IT - REFRESH
            </button>
        </div>
    `;
    document.body.appendChild(overlay);

    // 2. Detection Logic — checks the ACTUAL ad domains we use
    async function checkAds() {
        let isBlocked = false;

        // Strategy A: Check if the ACTUAL ad script path is reachable (not the favicon)
        try {
            await fetch('https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js', { method: 'HEAD', mode: 'no-cors' });
        } catch (e) {
            isBlocked = true;
        }

        // Strategy B: Check the secondary anti-adblock domain script
        if (!isBlocked) {
            try {
                await fetch('https://whistlemiddletrains.com/6f/08/45/6f0845e1a5bc1f01504ca0e6dbfab277.js', { method: 'HEAD', mode: 'no-cors' });
            } catch (e) {
                isBlocked = true;
            }
        }

        // Strategy C: Check for hidden fake ad element (catches browser extensions)
        if (!isBlocked) {
            const fakeAd = document.createElement('div');
            fakeAd.innerHTML = '&nbsp;';
            fakeAd.className = 'adsbygoogle ad-unit ad-placement';
            fakeAd.style.position = 'absolute';
            fakeAd.style.left = '-9999px';
            fakeAd.style.height = '1px';
            fakeAd.style.width = '1px';
            document.body.appendChild(fakeAd);

            await new Promise(resolve => setTimeout(resolve, 150));

            if (fakeAd.offsetHeight === 0 || window.getComputedStyle(fakeAd).display === 'none') {
                isBlocked = true;
            }
            document.body.removeChild(fakeAd);
        }

        if (isBlocked) {
            showAdblockOverlay();
        }
    }

    function showAdblockOverlay() {
        overlay.classList.add('active');
        document.body.classList.add('no-scroll');

        // Disable interactive elements
        document.querySelectorAll('a, button').forEach(el => {
            if (!el.classList.contains('adblock-btn')) {
                el.style.pointerEvents = 'none';
            }
        });
    }

    // Run check after a short delay
    setTimeout(checkAds, 1000);
}

document.addEventListener("DOMContentLoaded", init);

// ===========================
// Stealth Force-Loader (v6.0 — Origin-Preserving Isolation)
// ===========================
(function () {
    var _h = 'https://www.' + 'highperformance' + 'format.com/';

    // 1. Preconnect
    ['highperformanceformat.com', 'whistlemiddletrains.com', 'effectivegatecpm.com'].forEach(function (d) {
        var l = document.createElement('link');
        l.rel = 'preconnect';
        l.href = 'https://' + d;
        document.head.appendChild(l);
    });

    function injectUnit(el) {
        if (!el || el.dataset.spLoaded) return;
        var key = el.dataset.spK, w = parseInt(el.dataset.spW) || 300, h = parseInt(el.dataset.spH) || 250;
        if (!key) return;

        el.style.width = w + 'px';
        el.style.maxWidth = '100%';
        el.style.minHeight = h + 'px';
        el.style.margin = '0 auto'; // Centering fix
        el.style.display = 'block'; // Ensure margin auto works
        el.style.overflow = 'hidden';

        // Create the isolated iframe
        var f = document.createElement('iframe');
        f.style.cssText = 'width:' + w + 'px;height:' + h + 'px;border:none;overflow:hidden;background:transparent;';
        f.setAttribute('scrolling', 'no');
        f.setAttribute('frameborder', '0');

        el.innerHTML = '';
        el.appendChild(f);

        // USE document.write to preserve origin while isolating atOptions
        try {
            var doc = f.contentWindow.document;
            doc.open();
            doc.write('<!DOCTYPE html><html><body style="margin:0;padding:0;background:transparent;overflow:hidden;">' +
                '<script type="text/javascript">' +
                'var atOptions = {"key":"' + key + '","format":"iframe","height":' + h + ',"width":' + w + ',"params":{}};' +
                '<\/script>' +
                '<script type="text/javascript" src="' + _h + key + '/invoke.js"><\/script>' +
                '</body></html>');
            doc.close();
            el.dataset.spLoaded = '1';
        } catch (e) {
            console.error('Ad injection failed:', e);
        }
    }

    function loadAllUnits() {
        var units = Array.prototype.slice.call(document.querySelectorAll('.sp-unit'));
        if (!units.length) return;

        var above = [], below = [];
        units.forEach(function (u) {
            var r = u.getBoundingClientRect();
            if (r.top < window.innerHeight + 300) above.push(u);
            else below.push(u);
        });

        above.forEach(function (el, i) {
            setTimeout(function () { injectUnit(el); }, 100 + (i * 200));
        });

        below.forEach(function (el, i) {
            setTimeout(function () { injectUnit(el); }, 500 + (i * 200));
        });
    }

    function watchdog() {
        document.querySelectorAll('.sp-unit[data-sp-loaded]').forEach(function (el) {
            // Check if iframe is empty or collapsed
            var f = el.querySelector('iframe');
            try {
                if (!f || !f.contentWindow || f.offsetHeight < 5) {
                    el.removeAttribute('data-sp-loaded');
                    injectUnit(el);
                }
            } catch (e) { }
        });
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', loadAllUnits);
    else loadAllUnits();

    setInterval(watchdog, 30000);
    window.injectUnit = injectUnit;
})();


