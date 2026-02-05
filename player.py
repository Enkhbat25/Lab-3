import random
import threading
import sys
from ai import get_ai_move

# Try to import colors from board module
try:
    from board import (
        COLORS_ENABLED, PROMPT_COLOR, ERROR_COLOR, SUCCESS_COLOR,
        Style, Fore
    )
except ImportError:
    COLORS_ENABLED = False
    PROMPT_COLOR = ERROR_COLOR = SUCCESS_COLOR = ''
    class Style:
        RESET_ALL = ''
    class Fore:
        pass


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def get_move(self, board):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, symbol, name="Player"):
        super().__init__(symbol, name)

    def get_move(self, board, allow_undo=False):
        """Get move from human player. Returns move position or 'undo' string."""
        while True:
            try:
                # Build prompt with optional undo
                if allow_undo and board.can_undo():
                    if COLORS_ENABLED:
                        prompt = f"{PROMPT_COLOR}{self.name} ({self.symbol}), enter position (1-9) or 'u' to undo: {Style.RESET_ALL}"
                    else:
                        prompt = f"{self.name} ({self.symbol}), enter position (1-9) or 'u' to undo: "
                else:
                    if COLORS_ENABLED:
                        prompt = f"{PROMPT_COLOR}{self.name} ({self.symbol}), enter position (1-9): {Style.RESET_ALL}"
                    else:
                        prompt = f"{self.name} ({self.symbol}), enter position (1-9): "

                move = input(prompt).strip().lower()

                # Check for undo
                if move == 'u' and allow_undo and board.can_undo():
                    return 'undo'

                move = int(move)
                if board.is_valid_move(move):
                    return move
                else:
                    if COLORS_ENABLED:
                        print(f"{ERROR_COLOR}Invalid move. Position already taken or out of range.{Style.RESET_ALL}")
                    else:
                        print("Invalid move. Position already taken or out of range.")
            except ValueError:
                if COLORS_ENABLED:
                    print(f"{ERROR_COLOR}Please enter a number between 1 and 9.{Style.RESET_ALL}")
                else:
                    print("Please enter a number between 1 and 9.")


class AIPlayer(Player):
    def __init__(self, symbol, difficulty='medium', name="AI"):
        super().__init__(symbol, name)
        self.difficulty = difficulty

    def get_move(self, board, allow_undo=False):
        """AI doesn't support undo, just returns move."""
        if COLORS_ENABLED:
            print(f"{PROMPT_COLOR}{self.name} ({self.symbol}) is thinking...{Style.RESET_ALL}")
        else:
            print(f"{self.name} ({self.symbol}) is thinking...")

        move = get_ai_move(board, self.symbol, self.difficulty)

        if COLORS_ENABLED:
            print(f"{SUCCESS_COLOR}{self.name} chooses position {move}{Style.RESET_ALL}")
        else:
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

    def get_move(self, board, allow_undo=False):
        """Get timed move from human player. Returns move position or 'undo' string."""
        while True:
            self._input_result = None
            self._input_received.clear()

            # Build prompt with timer and optional undo
            if allow_undo and board.can_undo():
                if COLORS_ENABLED:
                    prompt = f"{PROMPT_COLOR}{self.name} ({self.symbol}), enter position (1-9) or 'u' to undo [{self.timeout}s]: {Style.RESET_ALL}"
                else:
                    prompt = f"{self.name} ({self.symbol}), enter position (1-9) or 'u' to undo [{self.timeout}s]: "
            else:
                if COLORS_ENABLED:
                    prompt = f"{PROMPT_COLOR}{self.name} ({self.symbol}), enter position (1-9) [{self.timeout}s]: {Style.RESET_ALL}"
                else:
                    prompt = f"{self.name} ({self.symbol}), enter position (1-9) [{self.timeout}s]: "

            input_thread = threading.Thread(target=self._input_thread, args=(prompt,))
            input_thread.daemon = True
            input_thread.start()

            if self._input_received.wait(timeout=self.timeout):
                try:
                    move_input = self._input_result.strip().lower() if self._input_result else ''

                    # Check for undo
                    if move_input == 'u' and allow_undo and board.can_undo():
                        return 'undo'

                    move = int(move_input)
                    if board.is_valid_move(move):
                        return move
                    else:
                        if COLORS_ENABLED:
                            print(f"{ERROR_COLOR}Invalid move. Position already taken or out of range.{Style.RESET_ALL}")
                        else:
                            print("Invalid move. Position already taken or out of range.")
                except (ValueError, TypeError):
                    if COLORS_ENABLED:
                        print(f"{ERROR_COLOR}Please enter a number between 1 and 9.{Style.RESET_ALL}")
                    else:
                        print("Please enter a number between 1 and 9.")
            else:
                available = board.get_available_moves()
                random_move = random.choice(available)
                if COLORS_ENABLED:
                    print(f"\n{ERROR_COLOR}Time's up! Random move selected: {random_move}{Style.RESET_ALL}")
                else:
                    print(f"\nTime's up! Random move selected: {random_move}")
                return random_move
