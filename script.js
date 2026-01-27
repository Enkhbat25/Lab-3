// Game State
let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let gameMode = 'pvp'; // 'pvp' or 'ai'
let aiDifficulty = 'medium';
let gameActive = true;

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
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]              // Diagonals
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
            <h3>Player vs Player</h3>
            <p>Total Games: <span>${stats.pvp.player1Wins + stats.pvp.player2Wins + stats.pvp.draws}</span></p>
            <p>Player 1 (X) Wins: <span>${stats.pvp.player1Wins}</span></p>
            <p>Player 2 (O) Wins: <span>${stats.pvp.player2Wins}</span></p>
            <p>Draws: <span>${stats.pvp.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>vs AI - Easy</h3>
            <p>Wins: <span>${stats.ai.easy.wins}</span> | Losses: <span>${stats.ai.easy.losses}</span> | Draws: <span>${stats.ai.easy.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>vs AI - Medium</h3>
            <p>Wins: <span>${stats.ai.medium.wins}</span> | Losses: <span>${stats.ai.medium.losses}</span> | Draws: <span>${stats.ai.medium.draws}</span></p>
        </div>
        <div class="stats-section">
            <h3>vs AI - Hard</h3>
            <p>Wins: <span>${stats.ai.hard.wins}</span> | Losses: <span>${stats.ai.hard.losses}</span> | Draws: <span>${stats.ai.hard.draws}</span></p>
        </div>
    `;
}

function resetStats() {
    if (confirm('Are you sure you want to reset all statistics?')) {
        stats = {
            pvp: { player1Wins: 0, player2Wins: 0, draws: 0 },
            ai: {
                easy: { wins: 0, losses: 0, draws: 0 },
                medium: { wins: 0, losses: 0, draws: 0 },
                hard: { wins: 0, losses: 0, draws: 0 }
            }
        };
        saveStats();
        alert('Statistics reset!');
    }
}

// Game Functions
function startPvP() {
    gameMode = 'pvp';
    modeDisplay.textContent = 'Player vs Player';
    initGame();
    showScreen(gameScreen);
}

function startAI(difficulty) {
    gameMode = 'ai';
    aiDifficulty = difficulty;
    modeDisplay.textContent = `vs AI (${difficulty})`;
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
    if (gameMode === 'pvp') {
        turnDisplay.textContent = `${currentPlayer === 'X' ? 'Player 1' : 'Player 2'}'s turn (${currentPlayer})`;
    } else {
        turnDisplay.textContent = currentPlayer === 'X' ? `Your turn (X)` : 'AI thinking...';
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
            // Highlight winning cells
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
        resultDisplay.textContent = "It's a Draw!";
        resultDisplay.className = 'draw';
        turnDisplay.textContent = 'Game Over';

        if (gameMode === 'pvp') {
            stats.pvp.draws++;
        } else {
            stats.ai[aiDifficulty].draws++;
        }
    } else {
        if (gameMode === 'pvp') {
            const playerNum = result === 'X' ? 1 : 2;
            resultDisplay.textContent = `Player ${playerNum} (${result}) Wins!`;
            resultDisplay.className = 'win';
            if (result === 'X') {
                stats.pvp.player1Wins++;
            } else {
                stats.pvp.player2Wins++;
            }
        } else {
            if (result === 'X') {
                resultDisplay.textContent = 'You Win!';
                resultDisplay.className = 'win';
                stats.ai[aiDifficulty].wins++;
            } else {
                resultDisplay.textContent = 'AI Wins!';
                resultDisplay.className = 'lose';
                stats.ai[aiDifficulty].losses++;
            }
        }
        turnDisplay.textContent = 'Game Over';
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
    // Check if AI can win
    for (const move of available) {
        board[move] = 'O';
        if (checkWinnerSimple() === 'O') {
            board[move] = '';
            return move;
        }
        board[move] = '';
    }

    // Block player win
    for (const move of available) {
        board[move] = 'X';
        if (checkWinnerSimple() === 'X') {
            board[move] = '';
            return move;
        }
        board[move] = '';
    }

    // Take center
    if (available.includes(4)) return 4;

    // Take corner
    const corners = [0, 2, 6, 8].filter(c => available.includes(c));
    if (corners.length > 0) {
        return corners[Math.floor(Math.random() * corners.length)];
    }

    // Random
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
