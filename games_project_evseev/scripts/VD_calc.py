import random
import operator


def calculate_expression(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](num1, num2)


def play_calc_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    
    correct_answers_count = 0
    rounds_to_win = 3
    
    while correct_answers_count < rounds_to_win:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*'])
        
        correct_answer = calculate_expression(num1, num2, operation)
        
        print(f"Question: {num1} {operation} {num2}")
        user_answer = input("Your answer: ").strip()
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    play_calc_game()


if __name__ == "__main__":
    main()
