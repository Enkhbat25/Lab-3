// Translations
const translations = {
    en: {
        title: 'Tic-Tac-Toe',
        mainMenu: 'Main Menu',
        pvp: 'Player vs Player',
        pvai: 'Player vs AI',
        viewStats: 'View Statistics',
        resetStats: 'Reset Statistics',
        selectDifficulty: 'Select Difficulty',
        easy: 'Easy',
        medium: 'Medium',
        hard: 'Hard (Unbeatable)',
        back: 'Back',
        playAgain: 'Play Again',
        mainMenuBtn: 'Main Menu',
        statistics: 'Statistics',
        lightMode: '☀️ Light Mode',
        darkMode: '🌙 Dark Mode',
        player1Turn: "Player 1's turn (X)",
        player2Turn: "Player 2's turn (O)",
        yourTurn: 'Your turn (X)',
        aiThinking: 'AI thinking...',
        gameOver: 'Game Over',
        youWin: 'You Win!',
        aiWins: 'AI Wins!',
        draw: "It's a Draw!",
        player1Wins: 'Player 1 (X) Wins!',
        player2Wins: 'Player 2 (O) Wins!',
        pvpMode: 'Player vs Player',
        vsAI: 'vs AI',
        confirmReset: 'Are you sure you want to reset all statistics?',
        statsReset: 'Statistics reset!',
        statsPvP: 'Player vs Player',
        totalGames: 'Total Games',
        p1Wins: 'Player 1 (X) Wins',
        p2Wins: 'Player 2 (O) Wins',
        draws: 'Draws',
        wins: 'Wins',
        losses: 'Losses',
        vsAIEasy: 'vs AI - Easy',
        vsAIMedium: 'vs AI - Medium',
        vsAIHard: 'vs AI - Hard'
    },
    mn: {
        title: 'Икс-Тэг',
        mainMenu: 'Үндсэн цэс',
        pvp: 'Тоглогч vs Тоглогч',
        pvai: 'Тоглогч vs AI',
        viewStats: 'Статистик харах',
        resetStats: 'Статистик устгах',
        selectDifficulty: 'Түвшин сонгох',
        easy: 'Амархан',
        medium: 'Дунд',
        hard: 'Хэцүү (Ялагдашгүй)',
        back: 'Буцах',
        playAgain: 'Дахин тоглох',
        mainMenuBtn: 'Үндсэн цэс',
        statistics: 'Статистик',
        lightMode: '☀️ Цайвар горим',
        darkMode: '🌙 Харанхуй горим',
        player1Turn: 'Тоглогч 1-ийн ээлж (X)',
        player2Turn: 'Тоглогч 2-ийн ээлж (O)',
        yourTurn: 'Таны ээлж (X)',
        aiThinking: 'AI бодож байна...',
        gameOver: 'Тоглоом дууслаа',
        youWin: 'Та яллаа!',
        aiWins: 'AI яллаа!',
        draw: 'Тэнцлээ!',
        player1Wins: 'Тоглогч 1 (X) яллаа!',
        player2Wins: 'Тоглогч 2 (O) яллаа!',
        pvpMode: 'Тоглогч vs Тоглогч',
        vsAI: 'vs AI',
        confirmReset: 'Та статистикийг устгахдаа итгэлтэй байна уу?',
        statsReset: 'Статистик устгагдлаа!',
        statsPvP: 'Тоглогч vs Тоглогч',
        totalGames: 'Нийт тоглолт',
        p1Wins: 'Тоглогч 1 (X) ялалт',
        p2Wins: 'Тоглогч 2 (O) ялалт',
        draws: 'Тэнцээ',
        wins: 'Ялалт',
        losses: 'Ялагдал',
        vsAIEasy: 'vs AI - Амархан',
        vsAIMedium: 'vs AI - Дунд',
        vsAIHard: 'vs AI - Хэцүү'
    },
    ru: {
        title: 'Крестики-Нолики',
        mainMenu: 'Главное меню',
        pvp: 'Игрок против Игрока',
        pvai: 'Игрок против ИИ',
        viewStats: 'Статистика',
        resetStats: 'Сбросить статистику',
        selectDifficulty: 'Выберите сложность',
        easy: 'Легко',
        medium: 'Средне',
        hard: 'Сложно (Непобедимый)',
        back: 'Назад',
        playAgain: 'Играть снова',
        mainMenuBtn: 'Главное меню',
        statistics: 'Статистика',
        lightMode: '☀️ Светлая тема',
        darkMode: '🌙 Тёмная тема',
        player1Turn: 'Ход Игрока 1 (X)',
        player2Turn: 'Ход Игрока 2 (O)',
        yourTurn: 'Ваш ход (X)',
        aiThinking: 'ИИ думает...',
        gameOver: 'Игра окончена',
        youWin: 'Вы победили!',
        aiWins: 'ИИ победил!',
        draw: 'Ничья!',
        player1Wins: 'Игрок 1 (X) победил!',
        player2Wins: 'Игрок 2 (O) победил!',
        pvpMode: 'Игрок против Игрока',
        vsAI: 'против ИИ',
        confirmReset: 'Вы уверены, что хотите сбросить статистику?',
        statsReset: 'Статистика сброшена!',
        statsPvP: 'Игрок против Игрока',
        totalGames: 'Всего игр',
        p1Wins: 'Побед Игрока 1 (X)',
        p2Wins: 'Побед Игрока 2 (O)',
        draws: 'Ничьих',
        wins: 'Победы',
        losses: 'Поражения',
        vsAIEasy: 'против ИИ - Легко',
        vsAIMedium: 'против ИИ - Средне',
        vsAIHard: 'против ИИ - Сложно'
    },
    ko: {
        title: '틱택토',
        mainMenu: '메인 메뉴',
        pvp: '플레이어 대 플레이어',
        pvai: '플레이어 대 AI',
        viewStats: '통계 보기',
        resetStats: '통계 초기화',
        selectDifficulty: '난이도 선택',
        easy: '쉬움',
        medium: '보통',
        hard: '어려움 (무적)',
        back: '뒤로',
        playAgain: '다시 하기',
        mainMenuBtn: '메인 메뉴',
        statistics: '통계',
        lightMode: '☀️ 라이트 모드',
        darkMode: '🌙 다크 모드',
        player1Turn: '플레이어 1 차례 (X)',
        player2Turn: '플레이어 2 차례 (O)',
        yourTurn: '당신의 차례 (X)',
        aiThinking: 'AI 생각 중...',
        gameOver: '게임 종료',
        youWin: '승리!',
        aiWins: 'AI 승리!',
        draw: '무승부!',
        player1Wins: '플레이어 1 (X) 승리!',
        player2Wins: '플레이어 2 (O) 승리!',
        pvpMode: '플레이어 대 플레이어',
        vsAI: 'vs AI',
        confirmReset: '통계를 초기화하시겠습니까?',
        statsReset: '통계가 초기화되었습니다!',
        statsPvP: '플레이어 대 플레이어',
        totalGames: '총 게임',
        p1Wins: '플레이어 1 (X) 승리',
        p2Wins: '플레이어 2 (O) 승리',
        draws: '무승부',
        wins: '승리',
        losses: '패배',
        vsAIEasy: 'vs AI - 쉬움',
        vsAIMedium: 'vs AI - 보통',
        vsAIHard: 'vs AI - 어려움'
    },
    ja: {
        title: '三目並べ',
        mainMenu: 'メインメニュー',
        pvp: 'プレイヤー対プレイヤー',
        pvai: 'プレイヤー対AI',
        viewStats: '統計を見る',
        resetStats: '統計をリセット',
        selectDifficulty: '難易度を選択',
        easy: '簡単',
        medium: '普通',
        hard: '難しい（無敵）',
        back: '戻る',
        playAgain: 'もう一度',
        mainMenuBtn: 'メインメニュー',
        statistics: '統計',
        lightMode: '☀️ ライトモード',
        darkMode: '🌙 ダークモード',
        player1Turn: 'プレイヤー1の番 (X)',
        player2Turn: 'プレイヤー2の番 (O)',
        yourTurn: 'あなたの番 (X)',
        aiThinking: 'AI思考中...',
        gameOver: 'ゲーム終了',
        youWin: '勝利！',
        aiWins: 'AIの勝利！',
        draw: '引き分け！',
        player1Wins: 'プレイヤー1 (X) の勝利！',
        player2Wins: 'プレイヤー2 (O) の勝利！',
        pvpMode: 'プレイヤー対プレイヤー',
        vsAI: '対AI',
        confirmReset: '統計をリセットしてもよろしいですか？',
        statsReset: '統計がリセットされました！',
        statsPvP: 'プレイヤー対プレイヤー',
        totalGames: '総ゲーム数',
        p1Wins: 'プレイヤー1 (X) 勝利',
        p2Wins: 'プレイヤー2 (O) 勝利',
        draws: '引き分け',
        wins: '勝利',
        losses: '敗北',
        vsAIEasy: '対AI - 簡単',
        vsAIMedium: '対AI - 普通',
        vsAIHard: '対AI - 難しい'
    },
    zh: {
        title: '井字棋',
        mainMenu: '主菜单',
        pvp: '玩家对玩家',
        pvai: '玩家对AI',
        viewStats: '查看统计',
        resetStats: '重置统计',
        selectDifficulty: '选择难度',
        easy: '简单',
        medium: '中等',
        hard: '困难（无敌）',
        back: '返回',
        playAgain: '再玩一次',
        mainMenuBtn: '主菜单',
        statistics: '统计',
        lightMode: '☀️ 浅色模式',
        darkMode: '🌙 深色模式',
        player1Turn: '玩家1的回合 (X)',
        player2Turn: '玩家2的回合 (O)',
        yourTurn: '你的回合 (X)',
        aiThinking: 'AI思考中...',
        gameOver: '游戏结束',
        youWin: '你赢了！',
        aiWins: 'AI赢了！',
        draw: '平局！',
        player1Wins: '玩家1 (X) 获胜！',
        player2Wins: '玩家2 (O) 获胜！',
        pvpMode: '玩家对玩家',
        vsAI: '对战AI',
        confirmReset: '确定要重置所有统计数据吗？',
        statsReset: '统计已重置！',
        statsPvP: '玩家对玩家',
        totalGames: '总游戏数',
        p1Wins: '玩家1 (X) 胜利',
        p2Wins: '玩家2 (O) 胜利',
        draws: '平局',
        wins: '胜利',
        losses: '失败',
        vsAIEasy: '对战AI - 简单',
        vsAIMedium: '对战AI - 中等',
        vsAIHard: '对战AI - 困难'
    }
};

// Current language
let currentLang = localStorage.getItem('tictactoe-lang') || 'en';

function t(key) {
    return translations[currentLang][key] || translations['en'][key] || key;
}

function changeLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('tictactoe-lang', lang);
    updateAllText();
    updateThemeButtonText();
    if (gameMode === 'pvp') {
        modeDisplay.textContent = t('pvpMode');
    } else if (gameMode === 'ai') {
        const diffText = t(aiDifficulty);
        modeDisplay.textContent = `${t('vsAI')} (${diffText})`;
    }
    updateTurnDisplay();
}

function updateAllText() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        el.textContent = t(key);
    });
    document.getElementById('lang-select').value = currentLang;
}

function initLanguage() {
    document.getElementById('lang-select').value = currentLang;
    updateAllText();
}

// Game State
let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let gameMode = 'pvp';
let aiDifficulty = 'medium';
let gameActive = true;

// Theme
let isDarkMode = localStorage.getItem('tictactoe-theme') !== 'light';

function initTheme() {
    const themeBtn = document.getElementById('theme-toggle');
    if (!isDarkMode) {
        document.body.classList.add('light-mode');
    }
    updateThemeButtonText();
}

function updateThemeButtonText() {
    const themeBtn = document.getElementById('theme-toggle');
    themeBtn.textContent = isDarkMode ? t('lightMode') : t('darkMode');
}

function toggleTheme() {
    isDarkMode = !isDarkMode;
    if (isDarkMode) {
        document.body.classList.remove('light-mode');
        localStorage.setItem('tictactoe-theme', 'dark');
    } else {
        document.body.classList.add('light-mode');
        localStorage.setItem('tictactoe-theme', 'light');
    }
    updateThemeButtonText();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initLanguage();
});

// DOM Elements
const menuScreen = document.getElementById('menu');
const aiMenuScreen = document.getElementById('ai-menu');
const gameScreen = document.getElementById('game');
const statsScreen = document.getElementById('stats');
const cells = document.querySelectorAll('.cell');
const turnDisplay = document.getElementById('turn-display');
const modeDisplay = document.getElementById('mode-display');
const resultDisplay = document.getElementById('result');

// Win Patterns
const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

// Stats
let stats = loadStats();

function loadStats() {
    const saved = localStorage.getItem('tictactoe-stats');
    if (saved) {
        return JSON.parse(saved);
    }
    return {
        pvp: { player1Wins: 0, player2Wins: 0, draws: 0 },
        ai: {
            easy: { wins: 0, losses: 0, draws: 0 },
            medium: { wins: 0, losses: 0, draws: 0 },
            hard: { wins: 0, losses: 0, draws: 0 }
        }
    };
}

function saveStats() {
    localStorage.setItem('tictactoe-stats', JSON.stringify(stats));
}

// Screen Navigation
function showScreen(screen) {
    menuScreen.classList.add('hidden');
    aiMenuScreen.classList.add('hidden');
    gameScreen.classList.add('hidden');
    statsScreen.classList.add('hidden');
    screen.classList.remove('hidden');
}

function showMenu() {
    showScreen(menuScreen);
}

function showAIMenu() {
    showScreen(aiMenuScreen);
}

function showStats() {
    updateStatsDisplay();
    showScreen(statsScreen);
}

function updateStatsDisplay() {
    const content = document.getElementById('stats-content');
    content.innerHTML = `
        <div class="stats-section">
            <h3>${t('statsPvP')}</h3>
            <p>${t('totalGames')}: <span>${stats.pvp.player1Wins + stats.pvp.player2Wins + stats.pvp.draws}</span></p>
            <p>${t('p1Wins')}: <span>${stats.pvp.player1Wins}</span></p>
            <p>${t('p2Wins')}: <span>${stats.pvp.player2Wins}</span></p>
            <p>${t('draws')}: <span>${stats.pvp.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>${t('vsAIEasy')}</h3>
            <p>${t('wins')}: <span>${stats.ai.easy.wins}</span> | ${t('losses')}: <span>${stats.ai.easy.losses}</span> | ${t('draws')}: <span>${stats.ai.easy.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>${t('vsAIMedium')}</h3>
            <p>${t('wins')}: <span>${stats.ai.medium.wins}</span> | ${t('losses')}: <span>${stats.ai.medium.losses}</span> | ${t('draws')}: <span>${stats.ai.medium.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>${t('vsAIHard')}</h3>
            <p>${t('wins')}: <span>${stats.ai.hard.wins}</span> | ${t('losses')}: <span>${stats.ai.hard.losses}</span> | ${t('draws')}: <span>${stats.ai.hard.draws}</span></p>
        </div>
    `;
}

function resetStats() {
    if (confirm(t('confirmReset'))) {
        stats = {
            pvp: { player1Wins: 0, player2Wins: 0, draws: 0 },
            ai: {
                easy: { wins: 0, losses: 0, draws: 0 },
                medium: { wins: 0, losses: 0, draws: 0 },
                hard: { wins: 0, losses: 0, draws: 0 }
            }
        };
        saveStats();
        alert(t('statsReset'));
    }
}

// Game Functions
function startPvP() {
    gameMode = 'pvp';
    modeDisplay.textContent = t('pvpMode');
    initGame();
    showScreen(gameScreen);
}

function startAI(difficulty) {
    gameMode = 'ai';
    aiDifficulty = difficulty;
    const diffText = t(difficulty);
    modeDisplay.textContent = `${t('vsAI')} (${diffText})`;
    initGame();
    showScreen(gameScreen);
}

function initGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    currentPlayer = 'X';
    gameActive = true;
    resultDisplay.classList.add('hidden');
    resultDisplay.className = 'hidden';

    cells.forEach(cell => {
        cell.textContent = '';
        cell.className = 'cell';
    });

    updateTurnDisplay();
}

function updateTurnDisplay() {
    if (!gameActive) {
        turnDisplay.textContent = t('gameOver');
        return;
    }
    if (gameMode === 'pvp') {
        turnDisplay.textContent = currentPlayer === 'X' ? t('player1Turn') : t('player2Turn');
    } else {
        turnDisplay.textContent = currentPlayer === 'X' ? t('yourTurn') : t('aiThinking');
    }
}

// Cell Click Handler
cells.forEach(cell => {
    cell.addEventListener('click', () => handleCellClick(cell));
});

function handleCellClick(cell) {
    const index = parseInt(cell.dataset.index);

    if (board[index] !== '' || !gameActive) return;
    if (gameMode === 'ai' && currentPlayer === 'O') return;

    makeMove(index);

    if (gameActive && gameMode === 'ai') {
        setTimeout(() => {
            if (gameActive) {
                const aiMove = getAIMove();
                if (aiMove !== null) {
                    makeMove(aiMove);
                }
            }
        }, 500);
    }
}

function makeMove(index) {
    board[index] = currentPlayer;
    const cell = cells[index];
    cell.textContent = currentPlayer;
    cell.classList.add(currentPlayer.toLowerCase());

    const winner = checkWinner();
    if (winner) {
        endGame(winner);
    } else if (board.every(cell => cell !== '')) {
        endGame('draw');
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        updateTurnDisplay();
    }
}

function checkWinner() {
    for (const pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            cells[a].classList.add('winner');
            cells[b].classList.add('winner');
            cells[c].classList.add('winner');
            return board[a];
        }
    }
    return null;
}

function endGame(result) {
    gameActive = false;

    if (result === 'draw') {
        resultDisplay.textContent = t('draw');
        resultDisplay.className = 'draw';
        turnDisplay.textContent = t('gameOver');

        if (gameMode === 'pvp') {
            stats.pvp.draws++;
        } else {
            stats.ai[aiDifficulty].draws++;
        }
    } else {
        if (gameMode === 'pvp') {
            resultDisplay.textContent = result === 'X' ? t('player1Wins') : t('player2Wins');
            resultDisplay.className = 'win';
            if (result === 'X') {
                stats.pvp.player1Wins++;
            } else {
                stats.pvp.player2Wins++;
            }
        } else {
            if (result === 'X') {
                resultDisplay.textContent = t('youWin');
                resultDisplay.className = 'win';
                stats.ai[aiDifficulty].wins++;
            } else {
                resultDisplay.textContent = t('aiWins');
                resultDisplay.className = 'lose';
                stats.ai[aiDifficulty].losses++;
            }
        }
        turnDisplay.textContent = t('gameOver');
    }

    resultDisplay.classList.remove('hidden');
    saveStats();
}

function restartGame() {
    initGame();
}

// AI Logic
function getAIMove() {
    const available = board.map((cell, i) => cell === '' ? i : null).filter(i => i !== null);
    if (available.length === 0) return null;

    switch (aiDifficulty) {
        case 'easy':
            return getEasyMove(available);
        case 'medium':
            return getMediumMove(available);
        case 'hard':
            return getHardMove();
        default:
            return getEasyMove(available);
    }
}

function getEasyMove(available) {
    return available[Math.floor(Math.random() * available.length)];
}

function getMediumMove(available) {
    for (const move of available) {
        board[move] = 'O';
        if (checkWinnerSimple() === 'O') {
            board[move] = '';
            return move;
        }
        board[move] = '';
    }

    for (const move of available) {
        board[move] = 'X';
        if (checkWinnerSimple() === 'X') {
            board[move] = '';
            return move;
        }
        board[move] = '';
    }

    if (available.includes(4)) return 4;

    const corners = [0, 2, 6, 8].filter(c => available.includes(c));
    if (corners.length > 0) {
        return corners[Math.floor(Math.random() * corners.length)];
    }

    return getEasyMove(available);
}

function getHardMove() {
    let bestScore = -Infinity;
    let bestMove = null;

    const available = board.map((cell, i) => cell === '' ? i : null).filter(i => i !== null);

    for (const move of available) {
        board[move] = 'O';
        const score = minimax(board, 0, false);
        board[move] = '';

        if (score > bestScore) {
            bestScore = score;
            bestMove = move;
        }
    }

    return bestMove;
}

function minimax(board, depth, isMaximizing) {
    const winner = checkWinnerSimple();
    if (winner === 'O') return 10 - depth;
    if (winner === 'X') return depth - 10;
    if (board.every(cell => cell !== '')) return 0;

    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'O';
                const score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'X';
                const score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

function checkWinnerSimple() {
    for (const pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            return board[a];
        }
    }
    return null;
}
