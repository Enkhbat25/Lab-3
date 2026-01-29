# Tic-Tac-Toe Game

A modern, feature-rich Tic-Tac-Toe game with both web-based and Python command-line interfaces.

## Live Demo

Open `index.html` in your browser to play the web version.

## Features

### Game Modes
- **Player vs Player (PvP)**: Play against a friend on the same device
- **Player vs AI**: Challenge the computer with three difficulty levels:
  - **Easy**: AI makes random moves
  - **Medium**: AI has 70% chance to take winning moves and 50% chance to block
  - **Hard (Unbeatable)**: Uses the Minimax algorithm - impossible to beat!

### Multi-Language Support
The game supports 6 languages:
- English
- Mongolian (Монгол)
- Russian (Русский)
- Korean (한국어)
- Japanese (日本語)
- Chinese (中文)

### Theme Options
- **Dark Mode**: Sleek dark interface with neon accents (default)
- **Light Mode**: Clean, bright interface for daytime use

### Statistics Tracking
- Track your wins, losses, and draws
- Separate statistics for each game mode and AI difficulty
- Statistics are saved locally and persist between sessions

### Responsive Design
- Works on desktop, tablet, and mobile devices
- Optimized touch controls for mobile play

## How to Play

### Basic Rules
1. The game is played on a 3x3 grid
2. Players take turns placing their mark (X or O) in empty squares
3. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
4. If all 9 squares are filled without a winner, the game is a draw

### Web Version
1. Open `index.html` in any modern web browser
2. Select your preferred language from the dropdown (top-right)
3. Toggle between light/dark mode using the theme button (top-right)
4. Choose a game mode from the main menu:
   - **Player vs Player**: Take turns with a friend
   - **Player vs AI**: Select difficulty and play against the computer
5. Click on any empty cell to place your mark
6. After the game ends, click "Play Again" or return to the main menu

### Python Version
```bash
python main.py
```

## Project Structure

```
tic_tac_toe/
├── index.html      # Web game HTML structure
├── style.css       # Styling and themes
├── script.js       # Game logic and AI for web version
├── main.py         # Python game entry point
├── board.py        # Board logic for Python version
├── player.py       # Player classes for Python version
├── ai.py           # AI logic for Python version
├── stats.py        # Statistics management for Python version
├── test_game.py    # Unit tests
├── test_optimal.py # AI optimality tests
└── data/
    └── stats.json  # Saved statistics (Python version)
```

## Technical Details

### AI Algorithm
The Hard difficulty uses the **Minimax algorithm**, a recursive algorithm used in decision-making and game theory. It provides optimal play by:
- Evaluating all possible future game states
- Assuming the opponent also plays optimally
- Choosing moves that maximize the AI's chance of winning while minimizing the player's

### Local Storage
The web version uses browser localStorage to save:
- Language preference (`tictactoe-lang`)
- Theme preference (`tictactoe-theme`)
- Game statistics (`tictactoe-stats`)

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## Installation

No installation required for the web version! Simply:
1. Clone or download this repository
2. Open `index.html` in your browser

For the Python version:
```bash
# Clone the repository
git clone https://github.com/Enkhbat25/Lab-3.git

# Navigate to the directory
cd Lab-3

# Run the game
python main.py
```

## Requirements

### Web Version
- Any modern web browser with JavaScript enabled

### Python Version
- Python 3.6 or higher
- No external dependencies required

## Controls

| Action | Web | Python |
|--------|-----|--------|
| Select cell | Click/Tap | Enter number (1-9) |
| Change language | Dropdown menu | N/A |
| Toggle theme | Theme button | N/A |
| View stats | Menu button | Menu option |
| Reset stats | Menu button | Menu option |

## Contributing

Feel free to fork this repository and submit pull requests for:
- Bug fixes
- New features
- Additional language translations
- UI/UX improvements

## License

This project is open source and available for educational purposes.

## Author

Enkhbat - [GitHub Profile](https://github.com/Enkhbat25)

---

Enjoy the game!
