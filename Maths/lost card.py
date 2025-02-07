
def find(n, cards):
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(cards)
    lost_card = expected_sum - actual_sum
    return lost_card

amount = int(input("Enter the number of cards: "))
cards = list(map(int, input("Enter the card numbers: ").split()))

lost_card = find(amount+1, cards)
print("The lost card is:", lost_card)