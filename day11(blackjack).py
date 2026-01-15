import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Takes a list of cards and returns the score."""
    # Blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace (11) to 1 if score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Compares user and computer scores."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Game loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
