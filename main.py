import random

dealer_cards = []
player_cards = []

# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(2, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X and", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(2, 11))
    if len(player_cards) == 2:
        print("You have", player_cards)
        print("Sum:", sum(player_cards))

# Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer have 21. Dealer wins!")
elif sum(dealer_cards) > 21:
    print("The dealer took more. Dealer lose!")

# Sum of the Player cards
if sum(player_cards) == 21:
    print("You have 21. You win!")
elif sum(player_cards) > 21:
    print("You took more than 21. You lose!")
while sum(player_cards) < 21:
    print("Stay or hit:")
    mes = str(input())
    if mes == 'hit':
        player_cards.append(random.randint(1, 11))
        print("The dealer has:", dealer_cards, "And sum:", sum(dealer_cards))
        print("You have:", player_cards, "And sum:", sum(player_cards))
        if sum(player_cards) > 21:
            print("You lose!")
    else:
        print("The dealer has:", dealer_cards, "And sum:", sum(dealer_cards))
        print("You have:", player_cards, "And sum:", sum(player_cards))
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer win!")
        elif sum(dealer_cards) == sum(player_cards):
            print("Draw!")
        else:
            print("You win!")
