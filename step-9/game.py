# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bigger in bidding_dictionary:
        big_amount = bidding_dictionary[bigger]
        if big_amount > highest_bid:
            highest_bid = big_amount
            winner = bigger

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no' \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)


