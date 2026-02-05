import time
import random
from board import Board
from player import HumanPlayer, AIPlayer, TimedHumanPlayer
from stats import update_pvp_stats, update_ai_stats, display_stats, reset_stats


def display_title():
    print("\n" + "=" * 40)
    print("         TIC-TAC-TOE")
    print("=" * 40)


def display_menu():
    print("\nMain Menu:")
    print("  1. Player vs Player")
    print("  2. Player vs AI")
    print("  3. AI vs AI")
    print("  4. View Statistics")
    print("  5. Reset Statistics")
    print("  6. Quit")
    return input("\nSelect option (1-6): ")


def get_player_names():
    """Prompt for custom player names in PvP mode."""
    print("\nEnter player names (press Enter for defaults):")
    name1 = input("  Player 1 (X) name: ").strip()
    name2 = input("  Player 2 (O) name: ").strip()
    return name1 if name1 else "Player 1", name2 if name2 else "Player 2"


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


def select_series_length():
    """Select the length of a best-of-N series."""
    print("\nSelect Series Length:")
    print("  1. Single Game")
    print("  2. Best of 3")
    print("  3. Best of 5")
    print("  4. Best of 7")
    print("  5. Best of 9")

    while True:
        choice = input("\nSelect option (1-5): ")
        options = {'1': 1, '2': 3, '3': 5, '4': 7, '5': 9}
        if choice in options:
            return options[choice]
        print("Invalid choice. Please enter 1-5.")


def select_timer_settings():
    """Select move timer settings."""
    print("\nMove Timer Settings:")
    print("  1. Timer OFF")
    print("  2. Timer ON - 5 seconds")
    print("  3. Timer ON - 10 seconds")
    print("  4. Timer ON - 15 seconds")
    print("  5. Timer ON - 30 seconds")

    while True:
        choice = input("\nSelect option (1-5): ")
        if choice == '1':
            return False, 0
        elif choice == '2':
            return True, 5
        elif choice == '3':
            return True, 10
        elif choice == '4':
            return True, 15
        elif choice == '5':
            return True, 30
        else:
            print("Invalid choice. Please enter 1-5.")


def select_handicap():
    """Select handicap for vs AI mode."""
    print("\nSelect Handicap:")
    print("  1. None - Normal play")
    print("  2. AI skips first turn - Human always goes first")
    print("  3. AI random first move - AI's first move is random")
    print("  4. Pre-placed piece - Human starts with center (5) marked")

    while True:
        choice = input("\nSelect option (1-4): ")
        if choice == '1':
            return 'none'
        elif choice == '2':
            return 'ai_skips_first'
        elif choice == '3':
            return 'ai_random_first'
        elif choice == '4':
            return 'pre_placed'
        else:
            print("Invalid choice. Please enter 1-4.")


def select_ai_delay():
    """Select delay between AI moves for AI vs AI mode."""
    print("\nSelect Move Delay:")
    print("  1. 500ms (Fast)")
    print("  2. 1000ms (Normal)")
    print("  3. 1500ms (Slow)")
    print("  4. 2000ms (Very Slow)")

    while True:
        choice = input("\nSelect option (1-4): ")
        delays = {'1': 0.5, '2': 1.0, '3': 1.5, '4': 2.0}
        if choice in delays:
            return delays[choice]
        print("Invalid choice. Please enter 1-4.")


def play_game(player1, player2, game_mode, difficulty=None, handicap='none'):
    """Play a single game and return the winner (player object or None for draw)."""
    board = Board()
    current_player = player1
    players = {player1.symbol: player1, player2.symbol: player2}

    # Apply handicaps
    ai_first_move_random = False
    if handicap == 'pre_placed':
        # Pre-place center for human
        human_symbol = 'X' if isinstance(player1, (HumanPlayer, TimedHumanPlayer)) else 'O'
        board.make_move(5, human_symbol)
        print("\nHandicap applied: Center position (5) pre-marked for human!")
    elif handicap == 'ai_random_first':
        ai_first_move_random = True
        print("\nHandicap applied: AI's first move will be random!")
    elif handicap == 'ai_skips_first':
        # Ensure human goes first
        if isinstance(player1, AIPlayer):
            current_player = player2
            print("\nHandicap applied: AI skips first turn, human goes first!")

    print("\nGame Start!")
    board.display_positions()

    first_ai_move_done = False

    while not board.is_game_over():
        board.display()

        # Handle AI random first move handicap
        if ai_first_move_random and isinstance(current_player, AIPlayer) and not first_ai_move_done:
            print(f"{current_player.name} ({current_player.symbol}) is thinking...")
            available = board.get_available_moves()
            move = random.choice(available)
            print(f"{current_player.name} chooses position {move} (random handicap)")
            first_ai_move_done = True
        else:
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
        elif game_mode == 'vs_ai':
            if isinstance(winning_player, (HumanPlayer, TimedHumanPlayer)):
                update_ai_stats(difficulty, 'win')
            else:
                update_ai_stats(difficulty, 'loss')
        # No stats update for AI vs AI mode

        return winning_player
    else:
        print("\nIt's a draw!")
        if game_mode == 'pvp':
            update_pvp_stats(None)
        elif game_mode == 'vs_ai':
            update_ai_stats(difficulty, 'draw')
        return None


def play_series(player1, player2, game_mode, series_length, difficulty=None, handicap='none', timer_enabled=False, timer_duration=15):
    """Play a best-of-N series."""
    wins_needed = (series_length // 2) + 1
    scores = {player1.name: 0, player2.name: 0}
    draws = 0
    round_num = 1

    print(f"\n{'='*40}")
    print(f"   BEST OF {series_length} SERIES")
    print(f"   First to {wins_needed} wins!")
    print(f"{'='*40}")

    while scores[player1.name] < wins_needed and scores[player2.name] < wins_needed:
        print(f"\n--- Round {round_num} ---")
        print(f"Score: {player1.name}: {scores[player1.name]} | {player2.name}: {scores[player2.name]} | Draws: {draws}")

        # Recreate players with timer if needed for human players
        p1 = player1
        p2 = player2
        if timer_enabled:
            if isinstance(player1, HumanPlayer):
                p1 = TimedHumanPlayer(player1.symbol, player1.name, timer_duration)
            if isinstance(player2, HumanPlayer):
                p2 = TimedHumanPlayer(player2.symbol, player2.name, timer_duration)

        winner = play_game(p1, p2, game_mode, difficulty, handicap if round_num == 1 else 'none')

        if winner:
            # Match winner to original player names
            if winner.name == player1.name or winner.name == p1.name:
                scores[player1.name] += 1
            else:
                scores[player2.name] += 1
        else:
            draws += 1

        round_num += 1

        # Check if series is over
        if scores[player1.name] >= wins_needed or scores[player2.name] >= wins_needed:
            break

        # Ask to continue or end series early
        print(f"\nCurrent Score: {player1.name}: {scores[player1.name]} | {player2.name}: {scores[player2.name]}")
        choice = input("Press Enter for next round or 'Q' to end series: ").strip().upper()
        if choice == 'Q':
            break

    # Display final results
    print(f"\n{'='*40}")
    print("   SERIES COMPLETE!")
    print(f"{'='*40}")
    print(f"Final Score: {player1.name}: {scores[player1.name]} | {player2.name}: {scores[player2.name]} | Draws: {draws}")

    if scores[player1.name] > scores[player2.name]:
        print(f"\n{player1.name} wins the series!")
    elif scores[player2.name] > scores[player1.name]:
        print(f"\n{player2.name} wins the series!")
    else:
        print("\nThe series ends in a tie!")


def play_pvp():
    print("\n--- Player vs Player ---")

    # Feature 1: Custom player names
    name1, name2 = get_player_names()

    # Feature 2: Series mode
    series_length = select_series_length()

    # Feature 5: Timer settings
    timer_enabled, timer_duration = select_timer_settings()

    if timer_enabled:
        player1 = TimedHumanPlayer('X', name1, timer_duration)
        player2 = TimedHumanPlayer('O', name2, timer_duration)
    else:
        player1 = HumanPlayer('X', name1)
        player2 = HumanPlayer('O', name2)

    if series_length == 1:
        play_game(player1, player2, 'pvp')
    else:
        # Use base HumanPlayer for series (timer applied per-game)
        base_p1 = HumanPlayer('X', name1)
        base_p2 = HumanPlayer('O', name2)
        play_series(base_p1, base_p2, 'pvp', series_length, timer_enabled=timer_enabled, timer_duration=timer_duration)


def play_vs_ai():
    print("\n--- Player vs AI ---")
    difficulty = select_difficulty()

    # Feature 2: Series mode
    series_length = select_series_length()

    # Feature 5: Timer settings
    timer_enabled, timer_duration = select_timer_settings()

    # Feature 4: Handicap selection
    handicap = select_handicap()

    print("\nDo you want to go first?")
    choice = input("Enter Y for yes, N for no: ").strip().upper()

    if choice == 'Y':
        if timer_enabled:
            player1 = TimedHumanPlayer('X', "You", timer_duration)
        else:
            player1 = HumanPlayer('X', "You")
        player2 = AIPlayer('O', difficulty, f"AI ({difficulty})")
    else:
        player1 = AIPlayer('X', difficulty, f"AI ({difficulty})")
        if timer_enabled:
            player2 = TimedHumanPlayer('O', "You", timer_duration)
        else:
            player2 = HumanPlayer('O', "You")

    if series_length == 1:
        play_game(player1, player2, 'vs_ai', difficulty, handicap)
    else:
        # For series, use base players
        if choice == 'Y':
            base_p1 = HumanPlayer('X', "You")
            base_p2 = AIPlayer('O', difficulty, f"AI ({difficulty})")
        else:
            base_p1 = AIPlayer('X', difficulty, f"AI ({difficulty})")
            base_p2 = HumanPlayer('O', "You")
        play_series(base_p1, base_p2, 'vs_ai', series_length, difficulty, handicap, timer_enabled, timer_duration)


def play_ai_vs_ai():
    """Feature 3: AI vs AI mode."""
    print("\n--- AI vs AI ---")

    print("\nSelect AI 1 (X) difficulty:")
    difficulty1 = select_difficulty()

    print("\nSelect AI 2 (O) difficulty:")
    difficulty2 = select_difficulty()

    delay = select_ai_delay()

    player1 = AIPlayer('X', difficulty1, f"AI-1 ({difficulty1})")
    player2 = AIPlayer('O', difficulty2, f"AI-2 ({difficulty2})")

    board = Board()
    current_player = player1
    players = {player1.symbol: player1, player2.symbol: player2}
    paused = False

    print("\nGame Start!")
    print("Press Enter to pause/resume during game.")
    board.display_positions()

    while not board.is_game_over():
        board.display()

        print(f"\n{current_player.name} is thinking...")
        time.sleep(delay)

        move = current_player.get_move(board)
        board.make_move(move, current_player.symbol)

        # Switch players
        current_player = player2 if current_player == player1 else player1

    board.display()

    winner = board.check_winner()
    if winner:
        winning_player = players[winner]
        print(f"\n{winning_player.name} ({winner}) wins!")
    else:
        print("\nIt's a draw!")

    print(f"\nMatch: {player1.name} vs {player2.name}")


def main():
    display_title()

    while True:
        choice = display_menu()

        if choice == '1':
            play_pvp()
        elif choice == '2':
            play_vs_ai()
        elif choice == '3':
            play_ai_vs_ai()
        elif choice == '4':
            display_stats()
        elif choice == '5':
            confirm = input("Are you sure you want to reset statistics? (Y/N): ")
            if confirm.strip().upper() == 'Y':
                reset_stats()
        elif choice == '6':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1-6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
