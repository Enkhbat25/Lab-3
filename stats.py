import json
import os
import csv
import uuid
from datetime import datetime
from typing import Optional, Dict, List, Any

STATS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'stats.json')
HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'data', 'game_history.json')
MAX_HISTORY_GAMES = 100

DEFAULT_STATS = {
    'version': '2.0',
    'last_updated': None,
    'pvp': {
        'player1_wins': 0,
        'player2_wins': 0,
        'draws': 0
    },
    'vs_ai': {
        'easy': {'wins': 0, 'losses': 0, 'draws': 0},
        'medium': {'wins': 0, 'losses': 0, 'draws': 0},
        'hard': {'wins': 0, 'losses': 0, 'draws': 0}
    },
    'as_x': {'wins': 0, 'losses': 0, 'draws': 0},
    'as_o': {'wins': 0, 'losses': 0, 'draws': 0},
    'streaks': {
        'current_win': 0,
        'current_loss': 0,
        'current_unbeaten': 0,
        'best_win': 0,
        'best_loss': 0,
        'best_unbeaten': 0
    }
}

DEFAULT_HISTORY = {
    'version': '1.0',
    'games': []
}

# Current game tracking
current_game = {
    'game_id': None,
    'start_time': None,
    'moves': [],
    'game_mode': None,
    'player_x': None,
    'player_o': None,
    'ai_difficulty': None
}


def load_stats() -> Dict:
    """Load statistics from file with migration support."""
    try:
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
            # Migrate old stats format if needed
            if 'version' not in stats:
                stats = migrate_stats(stats)
            return stats
    except (FileNotFoundError, json.JSONDecodeError):
        return get_default_stats()


def get_default_stats() -> Dict:
    """Return a fresh copy of default stats."""
    stats = json.loads(json.dumps(DEFAULT_STATS))
    stats['last_updated'] = datetime.now().isoformat()
    return stats


def migrate_stats(old_stats: Dict) -> Dict:
    """Migrate old stats format to new format."""
    new_stats = get_default_stats()

    # Copy over existing data
    if 'pvp' in old_stats:
        new_stats['pvp'] = old_stats['pvp']
    if 'vs_ai' in old_stats:
        new_stats['vs_ai'] = old_stats['vs_ai']

    return new_stats


def save_stats(stats: Dict) -> None:
    """Save statistics to file."""
    stats['last_updated'] = datetime.now().isoformat()
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)


def load_history() -> Dict:
    """Load game history from file."""
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return json.loads(json.dumps(DEFAULT_HISTORY))


def save_history(history: Dict) -> None:
    """Save game history to file, limiting to MAX_HISTORY_GAMES."""
    # Limit history size
    if len(history['games']) > MAX_HISTORY_GAMES:
        history['games'] = history['games'][-MAX_HISTORY_GAMES:]

    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)


# ============================================
# Win Rate Calculations
# ============================================

def calculate_win_rate(wins: int, total: int) -> str:
    """Calculate win rate percentage, handling division by zero."""
    if total == 0:
        return "N/A"
    rate = (wins / total) * 100
    return f"{rate:.1f}%"


def get_overall_stats() -> Dict:
    """Get overall statistics across all modes."""
    stats = load_stats()

    # PvP totals
    pvp = stats['pvp']
    pvp_total = pvp['player1_wins'] + pvp['player2_wins'] + pvp['draws']
    pvp_wins = pvp['player1_wins']  # Assuming player 1 is the main user

    # AI totals
    ai_wins = 0
    ai_losses = 0
    ai_draws = 0
    for diff in ['easy', 'medium', 'hard']:
        ai_wins += stats['vs_ai'][diff]['wins']
        ai_losses += stats['vs_ai'][diff]['losses']
        ai_draws += stats['vs_ai'][diff]['draws']
    ai_total = ai_wins + ai_losses + ai_draws

    # Overall
    total_games = pvp_total + ai_total
    total_wins = pvp_wins + ai_wins

    return {
        'total_games': total_games,
        'total_wins': total_wins,
        'overall_win_rate': calculate_win_rate(total_wins, total_games),
        'pvp_total': pvp_total,
        'pvp_win_rate': calculate_win_rate(pvp_wins, pvp_total),
        'ai_total': ai_total,
        'ai_wins': ai_wins,
        'ai_win_rate': calculate_win_rate(ai_wins, ai_total),
        'ai_by_difficulty': {
            diff: {
                'total': stats['vs_ai'][diff]['wins'] + stats['vs_ai'][diff]['losses'] + stats['vs_ai'][diff]['draws'],
                'wins': stats['vs_ai'][diff]['wins'],
                'win_rate': calculate_win_rate(
                    stats['vs_ai'][diff]['wins'],
                    stats['vs_ai'][diff]['wins'] + stats['vs_ai'][diff]['losses'] + stats['vs_ai'][diff]['draws']
                )
            }
            for diff in ['easy', 'medium', 'hard']
        }
    }


def get_symbol_stats() -> Dict:
    """Get win rates when playing as X vs O."""
    stats = load_stats()
    as_x = stats.get('as_x', {'wins': 0, 'losses': 0, 'draws': 0})
    as_o = stats.get('as_o', {'wins': 0, 'losses': 0, 'draws': 0})

    x_total = as_x['wins'] + as_x['losses'] + as_x['draws']
    o_total = as_o['wins'] + as_o['losses'] + as_o['draws']

    return {
        'as_x': {
            'total': x_total,
            'wins': as_x['wins'],
            'win_rate': calculate_win_rate(as_x['wins'], x_total)
        },
        'as_o': {
            'total': o_total,
            'wins': as_o['wins'],
            'win_rate': calculate_win_rate(as_o['wins'], o_total)
        }
    }


# ============================================
# Streak Tracking
# ============================================

def update_streak(result: str, stats: Dict) -> bool:
    """
    Update streak counters after a game.
    result: 'win', 'loss', or 'draw'
    Returns True if a new best streak was achieved.
    """
    streaks = stats.get('streaks', DEFAULT_STATS['streaks'].copy())
    new_best = False

    if result == 'win':
        streaks['current_win'] += 1
        streaks['current_loss'] = 0
        streaks['current_unbeaten'] += 1

        if streaks['current_win'] > streaks['best_win']:
            streaks['best_win'] = streaks['current_win']
            new_best = True

    elif result == 'loss':
        streaks['current_loss'] += 1
        streaks['current_win'] = 0
        streaks['current_unbeaten'] = 0

        if streaks['current_loss'] > streaks['best_loss']:
            streaks['best_loss'] = streaks['current_loss']

    else:  # draw
        streaks['current_win'] = 0
        streaks['current_loss'] = 0
        streaks['current_unbeaten'] += 1

    if streaks['current_unbeaten'] > streaks['best_unbeaten']:
        streaks['best_unbeaten'] = streaks['current_unbeaten']

    stats['streaks'] = streaks
    return new_best


def get_streak_display(stats: Dict) -> str:
    """Get formatted streak display string."""
    streaks = stats.get('streaks', DEFAULT_STATS['streaks'].copy())

    current = streaks['current_win']
    if current > 0:
        streak_text = f"[HOT] {current} win{'s' if current != 1 else ''}"
    elif streaks['current_loss'] > 0:
        streak_text = f"[COLD] {streaks['current_loss']} loss{'es' if streaks['current_loss'] != 1 else ''}"
    elif streaks['current_unbeaten'] > 0:
        streak_text = f"[*] {streaks['current_unbeaten']} unbeaten"
    else:
        streak_text = "None"

    return streak_text


# ============================================
# Move History Logging
# ============================================

def start_game_log(game_mode: str, player_x: str = "Player 1", player_o: str = "Player 2",
                   ai_difficulty: str = None) -> str:
    """Start logging a new game. Returns game_id."""
    global current_game

    game_id = str(uuid.uuid4())[:8]
    current_game = {
        'game_id': game_id,
        'start_time': datetime.now().isoformat(),
        'moves': [],
        'game_mode': game_mode,
        'player_x': player_x,
        'player_o': player_o,
        'ai_difficulty': ai_difficulty,
        'last_move_time': datetime.now()
    }

    return game_id


def log_move(player: str, position: int) -> None:
    """Record a single move to the current game."""
    global current_game

    if current_game['game_id'] is None:
        return

    now = datetime.now()
    time_taken = (now - current_game.get('last_move_time', now)).total_seconds()

    move_record = {
        'turn': len(current_game['moves']) + 1,
        'player': player,
        'position': position,
        'time_taken': round(time_taken, 2)
    }

    current_game['moves'].append(move_record)
    current_game['last_move_time'] = now


def end_game_log(result: str) -> Dict:
    """
    End the current game log and save to history.
    result: 'X_win', 'O_win', or 'draw'
    Returns the completed game record.
    """
    global current_game

    if current_game['game_id'] is None:
        return {}

    end_time = datetime.now()
    start_time = datetime.fromisoformat(current_game['start_time'])
    duration = (end_time - start_time).total_seconds()

    game_record = {
        'game_id': current_game['game_id'],
        'timestamp': current_game['start_time'],
        'game_mode': current_game['game_mode'],
        'player_x': current_game['player_x'],
        'player_o': current_game['player_o'],
        'ai_difficulty': current_game['ai_difficulty'],
        'moves': current_game['moves'],
        'result': result,
        'total_moves': len(current_game['moves']),
        'duration_seconds': round(duration, 1)
    }

    # Save to history
    history = load_history()
    history['games'].append(game_record)
    save_history(history)

    # Reset current game
    current_game = {
        'game_id': None,
        'start_time': None,
        'moves': [],
        'game_mode': None,
        'player_x': None,
        'player_o': None,
        'ai_difficulty': None
    }

    return game_record


def analyze_patterns() -> Dict:
    """Analyze move patterns from history."""
    history = load_history()
    games = history.get('games', [])

    if not games:
        return {
            'total_games': 0,
            'avg_moves': 0,
            'avg_duration': 0,
            'opening_moves': {},
            'position_frequency': [0] * 9
        }

    total_moves = 0
    total_duration = 0
    opening_moves = {}
    position_frequency = [0] * 9
    total_move_time = 0
    move_count = 0

    for game in games:
        total_moves += game.get('total_moves', 0)
        total_duration += game.get('duration_seconds', 0)

        moves = game.get('moves', [])
        if moves:
            # Track opening moves
            first_move = moves[0]['position']
            opening_moves[first_move] = opening_moves.get(first_move, 0) + 1

            # Track all positions
            for move in moves:
                pos = move['position']
                if 0 <= pos <= 8:
                    position_frequency[pos] += 1
                total_move_time += move.get('time_taken', 0)
                move_count += 1

    num_games = len(games)

    return {
        'total_games': num_games,
        'avg_moves': round(total_moves / num_games, 1) if num_games > 0 else 0,
        'avg_duration': round(total_duration / num_games, 1) if num_games > 0 else 0,
        'avg_time_per_move': round(total_move_time / move_count, 2) if move_count > 0 else 0,
        'opening_moves': opening_moves,
        'position_frequency': position_frequency,
        'favorite_position': position_frequency.index(max(position_frequency)) + 1 if max(position_frequency) > 0 else None
    }


# ============================================
# CSV Export
# ============================================

def export_to_csv(filepath: str = None, num_games: int = None,
                  mode_filter: str = None, date_from: str = None,
                  date_to: str = None) -> str:
    """
    Export statistics to CSV file.
    Returns the filepath of the created file.
    """
    if filepath is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(os.path.dirname(__file__), 'data', f'tictactoe_stats_{timestamp}.csv')

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Load data
    stats = load_stats()
    history = load_history()
    games = history.get('games', [])

    # Apply filters
    filtered_games = games.copy()

    if mode_filter:
        filtered_games = [g for g in filtered_games if g.get('game_mode') == mode_filter]

    if date_from:
        filtered_games = [g for g in filtered_games if g.get('timestamp', '') >= date_from]

    if date_to:
        filtered_games = [g for g in filtered_games if g.get('timestamp', '') <= date_to]

    if num_games:
        filtered_games = filtered_games[-num_games:]

    # Get overall stats
    overall = get_overall_stats()
    streaks = stats.get('streaks', {})

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Write summary header
            writer.writerow([f'# Tic-Tac-Toe Statistics Export - Generated: {datetime.now().isoformat()}'])
            writer.writerow([f'# Total Games: {overall["total_games"]}'])
            writer.writerow([f'# Overall Win Rate: {overall["overall_win_rate"]}'])
            writer.writerow([f'# Best Win Streak: {streaks.get("best_win", 0)}'])
            writer.writerow([])

            # Write column headers
            writer.writerow([
                'game_id', 'date', 'time', 'mode', 'player_x', 'player_o',
                'ai_difficulty', 'winner', 'total_moves', 'duration_seconds', 'move_sequence'
            ])

            # Write game data
            for game in filtered_games:
                timestamp = game.get('timestamp', '')
                date_part = timestamp[:10] if timestamp else ''
                time_part = timestamp[11:19] if len(timestamp) > 11 else ''

                # Format move sequence
                moves = game.get('moves', [])
                move_sequence = '-'.join([str(m['position']) for m in moves])

                # Determine winner
                result = game.get('result', '')
                if result == 'X_win':
                    winner = game.get('player_x', 'X')
                elif result == 'O_win':
                    winner = game.get('player_o', 'O')
                else:
                    winner = 'Draw'

                writer.writerow([
                    game.get('game_id', ''),
                    date_part,
                    time_part,
                    game.get('game_mode', ''),
                    game.get('player_x', ''),
                    game.get('player_o', ''),
                    game.get('ai_difficulty', ''),
                    winner,
                    game.get('total_moves', ''),
                    game.get('duration_seconds', ''),
                    move_sequence
                ])

        return filepath

    except (IOError, PermissionError) as e:
        print(f"Error exporting to CSV: {e}")
        return None


# ============================================
# Stats Update Functions (Enhanced)
# ============================================

def update_pvp_stats(winner, player_symbol: str = 'X'):
    """
    Update PvP stats. winner is 1, 2, or None for draw.
    player_symbol: The symbol the main player was using.
    """
    stats = load_stats()

    # Ensure new fields exist
    if 'streaks' not in stats:
        stats['streaks'] = DEFAULT_STATS['streaks'].copy()
    if 'as_x' not in stats:
        stats['as_x'] = {'wins': 0, 'losses': 0, 'draws': 0}
    if 'as_o' not in stats:
        stats['as_o'] = {'wins': 0, 'losses': 0, 'draws': 0}

    # Update basic stats
    if winner == 1:
        stats['pvp']['player1_wins'] += 1
        result = 'win'
    elif winner == 2:
        stats['pvp']['player2_wins'] += 1
        result = 'loss'
    else:
        stats['pvp']['draws'] += 1
        result = 'draw'

    # Update symbol stats (assuming player 1 is main user)
    if player_symbol == 'X':
        if winner == 1:
            stats['as_x']['wins'] += 1
        elif winner == 2:
            stats['as_x']['losses'] += 1
        else:
            stats['as_x']['draws'] += 1
    else:
        if winner == 2:
            stats['as_o']['wins'] += 1
        elif winner == 1:
            stats['as_o']['losses'] += 1
        else:
            stats['as_o']['draws'] += 1

    # Update streaks
    new_best = update_streak(result, stats)

    save_stats(stats)

    # End game log
    if winner == 1:
        end_game_log('X_win' if player_symbol == 'X' else 'O_win')
    elif winner == 2:
        end_game_log('O_win' if player_symbol == 'X' else 'X_win')
    else:
        end_game_log('draw')

    if new_best:
        print(f"\n*** NEW BEST WIN STREAK: {stats['streaks']['best_win']}! ***")


def update_ai_stats(difficulty, result, player_symbol: str = 'X'):
    """
    Update AI stats. result is 'win', 'loss', or 'draw'.
    player_symbol: The symbol the human player was using.
    """
    stats = load_stats()

    # Ensure new fields exist
    if 'streaks' not in stats:
        stats['streaks'] = DEFAULT_STATS['streaks'].copy()
    if 'as_x' not in stats:
        stats['as_x'] = {'wins': 0, 'losses': 0, 'draws': 0}
    if 'as_o' not in stats:
        stats['as_o'] = {'wins': 0, 'losses': 0, 'draws': 0}

    # Update basic stats
    if result == 'win':
        stats['vs_ai'][difficulty]['wins'] += 1
    elif result == 'loss':
        stats['vs_ai'][difficulty]['losses'] += 1
    else:
        stats['vs_ai'][difficulty]['draws'] += 1

    # Update symbol stats
    symbol_key = f'as_{player_symbol.lower()}'
    if symbol_key in stats:
        stats[symbol_key][result + 's' if result != 'loss' else 'losses'] += 1

    # Update streaks
    new_best = update_streak(result, stats)

    save_stats(stats)

    # End game log
    if result == 'win':
        game_result = 'X_win' if player_symbol == 'X' else 'O_win'
    elif result == 'loss':
        game_result = 'O_win' if player_symbol == 'X' else 'X_win'
    else:
        game_result = 'draw'
    end_game_log(game_result)

    if new_best:
        print(f"\n*** NEW BEST WIN STREAK: {stats['streaks']['best_win']}! ***")


# ============================================
# Display Functions
# ============================================

def display_stats():
    """Display comprehensive statistics."""
    stats = load_stats()
    overall = get_overall_stats()
    symbol_stats = get_symbol_stats()
    patterns = analyze_patterns()

    print("\n" + "=" * 50)
    print("              GAME STATISTICS")
    print("=" * 50)

    # Overall Stats
    print(f"\n  Games Played: {overall['total_games']}")
    print(f"  Overall Win Rate: {overall['overall_win_rate']} ({overall['total_wins']}/{overall['total_games']})")

    # Win Rate Breakdown
    print("\n  --- Win Rates by Mode ---")
    print(f"  | vs Easy AI:   {overall['ai_by_difficulty']['easy']['win_rate']}")
    print(f"  | vs Medium AI: {overall['ai_by_difficulty']['medium']['win_rate']}")
    print(f"  | vs Hard AI:   {overall['ai_by_difficulty']['hard']['win_rate']}")
    print(f"  + PvP:          {overall['pvp_win_rate']}")

    # Symbol Stats
    print("\n  --- Win Rates by Symbol ---")
    print(f"  | As X: {symbol_stats['as_x']['win_rate']} ({symbol_stats['as_x']['wins']}/{symbol_stats['as_x']['total']})")
    print(f"  + As O: {symbol_stats['as_o']['win_rate']} ({symbol_stats['as_o']['wins']}/{symbol_stats['as_o']['total']})")

    # Streaks
    streaks = stats.get('streaks', DEFAULT_STATS['streaks'].copy())
    print("\n  --- Streaks ---")
    print(f"  | Current: {get_streak_display(stats)}")
    print(f"  | Best Win Streak:     {streaks['best_win']}")
    print(f"  | Best Unbeaten:       {streaks['best_unbeaten']}")
    print(f"  + Worst Loss Streak:   {streaks['best_loss']}")

    # PvP Details
    print("\n  --- Player vs Player ---")
    pvp = stats['pvp']
    total_pvp = pvp['player1_wins'] + pvp['player2_wins'] + pvp['draws']
    print(f"  Total Games: {total_pvp}")
    print(f"  Player 1 (X) Wins: {pvp['player1_wins']}")
    print(f"  Player 2 (O) Wins: {pvp['player2_wins']}")
    print(f"  Draws: {pvp['draws']}")

    # AI Details
    print("\n  --- Player vs AI ---")
    for difficulty in ['easy', 'medium', 'hard']:
        ai_stats = stats['vs_ai'][difficulty]
        total = ai_stats['wins'] + ai_stats['losses'] + ai_stats['draws']
        print(f"\n  {difficulty.upper()}:")
        print(f"    Games: {total} | Wins: {ai_stats['wins']} | Losses: {ai_stats['losses']} | Draws: {ai_stats['draws']}")

    # Pattern Analysis
    if patterns['total_games'] > 0:
        print("\n  --- Game Patterns ---")
        print(f"  Avg Moves/Game: {patterns['avg_moves']}")
        print(f"  Avg Game Duration: {patterns['avg_duration']}s")
        print(f"  Avg Time/Move: {patterns['avg_time_per_move']}s")
        if patterns['favorite_position']:
            print(f"  Most Used Position: {patterns['favorite_position']}")

    print("\n" + "=" * 50)


def display_history(num_games: int = 10):
    """Display recent game history."""
    history = load_history()
    games = history.get('games', [])[-num_games:]

    if not games:
        print("\n  No game history available.")
        return

    print(f"\n  --- Last {len(games)} Games ---")
    for game in reversed(games):
        timestamp = game.get('timestamp', '')[:16].replace('T', ' ')
        mode = game.get('game_mode', 'unknown')
        result = game.get('result', 'unknown')
        moves = game.get('total_moves', 0)

        result_symbol = 'W' if 'X_win' in result else ('L' if 'O_win' in result else 'D')
        print(f"  [{result_symbol}] {timestamp} | {mode:8} | {result:7} | {moves} moves")


def reset_stats():
    """Reset all statistics after confirmation."""
    save_stats(get_default_stats())
    save_history(json.loads(json.dumps(DEFAULT_HISTORY)))
    print("Statistics and history have been reset.")


def export_stats_interactive():
    """Interactive CSV export."""
    print("\n  ─── Export Options ───")
    print("  1. Export all games")
    print("  2. Export last N games")
    print("  3. Export by mode")
    print("  4. Cancel")

    choice = input("\n  Select option (1-4): ").strip()

    if choice == '1':
        filepath = export_to_csv()
    elif choice == '2':
        try:
            n = int(input("  Number of games: ").strip())
            filepath = export_to_csv(num_games=n)
        except ValueError:
            print("  Invalid number.")
            return
    elif choice == '3':
        print("  Modes: pvp, vs_ai, ai_vs_ai")
        mode = input("  Enter mode: ").strip()
        filepath = export_to_csv(mode_filter=mode)
    else:
        print("  Export cancelled.")
        return

    if filepath:
        print(f"\n  ✓ Statistics exported to: {filepath}")
    else:
        print("\n  ✗ Export failed.")
