from game_data import data
from art import logo,vs
import random
print(logo)
a2=random.choice(data)
should_continue=True
while should_continue:
    a1=a2
    a2=random.choice(data)
    if a1==a2:
        a2=random.choice(data)
    def format_data(account):
        """convert the data to printable format"""
        name=account["name"]
        descr=account["description"]
        ctry=account["country"]
        return f"{name}, a {descr}, from {ctry}"

    def compare_answer(user_guess,f_a1,f_a2):
        if f_a1>f_a2:
            return  user_guess=="a"
        else:
            return user_guess=="b"


    print(f"Compare A: {format_data(a1)}.")
    print(vs)
    print(f"Against B: {format_data(a2)}.")

    user_guess=input("Who has more followers A or B ? ").lower()

    f_a1=a1["follower_count"]
    f_a2=a2["follower_count"]

    correct=compare_answer(user_guess,f_a1,f_a2)
    score = 0

    if correct:
        score+=1
        print(f"You are correct. Your current score is {score}")
    else:
        should_continue=False
        print(f"Oops that's wrong...Your final score is {score}")




