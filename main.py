VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    sum = 0
    for card in hand:
        if card in VALID_CARDS:
            if card == 'Jack' or card == 'Queen' or card == 'King': 
                card = 10
                sum += card
            
            elif card == 'Ace' and sum > 11:
                card = 1
                sum += card

            elif card == 'Ace':
                card = 11
                sum += card

            else:
                sum += card

            
    return sum


