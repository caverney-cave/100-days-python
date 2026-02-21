# * My Version

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')

bids = {}
should_continue = True

while should_continue:
    name = input("What's your name? ").capitalize()
    bid = int(input("What's your bid?: $"))

    bids[name] = bid
    other_bidder = input("Is there any other bidder? Type 'yes' or  'no': ").lower()

    winner = max(bids, key=bids.get)
    amount = bids[winner]

    if other_bidder in ['yes', 'y']:
        print("\n" * 100)
        continue
    else:
        should_continue = False

    print(f"The winner is {winner}, with a bid of: ${amount}")
