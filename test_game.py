"""Test script to play a game against the hard AI."""
from board import Board
from player import AIPlayer

def test_game_vs_hard_ai():
    print("=" * 40)
    print("  TEST GAME: Human vs Hard AI")
    print("=" * 40)

    board = Board()

    # Simulate human moves (we'll play as X, AI as O)
    human_symbol = 'X'
    ai_symbol = 'O'
    ai = AIPlayer(ai_symbol, 'hard', "Hard AI")

    # Predefined human moves to test the game
    human_moves = [5, 1, 9, 3, 7]  # Human tries center first, then corners
    move_index = 0

    current = 'X'  # X goes first

    print("\nHuman (X) vs Hard AI (O)")
    print("Human will try: center, then corners")
    print()
    board.display_positions()

    while not board.is_game_over():
        board.display()

        if current == human_symbol:
            # Find next valid human move
            while move_index < len(human_moves):
                move = human_moves[move_index]
                move_index += 1
                if board.is_valid_move(move):
                    print(f"Human plays position {move}")
                    board.make_move(move, human_symbol)
                    break
            else:
                # No more predefined moves, pick first available
                move = board.get_available_moves()[0]
                print(f"Human plays position {move}")
                board.make_move(move, human_symbol)
        else:
            move = ai.get_move(board)
            board.make_move(move, ai_symbol)

        current = 'O' if current == 'X' else 'X'

    board.display()

    winner = board.check_winner()
    if winner:
        if winner == human_symbol:
            print("Result: Human wins! (This shouldn't happen vs hard AI)")
        else:
            print("Result: Hard AI wins!")
    else:
        print("Result: Draw!")

    print("\n" + "=" * 40)
    print("Hard AI is unbeatable - best you can do is draw!")
    print("=" * 40)


if __name__ == "__main__":
    test_game_vs_hard_ai()
