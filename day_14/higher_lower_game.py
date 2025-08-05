from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user guess and the follower count and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0

game_continues = True

while game_continues:
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_b == account_b:
        account_b = random.choice(data)

    print(f"\nCompare A: {format_data(account_a)}")

    print(vs)

    print(f"Compare B: {format_data(account_b)}")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score is: {score}")
    else:
        print(f"Sorry, you're wrong. Final score: {score}")
        game_continues = False
