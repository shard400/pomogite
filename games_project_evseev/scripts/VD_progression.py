import random
from VD_games.engine import run_game

GAME_RULES = 'What number is missing in the progression?'

def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию."""
    return [start + i * step for i in range(length)]

def generate_round():
    """Генерирует один раунд игры."""
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    
    question = ' '.join(map(str, progression))
    return question, correct_answer

def main():
    run_game('scripts.VD_progression')

if __name__ == "__main__":
    main()
