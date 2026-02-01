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
        vsAIHard: 'vs AI - Hard',
        help: 'Help',
        helpTitle: 'How to Play',
        helpRulesTitle: 'Game Rules',
        helpRule1: 'The game is played on a 3x3 grid',
        helpRule2: 'Players take turns placing X or O',
        helpRule3: 'First to get 3 in a row wins!',
        helpRule4: 'If all cells are filled with no winner, it\'s a draw',
        helpModesTitle: 'Game Modes',
        helpPvpDesc: 'Play with a friend',
        helpEasyDesc: 'AI makes random moves',
        helpMediumDesc: 'AI plays smart sometimes',
        helpHardDesc: 'Unbeatable AI using Minimax',
        helpTipsTitle: 'Tips',
        helpTip1: 'Control the center for an advantage',
        helpTip2: 'Watch for opponent\'s winning moves',
        helpTip3: 'Try to create two ways to win',
        soundOn: '🔊 Sound On',
        soundOff: '🔇 Sound Off',
        undo: 'Undo',
        whoGoesFirst: 'Who goes first?',
        youFirst: 'You (X)',
        aiFirst: 'AI (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: 'Get',
        winConditionSuffix: 'in a row to win!',
        boardSize: 'Board Size'
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
        vsAIHard: 'vs AI - Хэцүү',
        help: 'Тусламж',
        helpTitle: 'Тоглох заавар',
        helpRulesTitle: 'Тоглоомын дүрэм',
        helpRule1: 'Тоглоом нь 3x3 хүснэгтэн дээр тоглогдоно',
        helpRule2: 'Тоглогчид ээлжлэн X эсвэл O тавина',
        helpRule3: 'Эхлээд 3-ыг дараалан цуглуулсан хүн яллана!',
        helpRule4: 'Бүх нүд дүүрч ялагч гараагүй бол тэнцээ',
        helpModesTitle: 'Тоглоомын горимууд',
        helpPvpDesc: 'Найзтайгаа тоглох',
        helpEasyDesc: 'AI санамсаргүй тоглоно',
        helpMediumDesc: 'AI заримдаа ухаалаг тоглоно',
        helpHardDesc: 'Ялагдашгүй AI (Minimax)',
        helpTipsTitle: 'Зөвлөгөө',
        helpTip1: 'Төв нүдийг эзэмшвэл давуу талтай',
        helpTip2: 'Өрсөлдөгчийн ялах боломжийг хянаарай',
        helpTip3: 'Хоёр ялах замыг бий болго',
        soundOn: '🔊 Дуу асаалттай',
        soundOff: '🔇 Дуу унтраалттай',
        undo: 'Буцаах',
        whoGoesFirst: 'Хэн эхлэх вэ?',
        youFirst: 'Та (X)',
        aiFirst: 'AI (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: '',
        winConditionSuffix: 'дараалан цуглуулж ял!',
        boardSize: 'Хүснэгтийн хэмжээ'
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
        vsAIHard: 'против ИИ - Сложно',
        help: 'Помощь',
        helpTitle: 'Как играть',
        helpRulesTitle: 'Правила игры',
        helpRule1: 'Игра ведётся на поле 3x3',
        helpRule2: 'Игроки по очереди ставят X или O',
        helpRule3: 'Первый, кто соберёт 3 в ряд, побеждает!',
        helpRule4: 'Если все клетки заполнены без победителя - ничья',
        helpModesTitle: 'Режимы игры',
        helpPvpDesc: 'Играть с другом',
        helpEasyDesc: 'ИИ делает случайные ходы',
        helpMediumDesc: 'ИИ иногда играет умно',
        helpHardDesc: 'Непобедимый ИИ (Minimax)',
        helpTipsTitle: 'Советы',
        helpTip1: 'Контролируйте центр для преимущества',
        helpTip2: 'Следите за выигрышными ходами противника',
        helpTip3: 'Создавайте две возможности для победы',
        soundOn: '🔊 Звук вкл',
        soundOff: '🔇 Звук выкл',
        undo: 'Отменить',
        whoGoesFirst: 'Кто ходит первым?',
        youFirst: 'Вы (X)',
        aiFirst: 'ИИ (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: 'Соберите',
        winConditionSuffix: 'в ряд чтобы победить!',
        boardSize: 'Размер поля'
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
        vsAIHard: 'vs AI - 어려움',
        help: '도움말',
        helpTitle: '게임 방법',
        helpRulesTitle: '게임 규칙',
        helpRule1: '3x3 격자에서 게임을 합니다',
        helpRule2: '플레이어가 번갈아 X 또는 O를 놓습니다',
        helpRule3: '먼저 3개를 연속으로 만들면 승리!',
        helpRule4: '모든 칸이 차면 무승부입니다',
        helpModesTitle: '게임 모드',
        helpPvpDesc: '친구와 함께 플레이',
        helpEasyDesc: 'AI가 무작위로 움직입니다',
        helpMediumDesc: 'AI가 가끔 똑똑하게 플레이합니다',
        helpHardDesc: '무적 AI (Minimax)',
        helpTipsTitle: '팁',
        helpTip1: '중앙을 점령하면 유리합니다',
        helpTip2: '상대방의 승리 수를 주시하세요',
        helpTip3: '두 가지 승리 방법을 만드세요',
        soundOn: '🔊 소리 켜짐',
        soundOff: '🔇 소리 꺼짐',
        undo: '실행 취소',
        whoGoesFirst: '누가 먼저 시작할까요?',
        youFirst: '당신 (X)',
        aiFirst: 'AI (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: '',
        winConditionSuffix: '개를 연속으로 만들면 승리!',
        boardSize: '보드 크기'
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
        vsAIHard: '対AI - 難しい',
        help: 'ヘルプ',
        helpTitle: '遊び方',
        helpRulesTitle: 'ゲームルール',
        helpRule1: '3x3のマス目でプレイします',
        helpRule2: 'プレイヤーは交互にXまたはOを置きます',
        helpRule3: '先に3つ並べた人の勝ち！',
        helpRule4: '全マスが埋まって勝者なしなら引き分け',
        helpModesTitle: 'ゲームモード',
        helpPvpDesc: '友達と対戦',
        helpEasyDesc: 'AIがランダムに動きます',
        helpMediumDesc: 'AIが時々賢くプレイします',
        helpHardDesc: '無敵AI（Minimax）',
        helpTipsTitle: 'ヒント',
        helpTip1: '中央を取ると有利です',
        helpTip2: '相手の勝ち筋に注意',
        helpTip3: '2つの勝ち筋を作りましょう',
        soundOn: '🔊 サウンドON',
        soundOff: '🔇 サウンドOFF',
        undo: '元に戻す',
        whoGoesFirst: '先手を選択',
        youFirst: 'あなた (X)',
        aiFirst: 'AI (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: '',
        winConditionSuffix: '個並べて勝利!',
        boardSize: 'ボードサイズ'
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
        vsAIHard: '对战AI - 困难',
        help: '帮助',
        helpTitle: '游戏玩法',
        helpRulesTitle: '游戏规则',
        helpRule1: '在3x3的格子上进行游戏',
        helpRule2: '玩家轮流放置X或O',
        helpRule3: '先连成3个的玩家获胜！',
        helpRule4: '所有格子填满且无获胜者则为平局',
        helpModesTitle: '游戏模式',
        helpPvpDesc: '与朋友对战',
        helpEasyDesc: 'AI随机移动',
        helpMediumDesc: 'AI有时会聪明地下棋',
        helpHardDesc: '无敌AI（Minimax算法）',
        helpTipsTitle: '小贴士',
        helpTip1: '控制中心位置可获得优势',
        helpTip2: '注意对手的获胜机会',
        helpTip3: '尝试创造两种获胜方式',
        soundOn: '🔊 声音开启',
        soundOff: '🔇 声音关闭',
        undo: '撤销',
        whoGoesFirst: '谁先走？',
        youFirst: '你 (X)',
        aiFirst: 'AI (O)',
        size3x3: '3×3',
        size4x4: '4×4',
        size5x5: '5×5',
        winConditionPrefix: '连成',
        winConditionSuffix: '个即可获胜!',
        boardSize: '棋盘大小'
    }
};

// Safe localStorage wrapper
const storage = {
    get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (error) {
            console.warn(`Failed to read ${key} from localStorage:`, error);
            return defaultValue;
        }
    },

    getString(key, defaultValue = null) {
        try {
            return localStorage.getItem(key) ?? defaultValue;
        } catch (error) {
            console.warn(`Failed to read ${key} from localStorage:`, error);
            return defaultValue;
        }
    },

    set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (error) {
            console.warn(`Failed to write ${key} to localStorage:`, error);
            return false;
        }
    },

    setString(key, value) {
        try {
            localStorage.setItem(key, value);
            return true;
        } catch (error) {
            console.warn(`Failed to write ${key} to localStorage:`, error);
            return false;
        }
    },

    remove(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (error) {
            console.warn(`Failed to remove ${key} from localStorage:`, error);
            return false;
        }
    }
};

// Sound System
const AudioContext = window.AudioContext || window.webkitAudioContext;
let audioCtx = null;
let soundEnabled = storage.getString('tictactoe-sound') !== 'false';

function initAudio() {
    if (!audioCtx) {
        audioCtx = new AudioContext();
    }
}

function playTone(frequency, duration, type = 'sine', volume = 0.3) {
    if (!soundEnabled) return;
    initAudio();

    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    oscillator.frequency.value = frequency;
    oscillator.type = type;
    gainNode.gain.setValueAtTime(volume, audioCtx.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);

    oscillator.start(audioCtx.currentTime);
    oscillator.stop(audioCtx.currentTime + duration);
}

function playMoveSound(player) {
    if (player === 'X') {
        playTone(600, 0.1, 'sine', 0.3);
    } else {
        playTone(400, 0.1, 'sine', 0.3);
    }
}

function playWinSound() {
    // Happy ascending melody
    setTimeout(() => playTone(523, 0.15, 'sine', 0.3), 0);    // C5
    setTimeout(() => playTone(659, 0.15, 'sine', 0.3), 150);  // E5
    setTimeout(() => playTone(784, 0.15, 'sine', 0.3), 300);  // G5
    setTimeout(() => playTone(1047, 0.3, 'sine', 0.3), 450);  // C6
}

function playLoseSound() {
    // Sad descending tones
    setTimeout(() => playTone(400, 0.2, 'sine', 0.3), 0);
    setTimeout(() => playTone(300, 0.2, 'sine', 0.3), 200);
    setTimeout(() => playTone(200, 0.4, 'sine', 0.3), 400);
}

function playDrawSound() {
    // Neutral double beep
    setTimeout(() => playTone(440, 0.15, 'triangle', 0.3), 0);
    setTimeout(() => playTone(440, 0.15, 'triangle', 0.3), 200);
}

function playButtonSound() {
    playTone(800, 0.05, 'sine', 0.2);
}

function toggleSound() {
    soundEnabled = !soundEnabled;
    storage.setString('tictactoe-sound', soundEnabled);
    updateSoundButtonText();
    if (soundEnabled) {
        playButtonSound();
    }
}

function updateSoundButtonText() {
    const soundBtn = document.getElementById('sound-toggle');
    if (soundBtn) {
        soundBtn.textContent = soundEnabled ? t('soundOn') : t('soundOff');
    }
}

// Current language
let currentLang = storage.getString('tictactoe-lang', 'en');

function t(key) {
    return translations[currentLang][key] || translations['en'][key] || key;
}

function changeLanguage(lang) {
    currentLang = lang;
    storage.setString('tictactoe-lang', lang);
    updateAllText();
    updateThemeButtonText();
    updateSoundButtonText();
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

// Board Size Configuration
const BOARD_CONFIGS = {
    '3x3': { size: 3, winCondition: 3, label: '3×3' },
    '4x4': { size: 4, winCondition: 4, label: '4×4' },
    '5x5': { size: 5, winCondition: 5, label: '5×5' }
};

let currentBoardConfig = BOARD_CONFIGS['3x3'];
let boardSize = currentBoardConfig.size;
let winCondition = currentBoardConfig.winCondition;

// Game State
let board = Array(boardSize * boardSize).fill('');
let currentPlayer = 'X';
let gameMode = 'pvp';
let aiDifficulty = 'medium';
let gameActive = true;
let moveHistory = [];
let playerGoesFirst = true;
let focusedCellIndex = 0;

// Winning lines cache for performance
const winningLinesCache = new Map();

/**
 * Generate all possible winning lines for an NxN board
 * @param {number} size - Board dimension (e.g., 3, 4, 5)
 * @param {number} winLength - Number in a row needed to win
 * @returns {number[][]} - Array of winning line index arrays
 */
function generateWinningLines(size, winLength) {
    const lines = [];
    const toIndex = (row, col) => row * size + col;

    // Horizontal lines
    for (let row = 0; row < size; row++) {
        for (let startCol = 0; startCol <= size - winLength; startCol++) {
            const line = [];
            for (let i = 0; i < winLength; i++) {
                line.push(toIndex(row, startCol + i));
            }
            lines.push(line);
        }
    }

    // Vertical lines
    for (let col = 0; col < size; col++) {
        for (let startRow = 0; startRow <= size - winLength; startRow++) {
            const line = [];
            for (let i = 0; i < winLength; i++) {
                line.push(toIndex(startRow + i, col));
            }
            lines.push(line);
        }
    }

    // Diagonal lines (top-left to bottom-right)
    for (let startRow = 0; startRow <= size - winLength; startRow++) {
        for (let startCol = 0; startCol <= size - winLength; startCol++) {
            const line = [];
            for (let i = 0; i < winLength; i++) {
                line.push(toIndex(startRow + i, startCol + i));
            }
            lines.push(line);
        }
    }

    // Anti-diagonal lines (top-right to bottom-left)
    for (let startRow = 0; startRow <= size - winLength; startRow++) {
        for (let startCol = winLength - 1; startCol < size; startCol++) {
            const line = [];
            for (let i = 0; i < winLength; i++) {
                line.push(toIndex(startRow + i, startCol - i));
            }
            lines.push(line);
        }
    }

    return lines;
}

/**
 * Get winning lines with caching for performance
 */
function getWinningLines(size, winLength) {
    const key = `${size}-${winLength}`;
    if (!winningLinesCache.has(key)) {
        winningLinesCache.set(key, generateWinningLines(size, winLength));
    }
    return winningLinesCache.get(key);
}

// Haptic feedback utility
function triggerHaptic(pattern = 10) {
    if ('vibrate' in navigator) {
        navigator.vibrate(pattern);
    }
}

// Keyboard navigation for game board
function initKeyboardNavigation() {
    const boardElement = document.getElementById('board');
    if (!boardElement) return;

    boardElement.addEventListener('keydown', handleBoardKeydown);

    // Make cells focusable
    cells.forEach((cell, index) => {
        cell.setAttribute('tabindex', index === 0 ? '0' : '-1');
    });
}

function handleBoardKeydown(e) {
    const gameScreenVisible = !document.getElementById('game').classList.contains('hidden');
    if (!gameScreenVisible) return;

    const totalCells = boardSize * boardSize;
    const currentRow = Math.floor(focusedCellIndex / boardSize);
    const currentCol = focusedCellIndex % boardSize;
    let newIndex = focusedCellIndex;

    switch (e.key) {
        case 'ArrowUp':
            e.preventDefault();
            newIndex = focusedCellIndex - boardSize;
            if (newIndex < 0) newIndex += totalCells; // Wrap to bottom
            break;
        case 'ArrowDown':
            e.preventDefault();
            newIndex = focusedCellIndex + boardSize;
            if (newIndex >= totalCells) newIndex -= totalCells; // Wrap to top
            break;
        case 'ArrowLeft':
            e.preventDefault();
            if (currentCol === 0) {
                newIndex = focusedCellIndex + (boardSize - 1); // Wrap to right
            } else {
                newIndex = focusedCellIndex - 1;
            }
            break;
        case 'ArrowRight':
            e.preventDefault();
            if (currentCol === boardSize - 1) {
                newIndex = focusedCellIndex - (boardSize - 1); // Wrap to left
            } else {
                newIndex = focusedCellIndex + 1;
            }
            break;
        case 'Enter':
        case ' ':
            e.preventDefault();
            if (cells[focusedCellIndex]) {
                handleCellClick(cells[focusedCellIndex]);
            }
            return;
        case 'Escape':
            e.preventDefault();
            newIndex = 0;
            break;
        // Number pad navigation (only works for 3x3)
        case '7': if (boardSize === 3) newIndex = 0; break;
        case '8': if (boardSize === 3) newIndex = 1; break;
        case '9': if (boardSize === 3) newIndex = 2; break;
        case '4': if (boardSize === 3) newIndex = 3; break;
        case '5': if (boardSize === 3) newIndex = 4; break;
        case '6': if (boardSize === 3) newIndex = 5; break;
        case '1': if (boardSize === 3) newIndex = 6; break;
        case '2': if (boardSize === 3) newIndex = 7; break;
        case '3': if (boardSize === 3) newIndex = 8; break;
        default:
            return;
    }

    // Update focus
    if (newIndex !== focusedCellIndex && newIndex >= 0 && newIndex < totalCells) {
        focusedCellIndex = newIndex;
        updateCellFocus();
    }
}

function updateCellFocus() {
    cells.forEach((cell, index) => {
        cell.setAttribute('tabindex', index === focusedCellIndex ? '0' : '-1');
    });
    if (cells[focusedCellIndex]) {
        cells[focusedCellIndex].focus();
    }
}

// Theme
let isDarkMode = storage.getString('tictactoe-theme') !== 'light';

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
        storage.setString('tictactoe-theme', 'dark');
    } else {
        document.body.classList.add('light-mode');
        storage.setString('tictactoe-theme', 'light');
    }
    updateThemeButtonText();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initLanguage();
    updateSoundButtonText();
    initKeyboardNavigation();
    initAccessibility();
});

// Accessibility initialization
function initAccessibility() {
    // Add ARIA attributes to game board
    const boardElement = document.getElementById('board');
    if (boardElement) {
        boardElement.setAttribute('role', 'grid');
        boardElement.setAttribute('aria-label', `${boardSize} by ${boardSize} tic-tac-toe game board`);
        boardElement.setAttribute('aria-describedby', 'turn-display');
    }

    // Add ARIA attributes to cells
    cells.forEach((cell, index) => {
        cell.setAttribute('role', 'gridcell');
        cell.setAttribute('aria-label', `Cell ${index + 1}, empty`);
        cell.setAttribute('aria-disabled', 'false');
    });

    // Add live region for turn display
    const turnDisplay = document.getElementById('turn-display');
    if (turnDisplay) {
        turnDisplay.setAttribute('aria-live', 'polite');
        turnDisplay.setAttribute('aria-atomic', 'true');
    }

    // Add live region for result display
    const resultDisplay = document.getElementById('result');
    if (resultDisplay) {
        resultDisplay.setAttribute('aria-live', 'assertive');
        resultDisplay.setAttribute('aria-atomic', 'true');
    }
}

// Update cell accessibility after move
function updateCellAccessibility(index, player) {
    const cell = cells[index];
    if (cell) {
        cell.setAttribute('aria-label', `Cell ${index + 1}, marked ${player}`);
        cell.setAttribute('aria-pressed', 'true');
        cell.setAttribute('aria-disabled', 'true');
    }
}

// Update all cells accessibility when game ends
function updateAllCellsDisabled(disabled) {
    cells.forEach((cell, index) => {
        cell.setAttribute('aria-disabled', disabled ? 'true' : (board[index] !== '' ? 'true' : 'false'));
    });
}

// Reset cell accessibility for new game
function resetCellAccessibility() {
    cells.forEach((cell, index) => {
        cell.setAttribute('aria-label', `Cell ${index + 1}, empty`);
        cell.setAttribute('aria-pressed', 'false');
        cell.setAttribute('aria-disabled', 'false');
    });
}

// DOM Elements
const menuScreen = document.getElementById('menu');
const aiMenuScreen = document.getElementById('ai-menu');
const gameScreen = document.getElementById('game');
const statsScreen = document.getElementById('stats');
const helpScreen = document.getElementById('help');
let cells = document.querySelectorAll('.cell');
const turnDisplay = document.getElementById('turn-display');
const modeDisplay = document.getElementById('mode-display');
const resultDisplay = document.getElementById('result');
const boardElement = document.getElementById('board');

/**
 * Generate board cells dynamically based on current board size
 */
function generateBoardCells() {
    // Clear existing cells (except the SVG)
    const svg = document.getElementById('winning-line');
    boardElement.innerHTML = '';
    if (svg) boardElement.appendChild(svg);

    // Update CSS grid
    boardElement.style.gridTemplateColumns = `repeat(${boardSize}, 1fr)`;
    boardElement.setAttribute('data-size', boardSize);

    // Create new cells
    const totalCells = boardSize * boardSize;
    for (let i = 0; i < totalCells; i++) {
        const cell = document.createElement('div');
        cell.className = 'cell';
        cell.setAttribute('data-index', i);
        cell.addEventListener('click', () => handleCellClick(cell));
        boardElement.insertBefore(cell, svg);
    }

    // Update cells reference
    cells = document.querySelectorAll('.cell');

    // Re-initialize keyboard navigation and accessibility
    initKeyboardNavigation();
    initAccessibility();
}

/**
 * Change board size configuration
 */
function changeBoardSize(configKey) {
    if (!BOARD_CONFIGS[configKey]) return;

    currentBoardConfig = BOARD_CONFIGS[configKey];
    boardSize = currentBoardConfig.size;
    winCondition = currentBoardConfig.winCondition;

    // Update size selector UI
    updateBoardSizeSelector();

    // Regenerate board
    generateBoardCells();

    // Reset game
    initGame();
}

/**
 * Update board size selector button states
 */
function updateBoardSizeSelector() {
    document.querySelectorAll('.size-option').forEach(btn => {
        const size = btn.getAttribute('data-size');
        if (size === `${boardSize}x${boardSize}`) {
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');
        } else {
            btn.classList.remove('active');
            btn.setAttribute('aria-pressed', 'false');
        }
    });

    // Update win condition display
    const winConditionNumber = document.getElementById('win-condition-number');
    if (winConditionNumber) {
        winConditionNumber.textContent = winCondition;
    }
}

// Get current winning patterns (dynamic based on board size)
function getWinPatterns() {
    return getWinningLines(boardSize, winCondition);
}

// Stats (per board size)
let stats = loadStats();

function getDefaultBoardStats() {
    return {
        pvp: { player1Wins: 0, player2Wins: 0, draws: 0 },
        ai: {
            easy: { wins: 0, losses: 0, draws: 0 },
            medium: { wins: 0, losses: 0, draws: 0 },
            hard: { wins: 0, losses: 0, draws: 0 }
        }
    };
}

function loadStats() {
    return storage.get('tictactoe-stats-v2', {
        '3x3': getDefaultBoardStats(),
        '4x4': getDefaultBoardStats(),
        '5x5': getDefaultBoardStats()
    });
}

function getCurrentStats() {
    const key = `${boardSize}x${boardSize}`;
    if (!stats[key]) {
        stats[key] = getDefaultBoardStats();
    }
    return stats[key];
}

function saveStats() {
    storage.set('tictactoe-stats', stats);
}

// Screen Navigation
function showScreen(screen) {
    menuScreen.classList.add('hidden');
    aiMenuScreen.classList.add('hidden');
    gameScreen.classList.add('hidden');
    statsScreen.classList.add('hidden');
    helpScreen.classList.add('hidden');
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

function showHelp() {
    showScreen(helpScreen);
}

function updateStatsDisplay() {
    const content = document.getElementById('stats-content');
    let html = '';

    // Generate stats for each board size
    const sizes = ['3x3', '4x4', '5x5'];
    for (const size of sizes) {
        const sizeStats = stats[size] || getDefaultBoardStats();
        html += `
            <div class="stats-board-section">
                <h3 class="board-size-header">${size}</h3>
                <div class="stats-section">
                    <h4>${t('statsPvP')}</h4>
                    <p>${t('totalGames')}: <span>${sizeStats.pvp.player1Wins + sizeStats.pvp.player2Wins + sizeStats.pvp.draws}</span></p>
                    <p>${t('p1Wins')}: <span>${sizeStats.pvp.player1Wins}</span> | ${t('p2Wins')}: <span>${sizeStats.pvp.player2Wins}</span> | ${t('draws')}: <span>${sizeStats.pvp.draws}</span></p>
                </div>
                <div class="stats-section">
                    <h4>${t('vsAI')}</h4>
                    <p><strong>${t('easy')}:</strong> ${t('wins')}: <span>${sizeStats.ai.easy.wins}</span> | ${t('losses')}: <span>${sizeStats.ai.easy.losses}</span> | ${t('draws')}: <span>${sizeStats.ai.easy.draws}</span></p>
                    <p><strong>${t('medium')}:</strong> ${t('wins')}: <span>${sizeStats.ai.medium.wins}</span> | ${t('losses')}: <span>${sizeStats.ai.medium.losses}</span> | ${t('draws')}: <span>${sizeStats.ai.medium.draws}</span></p>
                    <p><strong>${t('hard')}:</strong> ${t('wins')}: <span>${sizeStats.ai.hard.wins}</span> | ${t('losses')}: <span>${sizeStats.ai.hard.losses}</span> | ${t('draws')}: <span>${sizeStats.ai.hard.draws}</span></p>
                </div>
            </div>
        `;
    }

    content.innerHTML = html;
}

function resetStats() {
    if (confirm(t('confirmReset'))) {
        stats = {
            '3x3': getDefaultBoardStats(),
            '4x4': getDefaultBoardStats(),
            '5x5': getDefaultBoardStats()
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
    showFirstMoveChoice();
}

function showFirstMoveChoice() {
    document.getElementById('first-move-modal').classList.remove('hidden');
}

function hideFirstMoveChoice() {
    document.getElementById('first-move-modal').classList.add('hidden');
}

function selectFirstMove(playerFirst) {
    playerGoesFirst = playerFirst;
    hideFirstMoveChoice();
    initGame();
    showScreen(gameScreen);
}

function initGame() {
    board = Array(boardSize * boardSize).fill('');
    currentPlayer = 'X';
    gameActive = true;
    moveHistory = [];
    focusedCellIndex = 0;
    resultDisplay.classList.add('hidden');
    resultDisplay.className = 'hidden';

    cells.forEach(cell => {
        cell.textContent = '';
        cell.className = 'cell';
    });

    // Hide winning line from previous game
    hideWinningLine();

    // Reset accessibility attributes
    resetCellAccessibility();

    updateUndoButton();
    updateTurnDisplay();
    updateBoardSizeSelector();

    // If AI goes first, make AI move
    if (gameMode === 'ai' && !playerGoesFirst) {
        currentPlayer = 'O';
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

function updateUndoButton() {
    const undoBtn = document.getElementById('undo-btn');
    if (undoBtn) {
        // Disable if no moves or game is over
        const canUndo = moveHistory.length > 0 && gameActive;
        undoBtn.disabled = !canUndo;
        undoBtn.style.opacity = canUndo ? '1' : '0.5';
        undoBtn.style.cursor = canUndo ? 'pointer' : 'not-allowed';
    }
}

function undoMove() {
    if (moveHistory.length === 0 || !gameActive) return;

    if (gameMode === 'ai') {
        // In AI mode, undo both AI's move and player's move
        if (moveHistory.length >= 2) {
            // Undo AI's move
            const aiMove = moveHistory.pop();
            board[aiMove.index] = '';
            cells[aiMove.index].textContent = '';
            cells[aiMove.index].className = 'cell';

            // Undo player's move
            const playerMove = moveHistory.pop();
            board[playerMove.index] = '';
            cells[playerMove.index].textContent = '';
            cells[playerMove.index].className = 'cell';

            currentPlayer = 'X';
        } else if (moveHistory.length === 1 && !playerGoesFirst) {
            // AI went first, only one move to undo
            const aiMove = moveHistory.pop();
            board[aiMove.index] = '';
            cells[aiMove.index].textContent = '';
            cells[aiMove.index].className = 'cell';
            currentPlayer = 'O';
            // AI needs to move again
            setTimeout(() => {
                if (gameActive) {
                    const aiMove = getAIMove();
                    if (aiMove !== null) {
                        makeMove(aiMove);
                    }
                }
            }, 500);
        } else if (moveHistory.length === 1 && playerGoesFirst) {
            // Player went first, undo player's move
            const playerMove = moveHistory.pop();
            board[playerMove.index] = '';
            cells[playerMove.index].textContent = '';
            cells[playerMove.index].className = 'cell';
            currentPlayer = 'X';
        }
    } else {
        // In PvP mode, undo last move
        const lastMove = moveHistory.pop();
        board[lastMove.index] = '';
        cells[lastMove.index].textContent = '';
        cells[lastMove.index].className = 'cell';
        currentPlayer = lastMove.player;
    }

    playButtonSound();
    updateUndoButton();
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

    // Trigger haptic feedback on cell tap
    triggerHaptic(10);

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
    // Track move in history
    moveHistory.push({ index: index, player: currentPlayer });

    board[index] = currentPlayer;
    const cell = cells[index];
    cell.textContent = currentPlayer;
    cell.classList.add(currentPlayer.toLowerCase());
    playMoveSound(currentPlayer);
    updateCellAccessibility(index, currentPlayer);

    const winner = checkWinner({ highlight: true });
    if (winner) {
        endGame(winner);
    } else if (board.every(cell => cell !== '')) {
        endGame('draw');
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        updateTurnDisplay();
    }

    updateUndoButton();
}

/**
 * Check for a winner on the board
 * @param {Object} options - Optional configuration
 * @param {boolean} options.highlight - If true, add winner class to winning cells
 * @returns {string|null} - Winner mark ('X' or 'O') or null
 */
function checkWinner(options = {}) {
    const patterns = getWinPatterns();
    for (const pattern of patterns) {
        const firstCell = board[pattern[0]];
        if (firstCell && pattern.every(index => board[index] === firstCell)) {
            if (options.highlight) {
                pattern.forEach(index => {
                    cells[index].classList.add('winner');
                });
                drawWinningLine(pattern);
            }
            return firstCell;
        }
    }
    return null;
}

/**
 * Draw the winning line animation based on winning cell positions
 * @param {number[]} winningPattern - Array of winning cell indices
 */
function drawWinningLine(winningPattern) {
    const svg = document.getElementById('winning-line');
    const line = document.getElementById('win-line');

    // Calculate line coordinates based on first and last cell of winning pattern
    const firstIndex = winningPattern[0];
    const lastIndex = winningPattern[winningPattern.length - 1];

    // Convert indices to row/col
    const firstRow = Math.floor(firstIndex / boardSize);
    const firstCol = firstIndex % boardSize;
    const lastRow = Math.floor(lastIndex / boardSize);
    const lastCol = lastIndex % boardSize;

    // Calculate center positions as percentages
    const cellSize = 100 / boardSize;
    const x1 = (firstCol + 0.5) * cellSize;
    const y1 = (firstRow + 0.5) * cellSize;
    const x2 = (lastCol + 0.5) * cellSize;
    const y2 = (lastRow + 0.5) * cellSize;

    // Set line coordinates
    line.setAttribute('x1', x1);
    line.setAttribute('y1', y1);
    line.setAttribute('x2', x2);
    line.setAttribute('y2', y2);

    // Reset animation by removing and re-adding the element
    line.style.animation = 'none';
    line.offsetHeight; // Trigger reflow
    line.style.animation = '';

    // Show the SVG
    svg.classList.remove('hidden');
}

/**
 * Hide the winning line
 */
function hideWinningLine() {
    const svg = document.getElementById('winning-line');
    if (svg) {
        svg.classList.add('hidden');
    }
}

/**
 * Find a winning move for the specified player
 * @param {string} player - 'X' or 'O'
 * @returns {number|null} - Index of winning move or null
 */
function findWinningMove(player) {
    const available = board.map((cell, i) => cell === '' ? i : null).filter(i => i !== null);
    for (const move of available) {
        board[move] = player;
        const winner = checkWinner();
        board[move] = '';
        if (winner === player) {
            return move;
        }
    }
    return null;
}

function endGame(result) {
    gameActive = false;
    const currentStats = getCurrentStats();

    if (result === 'draw') {
        resultDisplay.textContent = t('draw');
        resultDisplay.className = 'draw';
        turnDisplay.textContent = t('gameOver');
        playDrawSound();
        triggerHaptic(30); // Draw haptic pattern

        if (gameMode === 'pvp') {
            currentStats.pvp.draws++;
        } else {
            currentStats.ai[aiDifficulty].draws++;
        }
    } else {
        if (gameMode === 'pvp') {
            resultDisplay.textContent = result === 'X' ? t('player1Wins') : t('player2Wins');
            resultDisplay.className = 'win';
            playWinSound();
            triggerHaptic([50, 50, 50]); // Win haptic pattern
            if (result === 'X') {
                currentStats.pvp.player1Wins++;
            } else {
                currentStats.pvp.player2Wins++;
            }
        } else {
            if (result === 'X') {
                resultDisplay.textContent = t('youWin');
                resultDisplay.className = 'win';
                playWinSound();
                triggerHaptic([50, 50, 50]); // Win haptic pattern
                currentStats.ai[aiDifficulty].wins++;
            } else {
                resultDisplay.textContent = t('aiWins');
                resultDisplay.className = 'lose';
                playLoseSound();
                triggerHaptic([100, 50, 100]); // Lose haptic pattern
                currentStats.ai[aiDifficulty].losses++;
            }
        }
        turnDisplay.textContent = t('gameOver');
    }

    resultDisplay.classList.remove('hidden');
    updateAllCellsDisabled(true);
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
    // ALWAYS take a winning move if one exists (priority 1)
    const winningMove = findWinningMove('O');
    if (winningMove !== null) return winningMove;

    // ALWAYS block opponent's winning move (priority 2)
    const blockingMove = findWinningMove('X');
    if (blockingMove !== null) return blockingMove;

    // Calculate center position(s) for current board size
    const center = Math.floor(boardSize / 2);
    const centerIndex = center * boardSize + center;

    // For non-critical moves, add some randomness for medium difficulty
    // 60% chance to take center if available
    if (Math.random() < 0.6 && available.includes(centerIndex)) {
        return centerIndex;
    }

    // Calculate corners for current board size
    const corners = [
        0,                              // Top-left
        boardSize - 1,                  // Top-right
        boardSize * (boardSize - 1),    // Bottom-left
        boardSize * boardSize - 1       // Bottom-right
    ].filter(c => available.includes(c));

    // 50% chance to take a corner
    if (Math.random() < 0.5 && corners.length > 0) {
        return corners[Math.floor(Math.random() * corners.length)];
    }

    // Otherwise random move
    return getEasyMove(available);
}

/**
 * Calculate appropriate search depth based on board state
 */
function getSearchDepth() {
    const emptyCells = board.filter(cell => cell === '').length;

    if (boardSize === 3) {
        return 20; // Full search for 3x3 (max 9 moves)
    } else if (boardSize === 4) {
        // 4x4: limit depth based on game progress
        if (emptyCells > 12) return 4;
        if (emptyCells > 8) return 6;
        return 8;
    } else {
        // 5x5: more aggressive limiting
        if (emptyCells > 20) return 3;
        if (emptyCells > 15) return 4;
        if (emptyCells > 10) return 5;
        return 6;
    }
}

/**
 * Heuristic evaluation for non-terminal board states
 * Positive = good for AI, Negative = good for player
 */
function evaluateBoard() {
    let score = 0;
    const patterns = getWinPatterns();

    for (const line of patterns) {
        const cells = line.map(i => board[i]);
        const aiCount = cells.filter(c => c === 'O').length;
        const playerCount = cells.filter(c => c === 'X').length;

        // Only score lines that aren't blocked
        if (aiCount > 0 && playerCount === 0) {
            // AI has potential in this line
            score += Math.pow(10, aiCount - 1);
        } else if (playerCount > 0 && aiCount === 0) {
            // Player has potential in this line
            score -= Math.pow(10, playerCount - 1);
        }
    }

    // Bonus for center control (more important in larger boards)
    const center = Math.floor(boardSize / 2);
    const centerIndex = center * boardSize + center;
    if (board[centerIndex] === 'O') score += 3;
    if (board[centerIndex] === 'X') score -= 3;

    return score;
}

/**
 * Order moves to improve alpha-beta pruning efficiency
 */
function orderMoves(emptyCells) {
    const center = Math.floor(boardSize / 2);
    const centerIndex = center * boardSize + center;

    return [...emptyCells].sort((a, b) => {
        // Prioritize center
        const aIsCenter = a === centerIndex ? 1 : 0;
        const bIsCenter = b === centerIndex ? 1 : 0;
        if (aIsCenter !== bIsCenter) return bIsCenter - aIsCenter;

        // Prioritize cells adjacent to existing pieces
        const aHasNeighbor = hasAdjacentPiece(a) ? 1 : 0;
        const bHasNeighbor = hasAdjacentPiece(b) ? 1 : 0;
        return bHasNeighbor - aHasNeighbor;
    });
}

/**
 * Check if a cell has an adjacent piece
 */
function hasAdjacentPiece(index) {
    const row = Math.floor(index / boardSize);
    const col = index % boardSize;

    for (let dr = -1; dr <= 1; dr++) {
        for (let dc = -1; dc <= 1; dc++) {
            if (dr === 0 && dc === 0) continue;
            const newRow = row + dr;
            const newCol = col + dc;
            if (newRow >= 0 && newRow < boardSize && newCol >= 0 && newCol < boardSize) {
                if (board[newRow * boardSize + newCol] !== '') return true;
            }
        }
    }
    return false;
}

function getHardMove() {
    // First check for immediate winning move
    const winningMove = findWinningMove('O');
    if (winningMove !== null) return winningMove;

    // Then check for blocking move
    const blockingMove = findWinningMove('X');
    if (blockingMove !== null) return blockingMove;

    let bestScore = -Infinity;
    let bestMove = null;

    const available = board.map((cell, i) => cell === '' ? i : null).filter(i => i !== null);
    const orderedMoves = orderMoves(available);
    const maxDepth = getSearchDepth();

    for (const move of orderedMoves) {
        board[move] = 'O';
        const score = minimax(0, maxDepth, false, -Infinity, Infinity);
        board[move] = '';

        if (score > bestScore) {
            bestScore = score;
            bestMove = move;
        }
    }

    return bestMove;
}

/**
 * Minimax algorithm with alpha-beta pruning and depth limiting
 * @param {number} depth - Current depth in the tree
 * @param {number} maxDepth - Maximum search depth
 * @param {boolean} isMaximizing - True if maximizing player (AI)
 * @param {number} alpha - Best value maximizer can guarantee
 * @param {number} beta - Best value minimizer can guarantee
 * @returns {number} - The best score for this position
 */
function minimax(depth, maxDepth, isMaximizing, alpha, beta) {
    const winner = checkWinner();
    if (winner === 'O') return 100 - depth; // Prefer faster wins
    if (winner === 'X') return depth - 100; // Prefer slower losses
    if (board.every(cell => cell !== '')) return 0;

    // Depth limit reached - use heuristic evaluation
    if (depth >= maxDepth) {
        return evaluateBoard();
    }

    const totalCells = boardSize * boardSize;

    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < totalCells; i++) {
            if (board[i] === '') {
                board[i] = 'O';
                const score = minimax(depth + 1, maxDepth, false, alpha, beta);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
                alpha = Math.max(alpha, score);
                // Alpha-beta pruning
                if (beta <= alpha) {
                    break;
                }
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < totalCells; i++) {
            if (board[i] === '') {
                board[i] = 'X';
                const score = minimax(depth + 1, maxDepth, true, alpha, beta);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
                beta = Math.min(beta, score);
                // Alpha-beta pruning
                if (beta <= alpha) {
                    break;
                }
            }
        }
        return bestScore;
    }
}
