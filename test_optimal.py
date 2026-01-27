"""Test optimal play - should always result in a draw."""
from board import Board
from player import AIPlayer

def test_optimal_play():
    print("=" * 40)
    print("  TEST: Optimal Human vs Hard AI")
    print("=" * 40)

    board = Board()
    ai = AIPlayer('O', 'hard', "Hard AI")

    # Optimal strategy: take center, then respond to AI
    print("\nHuman (X) plays optimally against Hard AI (O)")
    print()

    current = 'X'

    while not board.is_game_over():
        board.display()

        if current == 'X':
            # Simple optimal strategy for human
            available = board.get_available_moves()

            # Priority: center > corners > edges
            if 5 in available:
                move = 5
            elif any(c in available for c in [1, 3, 7, 9]):
                # Pick corner opposite to AI if possible, else any corner
                corners = [c for c in [1, 3, 7, 9] if c in available]
                # Try to block AI wins
                for m in available:
                    test = board.copy()
                    test.make_move(m, 'O')
                    if test.check_winner() == 'O':
                        move = m
                        break
                else:
                    move = corners[0]
            else:
                move = available[0]

            # Actually use minimax for human too to ensure optimal
            from ai import get_hard_move
            # Swap perspective - get best move for X
            move = get_optimal_human_move(board)

            print(f"Human plays position {move}")
            board.make_move(move, 'X')
        else:
            move = ai.get_move(board)
            board.make_move(move, 'O')

        current = 'O' if current == 'X' else 'X'

    board.display()

    winner = board.check_winner()
    if winner == 'X':
        print("Result: Human wins!")
    elif winner == 'O':
        print("Result: AI wins!")
    else:
        print("Result: DRAW (as expected with optimal play)")


def get_optimal_human_move(board):
    """Minimax for human player (X)."""
    def minimax(b, is_maximizing):
        winner = b.check_winner()
        if winner == 'X':
            return 10
        if winner == 'O':
            return -10
        if b.is_draw():
            return 0

        if is_maximizing:
            best = float('-inf')
            for move in b.get_available_moves():
                test = b.copy()
                test.make_move(move, 'X')
                best = max(best, minimax(test, False))
            return best
        else:
            best = float('inf')
            for move in b.get_available_moves():
                test = b.copy()
                test.make_move(move, 'O')
                best = min(best, minimax(test, True))
            return best

    best_move = None
    best_score = float('-inf')
    for move in board.get_available_moves():
        test = board.copy()
        test.make_move(move, 'X')
        score = minimax(test, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


if __name__ == "__main__":
    test_optimal_play()
