import random
from VD_games.engine import run_game

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_round():
    """Генерирует один раунд игры."""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer

def main():
    run_game('scripts.VD_prime')

if __name__ == "__main__":
    main()
