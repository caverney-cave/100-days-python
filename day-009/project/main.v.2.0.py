# * Tutor Version
# ** little modification

from art import logo

print(logo)

continue_bidding = True


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner}, with a bid of: ${highest_bid}")


while continue_bidding:
    name = input("What's your name? ").capitalize()
    bid = int(input("What's your bid?: $"))
    bids = {name: bid}
    should_continue = input("Is there any other bidder? Type 'yes' or  'no': ").lower()
    if should_continue not in ["yes", "y"]:
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)
        continue
