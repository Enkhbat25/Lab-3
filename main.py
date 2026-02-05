import time
import random
from board import (
    Board, clear_screen, COLORS_ENABLED,
    TITLE_COLOR, PROMPT_COLOR, SUCCESS_COLOR, ERROR_COLOR,
    Style, X_COLOR, O_COLOR
)
from player import HumanPlayer, AIPlayer, TimedHumanPlayer
from stats import (
    update_pvp_stats, update_ai_stats, display_stats, reset_stats,
    start_game_log, log_move, display_history, export_stats_interactive
)


def display_title():
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}{'=' * 40}")
        print("         TIC-TAC-TOE")
        print(f"{'=' * 40}{Style.RESET_ALL}")
    else:
        print("\n" + "=" * 40)
        print("         TIC-TAC-TOE")
        print("=" * 40)


def display_menu():
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Main Menu:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} Player vs Player")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} Player vs AI")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} AI vs AI")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} View Statistics")
        print(f"  {X_COLOR}5.{Style.RESET_ALL} View Game History")
        print(f"  {X_COLOR}6.{Style.RESET_ALL} Export Stats to CSV")
        print(f"  {X_COLOR}7.{Style.RESET_ALL} Reset Statistics")
        print(f"  {X_COLOR}8.{Style.RESET_ALL} Quit")
        return input(f"\n{PROMPT_COLOR}Select option (1-8): {Style.RESET_ALL}")
    else:
        print("\nMain Menu:")
        print("  1. Player vs Player")
        print("  2. Player vs AI")
        print("  3. AI vs AI")
        print("  4. View Statistics")
        print("  5. View Game History")
        print("  6. Export Stats to CSV")
        print("  7. Reset Statistics")
        print("  8. Quit")
        return input("\nSelect option (1-8): ")


def get_player_names():
    """Prompt for custom player names in PvP mode."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Enter player names (press Enter for defaults):{Style.RESET_ALL}")
        name1 = input(f"  {X_COLOR}Player 1 (X){Style.RESET_ALL} name: ").strip()
        name2 = input(f"  {O_COLOR}Player 2 (O){Style.RESET_ALL} name: ").strip()
    else:
        print("\nEnter player names (press Enter for defaults):")
        name1 = input("  Player 1 (X) name: ").strip()
        name2 = input("  Player 2 (O) name: ").strip()
    return name1 if name1 else "Player 1", name2 if name2 else "Player 2"


def select_difficulty():
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Select AI Difficulty:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} Easy (Random moves)")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} Medium (Blocks and takes wins)")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} Hard (Unbeatable)")
    else:
        print("\nSelect AI Difficulty:")
        print("  1. Easy (Random moves)")
        print("  2. Medium (Blocks and takes wins)")
        print("  3. Hard (Unbeatable)")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select difficulty (1-3): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect difficulty (1-3): ")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print(f"{ERROR_COLOR}Invalid choice. Please enter 1, 2, or 3.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1, 2, or 3.")


def select_series_length():
    """Select the length of a best-of-N series."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Select Series Length:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} Single Game")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} Best of 3")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} Best of 5")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} Best of 7")
        print(f"  {X_COLOR}5.{Style.RESET_ALL} Best of 9")
    else:
        print("\nSelect Series Length:")
        print("  1. Single Game")
        print("  2. Best of 3")
        print("  3. Best of 5")
        print("  4. Best of 7")
        print("  5. Best of 9")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select option (1-5): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect option (1-5): ")
        options = {'1': 1, '2': 3, '3': 5, '4': 7, '5': 9}
        if choice in options:
            return options[choice]
        print(f"{ERROR_COLOR}Invalid choice. Please enter 1-5.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1-5.")


def select_timer_settings():
    """Select move timer settings."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Move Timer Settings:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} Timer OFF")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} Timer ON - 5 seconds")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} Timer ON - 10 seconds")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} Timer ON - 15 seconds")
        print(f"  {X_COLOR}5.{Style.RESET_ALL} Timer ON - 30 seconds")
    else:
        print("\nMove Timer Settings:")
        print("  1. Timer OFF")
        print("  2. Timer ON - 5 seconds")
        print("  3. Timer ON - 10 seconds")
        print("  4. Timer ON - 15 seconds")
        print("  5. Timer ON - 30 seconds")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select option (1-5): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect option (1-5): ")
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
            print(f"{ERROR_COLOR}Invalid choice. Please enter 1-5.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1-5.")


def select_handicap():
    """Select handicap for vs AI mode."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Select Handicap:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} None - Normal play")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} AI skips first turn - Human always goes first")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} AI random first move - AI's first move is random")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} Pre-placed piece - Human starts with center (5) marked")
    else:
        print("\nSelect Handicap:")
        print("  1. None - Normal play")
        print("  2. AI skips first turn - Human always goes first")
        print("  3. AI random first move - AI's first move is random")
        print("  4. Pre-placed piece - Human starts with center (5) marked")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select option (1-4): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect option (1-4): ")
        if choice == '1':
            return 'none'
        elif choice == '2':
            return 'ai_skips_first'
        elif choice == '3':
            return 'ai_random_first'
        elif choice == '4':
            return 'pre_placed'
        else:
            print(f"{ERROR_COLOR}Invalid choice. Please enter 1-4.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1-4.")


def select_ai_delay():
    """Select delay between AI moves for AI vs AI mode."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Select Move Delay:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} 500ms (Fast)")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} 1000ms (Normal)")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} 1500ms (Slow)")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} 2000ms (Very Slow)")
    else:
        print("\nSelect Move Delay:")
        print("  1. 500ms (Fast)")
        print("  2. 1000ms (Normal)")
        print("  3. 1500ms (Slow)")
        print("  4. 2000ms (Very Slow)")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select option (1-4): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect option (1-4): ")
        delays = {'1': 0.5, '2': 1.0, '3': 1.5, '4': 2.0}
        if choice in delays:
            return delays[choice]
        print(f"{ERROR_COLOR}Invalid choice. Please enter 1-4.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1-4.")


def select_replay_speed():
    """Select replay animation speed."""
    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Select Replay Speed:{Style.RESET_ALL}")
        print(f"  {X_COLOR}1.{Style.RESET_ALL} Slow (2.0s)")
        print(f"  {X_COLOR}2.{Style.RESET_ALL} Normal (1.0s)")
        print(f"  {X_COLOR}3.{Style.RESET_ALL} Fast (0.3s)")
        print(f"  {X_COLOR}4.{Style.RESET_ALL} Skip to end")
    else:
        print("\nSelect Replay Speed:")
        print("  1. Slow (2.0s)")
        print("  2. Normal (1.0s)")
        print("  3. Fast (0.3s)")
        print("  4. Skip to end")

    while True:
        choice = input(f"\n{PROMPT_COLOR}Select option (1-4): {Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect option (1-4): ")
        speeds = {'1': 2.0, '2': 1.0, '3': 0.3, '4': 0}
        if choice in speeds:
            return speeds[choice]
        print(f"{ERROR_COLOR}Invalid choice. Please enter 1-4.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid choice. Please enter 1-4.")


def replay_game(move_history, winner_symbol=None, winning_line=None):
    """Animate the game replay move by move."""
    delay = select_replay_speed()

    board = Board()

    if delay == 0:
        # Skip to end - just show final board
        clear_screen()
        for move in move_history:
            board.grid[move['position'] - 1] = move['symbol']
            board.last_move = move['position'] - 1
        if COLORS_ENABLED:
            print(f"\n{TITLE_COLOR}REPLAY - Final Position{Style.RESET_ALL}\n")
        else:
            print("\nREPLAY - Final Position\n")
        board.display(winning_line=winning_line)
        return

    # Animated replay
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}REPLAY{Style.RESET_ALL}\n")
    else:
        print("\nREPLAY\n")
    board.display()
    time.sleep(delay)

    for i, move in enumerate(move_history):
        clear_screen()
        if COLORS_ENABLED:
            print(f"\n{TITLE_COLOR}REPLAY - Move {i + 1}/{len(move_history)}{Style.RESET_ALL}\n")
        else:
            print(f"\nREPLAY - Move {i + 1}/{len(move_history)}\n")

        board.grid[move['position'] - 1] = move['symbol']
        board.last_move = move['position'] - 1

        # Show winning line on last move if there's a winner
        if i == len(move_history) - 1 and winning_line:
            board.display(winning_line=winning_line)
        else:
            board.display()

        symbol_color = X_COLOR if move['symbol'] == 'X' else O_COLOR
        if COLORS_ENABLED:
            print(f"{symbol_color}{move['symbol']}{Style.RESET_ALL} played position {move['position']}")
        else:
            print(f"{move['symbol']} played position {move['position']}")

        time.sleep(delay)

    if COLORS_ENABLED:
        print(f"\n{SUCCESS_COLOR}[Replay complete]{Style.RESET_ALL}")
    else:
        print("\n[Replay complete]")


def play_game(player1, player2, game_mode, difficulty=None, handicap='none', enable_undo=True):
    """Play a single game and return the winner (player object or None for draw)."""
    board = Board()
    current_player = player1
    players = {player1.symbol: player1, player2.symbol: player2}

    # Track move history for replay
    game_moves = []

    # Determine human player symbol for stats
    human_symbol = 'X'
    if game_mode == 'vs_ai':
        if isinstance(player1, (HumanPlayer, TimedHumanPlayer)):
            human_symbol = 'X'
        else:
            human_symbol = 'O'

    # Start game logging
    start_game_log(
        game_mode=game_mode,
        player_x=player1.name,
        player_o=player2.name,
        ai_difficulty=difficulty
    )

    # Apply handicaps
    ai_first_move_random = False
    if handicap == 'pre_placed':
        # Pre-place center for human
        pre_symbol = 'X' if isinstance(player1, (HumanPlayer, TimedHumanPlayer)) else 'O'
        board.make_move(5, pre_symbol)
        game_moves.append({'position': 5, 'symbol': pre_symbol})
        log_move(pre_symbol, 5)
        if COLORS_ENABLED:
            print(f"\n{SUCCESS_COLOR}Handicap applied: Center position (5) pre-marked for human!{Style.RESET_ALL}")
        else:
            print("\nHandicap applied: Center position (5) pre-marked for human!")
    elif handicap == 'ai_random_first':
        ai_first_move_random = True
        if COLORS_ENABLED:
            print(f"\n{SUCCESS_COLOR}Handicap applied: AI's first move will be random!{Style.RESET_ALL}")
        else:
            print("\nHandicap applied: AI's first move will be random!")
    elif handicap == 'ai_skips_first':
        # Ensure human goes first
        if isinstance(player1, AIPlayer):
            current_player = player2
            if COLORS_ENABLED:
                print(f"\n{SUCCESS_COLOR}Handicap applied: AI skips first turn, human goes first!{Style.RESET_ALL}")
            else:
                print("\nHandicap applied: AI skips first turn, human goes first!")

    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}Game Start!{Style.RESET_ALL}")
    else:
        print("\nGame Start!")
    board.display_positions()

    first_ai_move_done = False

    while not board.is_game_over():
        clear_screen()

        # Show game info header
        if COLORS_ENABLED:
            print(f"\n{TITLE_COLOR}TIC-TAC-TOE{Style.RESET_ALL}")
        else:
            print("\nTIC-TAC-TOE")

        board.display()

        # Handle AI random first move handicap
        if ai_first_move_random and isinstance(current_player, AIPlayer) and not first_ai_move_done:
            if COLORS_ENABLED:
                print(f"{PROMPT_COLOR}{current_player.name} ({current_player.symbol}) is thinking...{Style.RESET_ALL}")
            else:
                print(f"{current_player.name} ({current_player.symbol}) is thinking...")
            available = board.get_available_moves()
            move = random.choice(available)
            if COLORS_ENABLED:
                print(f"{SUCCESS_COLOR}{current_player.name} chooses position {move} (random handicap){Style.RESET_ALL}")
            else:
                print(f"{current_player.name} chooses position {move} (random handicap)")
            first_ai_move_done = True
        else:
            # Determine if undo is allowed for this player
            allow_undo = enable_undo and isinstance(current_player, (HumanPlayer, TimedHumanPlayer))

            move = current_player.get_move(board, allow_undo=allow_undo)

            # Handle undo
            if move == 'undo':
                if game_mode == 'vs_ai':
                    # Undo both player's and AI's last move
                    undone = board.undo_move()
                    if undone:
                        game_moves.pop() if game_moves else None
                    undone = board.undo_move()
                    if undone:
                        game_moves.pop() if game_moves else None
                    if COLORS_ENABLED:
                        print(f"{SUCCESS_COLOR}Undone your move and AI's move!{Style.RESET_ALL}")
                    else:
                        print("Undone your move and AI's move!")
                else:
                    # PvP: just undo last move
                    undone = board.undo_move()
                    if undone:
                        game_moves.pop() if game_moves else None
                        # Switch back to previous player
                        current_player = player2 if current_player == player1 else player1
                    if COLORS_ENABLED:
                        print(f"{SUCCESS_COLOR}Move undone!{Style.RESET_ALL}")
                    else:
                        print("Move undone!")
                time.sleep(0.5)
                continue

        board.make_move(move, current_player.symbol)
        game_moves.append({'position': move, 'symbol': current_player.symbol})
        log_move(current_player.symbol, move)

        # Switch players
        current_player = player2 if current_player == player1 else player1

    # Game over - show final board with winning line
    clear_screen()
    winning_line = board.get_winning_line()
    board.display(winning_line=winning_line)

    winner = board.check_winner()
    if winner:
        winning_player = players[winner]
        if COLORS_ENABLED:
            winner_color = X_COLOR if winner == 'X' else O_COLOR
            print(f"\n{winner_color}{winning_player.name} ({winner}) wins!{Style.RESET_ALL}")
        else:
            print(f"\n{winning_player.name} ({winner}) wins!")

        if game_mode == 'pvp':
            update_pvp_stats(1 if winner == 'X' else 2, 'X')
        elif game_mode == 'vs_ai':
            if isinstance(winning_player, (HumanPlayer, TimedHumanPlayer)):
                update_ai_stats(difficulty, 'win', human_symbol)
            else:
                update_ai_stats(difficulty, 'loss', human_symbol)

        # Offer replay
        replay_choice = input(f"\n{PROMPT_COLOR}Watch replay? (y/n): {Style.RESET_ALL}" if COLORS_ENABLED else "\nWatch replay? (y/n): ").strip().lower()
        if replay_choice == 'y':
            replay_game(game_moves, winner, winning_line)

        return winning_player
    else:
        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}It's a draw!{Style.RESET_ALL}")
        else:
            print("\nIt's a draw!")

        if game_mode == 'pvp':
            update_pvp_stats(None, 'X')
        elif game_mode == 'vs_ai':
            update_ai_stats(difficulty, 'draw', human_symbol)

        # Offer replay
        replay_choice = input(f"\n{PROMPT_COLOR}Watch replay? (y/n): {Style.RESET_ALL}" if COLORS_ENABLED else "\nWatch replay? (y/n): ").strip().lower()
        if replay_choice == 'y':
            replay_game(game_moves)

        return None


def play_series(player1, player2, game_mode, series_length, difficulty=None, handicap='none', timer_enabled=False, timer_duration=15):
    """Play a best-of-N series."""
    wins_needed = (series_length // 2) + 1
    scores = {player1.name: 0, player2.name: 0}
    draws = 0
    round_num = 1

    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}{'='*40}")
        print(f"   BEST OF {series_length} SERIES")
        print(f"   First to {wins_needed} wins!")
        print(f"{'='*40}{Style.RESET_ALL}")
    else:
        print(f"\n{'='*40}")
        print(f"   BEST OF {series_length} SERIES")
        print(f"   First to {wins_needed} wins!")
        print(f"{'='*40}")

    while scores[player1.name] < wins_needed and scores[player2.name] < wins_needed:
        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}--- Round {round_num} ---{Style.RESET_ALL}")
            print(f"Score: {X_COLOR}{player1.name}: {scores[player1.name]}{Style.RESET_ALL} | {O_COLOR}{player2.name}: {scores[player2.name]}{Style.RESET_ALL} | Draws: {draws}")
        else:
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
        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}Current Score: {X_COLOR}{player1.name}: {scores[player1.name]}{Style.RESET_ALL} | {O_COLOR}{player2.name}: {scores[player2.name]}{Style.RESET_ALL}")
        else:
            print(f"\nCurrent Score: {player1.name}: {scores[player1.name]} | {player2.name}: {scores[player2.name]}")
        choice = input(f"{PROMPT_COLOR}Press Enter for next round or 'Q' to end series: {Style.RESET_ALL}" if COLORS_ENABLED else "Press Enter for next round or 'Q' to end series: ").strip().upper()
        if choice == 'Q':
            break

    # Display final results
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}{'='*40}")
        print("   SERIES COMPLETE!")
        print(f"{'='*40}{Style.RESET_ALL}")
        print(f"Final Score: {X_COLOR}{player1.name}: {scores[player1.name]}{Style.RESET_ALL} | {O_COLOR}{player2.name}: {scores[player2.name]}{Style.RESET_ALL} | Draws: {draws}")
    else:
        print(f"\n{'='*40}")
        print("   SERIES COMPLETE!")
        print(f"{'='*40}")
        print(f"Final Score: {player1.name}: {scores[player1.name]} | {player2.name}: {scores[player2.name]} | Draws: {draws}")

    if scores[player1.name] > scores[player2.name]:
        if COLORS_ENABLED:
            print(f"\n{SUCCESS_COLOR}{player1.name} wins the series!{Style.RESET_ALL}")
        else:
            print(f"\n{player1.name} wins the series!")
    elif scores[player2.name] > scores[player1.name]:
        if COLORS_ENABLED:
            print(f"\n{SUCCESS_COLOR}{player2.name} wins the series!{Style.RESET_ALL}")
        else:
            print(f"\n{player2.name} wins the series!")
    else:
        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}The series ends in a tie!{Style.RESET_ALL}")
        else:
            print("\nThe series ends in a tie!")


def play_pvp():
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}--- Player vs Player ---{Style.RESET_ALL}")
    else:
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
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}--- Player vs AI ---{Style.RESET_ALL}")
    else:
        print("\n--- Player vs AI ---")

    difficulty = select_difficulty()

    # Feature 2: Series mode
    series_length = select_series_length()

    # Feature 5: Timer settings
    timer_enabled, timer_duration = select_timer_settings()

    # Feature 4: Handicap selection
    handicap = select_handicap()

    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Do you want to go first?{Style.RESET_ALL}")
        choice = input(f"{PROMPT_COLOR}Enter Y for yes, N for no: {Style.RESET_ALL}").strip().upper()
    else:
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
    clear_screen()
    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}--- AI vs AI ---{Style.RESET_ALL}")
    else:
        print("\n--- AI vs AI ---")

    print(f"\n{PROMPT_COLOR}Select AI 1 (X) difficulty:{Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect AI 1 (X) difficulty:")
    difficulty1 = select_difficulty()

    print(f"\n{PROMPT_COLOR}Select AI 2 (O) difficulty:{Style.RESET_ALL}" if COLORS_ENABLED else "\nSelect AI 2 (O) difficulty:")
    difficulty2 = select_difficulty()

    delay = select_ai_delay()

    player1 = AIPlayer('X', difficulty1, f"AI-1 ({difficulty1})")
    player2 = AIPlayer('O', difficulty2, f"AI-2 ({difficulty2})")

    board = Board()
    current_player = player1
    players = {player1.symbol: player1, player2.symbol: player2}
    game_moves = []

    if COLORS_ENABLED:
        print(f"\n{TITLE_COLOR}Game Start!{Style.RESET_ALL}")
    else:
        print("\nGame Start!")
    board.display_positions()

    while not board.is_game_over():
        clear_screen()
        if COLORS_ENABLED:
            print(f"\n{TITLE_COLOR}AI vs AI{Style.RESET_ALL}")
        else:
            print("\nAI vs AI")
        board.display()

        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}{current_player.name} is thinking...{Style.RESET_ALL}")
        else:
            print(f"\n{current_player.name} is thinking...")
        time.sleep(delay)

        move = current_player.get_move(board)
        board.make_move(move, current_player.symbol)
        game_moves.append({'position': move, 'symbol': current_player.symbol})

        # Switch players
        current_player = player2 if current_player == player1 else player1

    clear_screen()
    winning_line = board.get_winning_line()
    board.display(winning_line=winning_line)

    winner = board.check_winner()
    if winner:
        winning_player = players[winner]
        if COLORS_ENABLED:
            winner_color = X_COLOR if winner == 'X' else O_COLOR
            print(f"\n{winner_color}{winning_player.name} ({winner}) wins!{Style.RESET_ALL}")
        else:
            print(f"\n{winning_player.name} ({winner}) wins!")
    else:
        if COLORS_ENABLED:
            print(f"\n{PROMPT_COLOR}It's a draw!{Style.RESET_ALL}")
        else:
            print("\nIt's a draw!")

    if COLORS_ENABLED:
        print(f"\n{PROMPT_COLOR}Match: {player1.name} vs {player2.name}{Style.RESET_ALL}")
    else:
        print(f"\nMatch: {player1.name} vs {player2.name}")

    # Offer replay
    replay_choice = input(f"\n{PROMPT_COLOR}Watch replay? (y/n): {Style.RESET_ALL}" if COLORS_ENABLED else "\nWatch replay? (y/n): ").strip().lower()
    if replay_choice == 'y':
        replay_game(game_moves, winner, winning_line)


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
            clear_screen()
            display_stats()
        elif choice == '5':
            clear_screen()
            display_history()
        elif choice == '6':
            clear_screen()
            export_stats_interactive()
        elif choice == '7':
            confirm = input(f"{PROMPT_COLOR}Are you sure you want to reset statistics? (Y/N): {Style.RESET_ALL}" if COLORS_ENABLED else "Are you sure you want to reset statistics? (Y/N): ")
            if confirm.strip().upper() == 'Y':
                reset_stats()
        elif choice == '8':
            clear_screen()
            if COLORS_ENABLED:
                print(f"\n{SUCCESS_COLOR}Thanks for playing! Goodbye!{Style.RESET_ALL}")
            else:
                print("\nThanks for playing! Goodbye!")
            break
        else:
            print(f"{ERROR_COLOR}Invalid option. Please enter 1-8.{Style.RESET_ALL}" if COLORS_ENABLED else "Invalid option. Please enter 1-8.")

        input(f"\n{PROMPT_COLOR}Press Enter to continue...{Style.RESET_ALL}" if COLORS_ENABLED else "\nPress Enter to continue...")
        clear_screen()


if __name__ == "__main__":
    main()
