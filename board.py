import os
import platform

# Try to import colorama for cross-platform color support
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORS_ENABLED = True
except ImportError:
    COLORS_ENABLED = False
    # Define dummy color constants
    class Fore:
        CYAN = MAGENTA = WHITE = RED = GREEN = YELLOW = BLUE = ''
    class Back:
        GREEN = YELLOW = ''
    class Style:
        RESET_ALL = DIM = BRIGHT = ''

# Color scheme
X_COLOR = Fore.CYAN
O_COLOR = Fore.MAGENTA
GRID_COLOR = Style.DIM + Fore.WHITE
WIN_HIGHLIGHT = Back.GREEN + Fore.WHITE + Style.BRIGHT
LAST_MOVE_HIGHLIGHT = Back.YELLOW + Fore.WHITE + Style.BRIGHT
ERROR_COLOR = Fore.RED
SUCCESS_COLOR = Fore.GREEN
PROMPT_COLOR = Fore.YELLOW
TITLE_COLOR = Fore.CYAN + Style.BRIGHT

# Settings
CLEAR_SCREEN_ENABLED = True
UNICODE_SUPPORTED = True

# Box drawing characters
if UNICODE_SUPPORTED:
    H_LINE = '───'
    V_LINE = '│'
    CROSS = '┼'
else:
    H_LINE = '---'
    V_LINE = '|'
    CROSS = '+'


def clear_screen():
    """Clear terminal screen (cross-platform)."""
    if not CLEAR_SCREEN_ENABLED:
        return
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def get_colored_symbol(symbol, is_last_move=False, is_winning=False):
    """Get a symbol with appropriate coloring."""
    if not COLORS_ENABLED:
        if is_winning:
            return f'[{symbol}]'
        elif is_last_move:
            return f'({symbol})'
        return symbol

    if is_winning:
        return f'{WIN_HIGHLIGHT}{symbol}{Style.RESET_ALL}'
    elif is_last_move:
        return f'{LAST_MOVE_HIGHLIGHT}{symbol}{Style.RESET_ALL}'
    elif symbol == 'X':
        return f'{X_COLOR}{symbol}{Style.RESET_ALL}'
    elif symbol == 'O':
        return f'{O_COLOR}{symbol}{Style.RESET_ALL}'
    else:
        return f'{Style.DIM}{symbol}{Style.RESET_ALL}'


class Board:
    # Win patterns as class attribute
    WIN_PATTERNS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    def __init__(self):
        self.grid = [' ' for _ in range(9)]
        self.last_move = None
        self.move_history = []

    def display(self, winning_line=None, show_last_move=True):
        """Display board with optional highlights."""
        print()

        winning_positions = winning_line if winning_line else []

        for i in range(3):
            row_cells = []
            for j in range(3):
                idx = i * 3 + j
                cell = self.grid[idx]

                # Determine display for this cell
                if cell == ' ':
                    # Show position number for empty cells
                    display_cell = get_colored_symbol(str(idx + 1))
                else:
                    is_last = show_last_move and self.last_move == idx
                    is_winning = idx in winning_positions
                    display_cell = get_colored_symbol(cell, is_last, is_winning)

                row_cells.append(display_cell)

            # Build row with grid lines
            if COLORS_ENABLED:
                row_str = f" {row_cells[0]} {GRID_COLOR}{V_LINE}{Style.RESET_ALL} {row_cells[1]} {GRID_COLOR}{V_LINE}{Style.RESET_ALL} {row_cells[2]} "
            else:
                row_str = f" {row_cells[0]} {V_LINE} {row_cells[1]} {V_LINE} {row_cells[2]} "

            print(row_str)

            if i < 2:
                if COLORS_ENABLED:
                    print(f"{GRID_COLOR}{H_LINE}{CROSS}{H_LINE}{CROSS}{H_LINE}{Style.RESET_ALL}")
                else:
                    print(f"{H_LINE}{CROSS}{H_LINE}{CROSS}{H_LINE}")

        print()

    def display_positions(self):
        """Display position reference guide."""
        print(f"\n{PROMPT_COLOR}Positions:{Style.RESET_ALL}" if COLORS_ENABLED else "\nPositions:")
        print(" 1 │ 2 │ 3 " if UNICODE_SUPPORTED else " 1 | 2 | 3 ")
        print("───┼───┼───" if UNICODE_SUPPORTED else "---+---+---")
        print(" 4 │ 5 │ 6 " if UNICODE_SUPPORTED else " 4 | 5 | 6 ")
        print("───┼───┼───" if UNICODE_SUPPORTED else "---+---+---")
        print(" 7 │ 8 │ 9 " if UNICODE_SUPPORTED else " 7 | 8 | 9 ")
        print()

    def is_valid_move(self, position):
        if position < 1 or position > 9:
            return False
        return self.grid[position - 1] == ' '

    def make_move(self, position, symbol, record=True):
        """Make a move on the board."""
        if self.is_valid_move(position):
            if record:
                # Record move in history for undo
                self.move_history.append({
                    'position': position,
                    'symbol': symbol,
                    'board_snapshot': self.grid.copy()
                })
            self.grid[position - 1] = symbol
            self.last_move = position - 1
            return True
        return False

    def undo_move(self):
        """Undo the last move. Returns the undone move info or None."""
        if not self.move_history:
            return None

        last_move = self.move_history.pop()
        self.grid = last_move['board_snapshot']

        # Update last_move to previous move if exists
        if self.move_history:
            self.last_move = self.move_history[-1]['position'] - 1
        else:
            self.last_move = None

        return last_move

    def can_undo(self):
        """Check if undo is available."""
        return len(self.move_history) > 0

    def get_undo_count(self):
        """Get number of moves that can be undone."""
        return len(self.move_history)

    def get_available_moves(self):
        return [i + 1 for i, cell in enumerate(self.grid) if cell == ' ']

    def check_winner(self):
        for pattern in self.WIN_PATTERNS:
            a, b, c = pattern
            if self.grid[a] != ' ' and self.grid[a] == self.grid[b] == self.grid[c]:
                return self.grid[a]
        return None

    def get_winning_line(self):
        """Get the winning line positions (0-indexed) or None."""
        for pattern in self.WIN_PATTERNS:
            a, b, c = pattern
            if self.grid[a] != ' ' and self.grid[a] == self.grid[b] == self.grid[c]:
                return pattern
        return None

    def is_draw(self):
        return ' ' not in self.grid and self.check_winner() is None

    def is_game_over(self):
        return self.check_winner() is not None or self.is_draw()

    def reset(self):
        self.grid = [' ' for _ in range(9)]
        self.last_move = None
        self.move_history = []

    def copy(self):
        new_board = Board()
        new_board.grid = self.grid.copy()
        new_board.last_move = self.last_move
        new_board.move_history = [m.copy() for m in self.move_history]
        return new_board
