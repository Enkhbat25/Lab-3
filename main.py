from board import Board
from player import HumanPlayer, AIPlayer
from stats import update_pvp_stats, update_ai_stats, display_stats, reset_stats


def display_title():
    print("\n" + "=" * 40)
    print("         TIC-TAC-TOE")
    print("=" * 40)


def display_menu():
    print("\nMain Menu:")
    print("  1. Player vs Player")
    print("  2. Player vs AI")
    print("  3. View Statistics")
    print("  4. Reset Statistics")
    print("  5. Quit")
    return input("\nSelect option (1-5): ")


def select_difficulty():
    print("\nSelect AI Difficulty:")
    print("  1. Easy (Random moves)")
    print("  2. Medium (Blocks and takes wins)")
    print("  3. Hard (Unbeatable)")

    while True:
        choice = input("\nSelect difficulty (1-3): ")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def play_game(player1, player2, game_mode, difficulty=None):
    board = Board()
    current_player = player1
    players = {player1.symbol: player1, player2.symbol: player2}

    print("\nGame Start!")
    board.display_positions()

    while not board.is_game_over():
        board.display()
        move = current_player.get_move(board)
        board.make_move(move, current_player.symbol)

        # Switch players
        current_player = player2 if current_player == player1 else player1

    board.display()

    winner = board.check_winner()
    if winner:
        winning_player = players[winner]
        print(f"\n{winning_player.name} ({winner}) wins!")

        if game_mode == 'pvp':
            update_pvp_stats(1 if winner == 'X' else 2)
        else:
            if winning_player == player1:
                update_ai_stats(difficulty, 'win')
            else:
                update_ai_stats(difficulty, 'loss')
    else:
        print("\nIt's a draw!")
        if game_mode == 'pvp':
            update_pvp_stats(None)
        else:
            update_ai_stats(difficulty, 'draw')


def play_pvp():
    print("\n--- Player vs Player ---")
    player1 = HumanPlayer('X', "Player 1")
    player2 = HumanPlayer('O', "Player 2")
    play_game(player1, player2, 'pvp')


def play_vs_ai():
    print("\n--- Player vs AI ---")
    difficulty = select_difficulty()

    print("\nDo you want to go first?")
    choice = input("Enter Y for yes, N for no: ").strip().upper()

    if choice == 'Y':
        player1 = HumanPlayer('X', "You")
        player2 = AIPlayer('O', difficulty, f"AI ({difficulty})")
    else:
        player1 = AIPlayer('X', difficulty, f"AI ({difficulty})")
        player2 = HumanPlayer('O', "You")

    play_game(player1, player2, 'vs_ai', difficulty)


def main():
    display_title()

    while True:
        choice = display_menu()

        if choice == '1':
            play_pvp()
        elif choice == '2':
            play_vs_ai()
        elif choice == '3':
            display_stats()
        elif choice == '4':
            confirm = input("Are you sure you want to reset statistics? (Y/N): ")
            if confirm.strip().upper() == 'Y':
                reset_stats()
        elif choice == '5':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1-5.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
