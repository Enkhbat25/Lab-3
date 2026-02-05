import random
import threading
import sys
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


class TimedHumanPlayer(Player):
    def __init__(self, symbol, name="Player", timeout=15):
        super().__init__(symbol, name)
        self.timeout = timeout
        self._input_result = None
        self._input_received = threading.Event()

    def _input_thread(self, prompt):
        try:
            self._input_result = input(prompt)
        except EOFError:
            self._input_result = None
        finally:
            self._input_received.set()

    def get_move(self, board):
        while True:
            self._input_result = None
            self._input_received.clear()

            prompt = f"{self.name} ({self.symbol}), enter position (1-9) [{self.timeout}s]: "

            input_thread = threading.Thread(target=self._input_thread, args=(prompt,))
            input_thread.daemon = True
            input_thread.start()

            if self._input_received.wait(timeout=self.timeout):
                try:
                    move = int(self._input_result)
                    if board.is_valid_move(move):
                        return move
                    else:
                        print("Invalid move. Position already taken or out of range.")
                except (ValueError, TypeError):
                    print("Please enter a number between 1 and 9.")
            else:
                available = board.get_available_moves()
                random_move = random.choice(available)
                print(f"\nTime's up! Random move selected: {random_move}")
                return random_move
