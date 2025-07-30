import random

logo = """
  ____  _            _      _            _    
 |  _ \| |          | |    (_)          | |   
 | |_) | | __ _  ___| | __  _  ___  __ _| | __
 |  _ <| |/ _` |/ __| |/ / | |/ _ \/ _` | |/ /
 | |_) | | (_| | (__|   < _| |  __/ (_| |   < 
 |____/|_|\__,_|\___|_|\_(_)_|\___|\__,_|_|\_\ 

         ♠ ♣ ♢ ♡   BLACKJACK   ♠ ♣ ♢ ♡
        ==============================
"""


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Player lost, computer has a Black Jack!"
    elif u_score == 0:
        return "Player won with a Black Jack!"
    elif u_score > 21:
        return "Player lost. Player went over. Computer wins!"
    elif c_score > 21:
        return "Player won! Computer went over"
    elif u_score > c_score:
        return "Player won!"
    else:
        return "Player lost. Computer won."


def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("=======================================")
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Comp 1st card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("=======================================")
    print(compare(user_score, computer_score))
    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Comp cards: {computer_cards}, comp score: {computer_score}")
    print("=======================================")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print(logo)
    play_game()
