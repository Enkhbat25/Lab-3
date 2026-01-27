from ai import get_ai_move


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def get_move(self, board):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, symbol, name="Player"):
        super().__init__(symbol, name)

    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter position (1-9): ")
                move = int(move)
                if board.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. Position already taken or out of range.")
            except ValueError:
                print("Please enter a number between 1 and 9.")


class AIPlayer(Player):
    def __init__(self, symbol, difficulty='medium', name="AI"):
        super().__init__(symbol, name)
        self.difficulty = difficulty

    def get_move(self, board):
        print(f"{self.name} ({self.symbol}) is thinking...")
        move = get_ai_move(board, self.symbol, self.difficulty)
        print(f"{self.name} chooses position {move}")
        return move
