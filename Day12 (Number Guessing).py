import random

Easy_chance=10
Hard_chance=5

def check(user_guess,actual,turns):
    """ Compares user choice with actual number"""
    if user_guess>actual:
        print("Too high...")
        return turns-1
    elif user_guess<actual:
        print("Too low...")
        return turns-1
    else:
        print("You guessed it right.")

def difficulty():
    difficulty_level=input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level=="easy":
        return Easy_chance
    else:
        return Hard_chance

def game():
    print("Welcome to the number guessing game.")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    turns=difficulty()

    guess=0
    while guess!=answer:
        print(f"You have {turns} chances left.")
        guess=int(input("Guess a number: "))
        turns=check(guess,answer,turns)
        if turns==0:
            print("You ran out of guesses. You lose...")
            return
game()
