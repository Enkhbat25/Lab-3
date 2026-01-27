class Board:
    def __init__(self):
        self.grid = [' ' for _ in range(9)]

    def display(self):
        print()
        for i in range(3):
            row = self.grid[i*3:(i+1)*3]
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("-----------")
        print()

    def display_positions(self):
        print("\nPositions:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print()

    def is_valid_move(self, position):
        if position < 1 or position > 9:
            return False
        return self.grid[position - 1] == ' '

    def make_move(self, position, symbol):
        if self.is_valid_move(position):
            self.grid[position - 1] = symbol
            return True
        return False

    def get_available_moves(self):
        return [i + 1 for i, cell in enumerate(self.grid) if cell == ' ']

    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for pattern in win_patterns:
            a, b, c = pattern
            if self.grid[a] != ' ' and self.grid[a] == self.grid[b] == self.grid[c]:
                return self.grid[a]
        return None

    def is_draw(self):
        return ' ' not in self.grid and self.check_winner() is None

    def is_game_over(self):
        return self.check_winner() is not None or self.is_draw()

    def reset(self):
        self.grid = [' ' for _ in range(9)]

    def copy(self):
        new_board = Board()
        new_board.grid = self.grid.copy()
        return new_board
