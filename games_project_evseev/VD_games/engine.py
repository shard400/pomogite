import importlib

def run_game(game_module_name):
    """Основной движок для запуска всех игр."""
    game_module = importlib.import_module(game_module_name)
    
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    print(game_module.GAME_RULES)
    
    correct_answers_count = 0
    rounds_to_win = 3
    
    while correct_answers_count < rounds_to_win:
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == str(correct_answer).lower():
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
