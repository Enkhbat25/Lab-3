import json
import os

STATS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'stats.json')

DEFAULT_STATS = {
    'pvp': {
        'player1_wins': 0,
        'player2_wins': 0,
        'draws': 0
    },
    'vs_ai': {
        'easy': {'wins': 0, 'losses': 0, 'draws': 0},
        'medium': {'wins': 0, 'losses': 0, 'draws': 0},
        'hard': {'wins': 0, 'losses': 0, 'draws': 0}
    }
}


def load_stats():
    try:
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_STATS.copy()


def save_stats(stats):
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)


def update_pvp_stats(winner):
    """Update PvP stats. winner is 1, 2, or None for draw."""
    stats = load_stats()
    if winner == 1:
        stats['pvp']['player1_wins'] += 1
    elif winner == 2:
        stats['pvp']['player2_wins'] += 1
    else:
        stats['pvp']['draws'] += 1
    save_stats(stats)


def update_ai_stats(difficulty, result):
    """Update AI stats. result is 'win', 'loss', or 'draw'."""
    stats = load_stats()
    if result == 'win':
        stats['vs_ai'][difficulty]['wins'] += 1
    elif result == 'loss':
        stats['vs_ai'][difficulty]['losses'] += 1
    else:
        stats['vs_ai'][difficulty]['draws'] += 1
    save_stats(stats)


def display_stats():
    stats = load_stats()

    print("\n" + "=" * 40)
    print("           GAME STATISTICS")
    print("=" * 40)

    print("\n--- Player vs Player ---")
    pvp = stats['pvp']
    total_pvp = pvp['player1_wins'] + pvp['player2_wins'] + pvp['draws']
    print(f"  Total Games: {total_pvp}")
    print(f"  Player 1 (X) Wins: {pvp['player1_wins']}")
    print(f"  Player 2 (O) Wins: {pvp['player2_wins']}")
    print(f"  Draws: {pvp['draws']}")

    print("\n--- Player vs AI ---")
    for difficulty in ['easy', 'medium', 'hard']:
        ai_stats = stats['vs_ai'][difficulty]
        total = ai_stats['wins'] + ai_stats['losses'] + ai_stats['draws']
        print(f"\n  {difficulty.upper()} Difficulty:")
        print(f"    Total Games: {total}")
        print(f"    Your Wins: {ai_stats['wins']}")
        print(f"    AI Wins: {ai_stats['losses']}")
        print(f"    Draws: {ai_stats['draws']}")

    print("\n" + "=" * 40)


def reset_stats():
    save_stats(DEFAULT_STATS.copy())
    print("Statistics have been reset.")
