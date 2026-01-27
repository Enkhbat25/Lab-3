import random


def get_easy_move(board):
    """Easy AI: picks a random available move."""
    available = board.get_available_moves()
    return random.choice(available) if available else None


def get_medium_move(board, ai_symbol):
    """Medium AI: blocks opponent wins and takes winning moves."""
    opponent = 'O' if ai_symbol == 'X' else 'X'
    available = board.get_available_moves()

    # Check if AI can win
    for move in available:
        test_board = board.copy()
        test_board.make_move(move, ai_symbol)
        if test_board.check_winner() == ai_symbol:
            return move

    # Block opponent's winning move
    for move in available:
        test_board = board.copy()
        test_board.make_move(move, opponent)
        if test_board.check_winner() == opponent:
            return move

    # Take center if available
    if 5 in available:
        return 5

    # Take a corner if available
    corners = [1, 3, 7, 9]
    available_corners = [c for c in corners if c in available]
    if available_corners:
        return random.choice(available_corners)

    # Take any available move
    return random.choice(available) if available else None


def get_hard_move(board, ai_symbol):
    """Hard AI: unbeatable using minimax algorithm."""
    opponent = 'O' if ai_symbol == 'X' else 'X'

    def minimax(board, depth, is_maximizing):
        winner = board.check_winner()
        if winner == ai_symbol:
            return 10 - depth
        if winner == opponent:
            return depth - 10
        if board.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in board.get_available_moves():
                test_board = board.copy()
                test_board.make_move(move, ai_symbol)
                score = minimax(test_board, depth + 1, False)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in board.get_available_moves():
                test_board = board.copy()
                test_board.make_move(move, opponent)
                score = minimax(test_board, depth + 1, True)
                best_score = min(score, best_score)
            return best_score

    best_move = None
    best_score = float('-inf')

    for move in board.get_available_moves():
        test_board = board.copy()
        test_board.make_move(move, ai_symbol)
        score = minimax(test_board, 0, False)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def get_ai_move(board, ai_symbol, difficulty):
    """Get AI move based on difficulty level."""
    if difficulty == 'easy':
        return get_easy_move(board)
    elif difficulty == 'medium':
        return get_medium_move(board, ai_symbol)
    else:  # hard
        return get_hard_move(board, ai_symbol)
