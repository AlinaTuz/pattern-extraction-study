import random

def simulate_game() -> bool:
    """
    Simulates one round of the game and determines if Moriarty wins.

    Variables:
    - S: Accumulated sum.
    - x: Holmes' last chosen number.
    - y: Moriarty's last chosen number.

    Returns:
    - True if Moriarty wins (y > x), otherwise False.
    """

    S = 0
    x = 0
    y = 0

    # Holmes' turn
    while S < 100:
        x = random.randint(1, 100)
        S += x
    
    # Moriarty's turn
    while S < 200:
        y = random.randint(1, 100)
        S += y
    
    # Moriarty wins if his last chosen number is greater
    return y > x

def moriarty_win_probability(rounds: int) -> float:
    """Runs multiple simulations and estimates Moriarty's win probability."""
    moriarty_wins = sum(simulate_game() for _ in range(rounds))
    return moriarty_wins / rounds

if __name__ == "__main__":
    rounds = 100000
    probability = moriarty_win_probability(rounds)
    print(f"Moriarty's victory probability: {probability:.4%}")