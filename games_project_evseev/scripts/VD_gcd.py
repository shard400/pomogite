import random
import math


def find_gcd(a, b):
    return math.gcd(a, b)


def play_gcd_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    
    correct_answers_count = 0
    rounds_to_win = 3
    
    while correct_answers_count < rounds_to_win:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)
        
        print(f"Question: {num1} {num2}")
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
    play_gcd_game()


if __name__ == "__main__":
    main()
