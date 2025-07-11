print("Welcome to the secret Auction Program.")

bids = {}

continue_auction = "yes"

while continue_auction == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    continue_auction = input(
        "Are there any other bidders? Type 'yes' or 'no': ")
    print("\n" * 100)

print(
    f"The winner is {max(bids, key=bids.get)} with a bid of ${bids[max(bids, key=bids.get)]}")
