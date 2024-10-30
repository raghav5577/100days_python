data={}
def find_highest_bid():
    winner=""
    highest_bid=0
    for bidder in data:
        bid_amount=data[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print(f"The winner is {winner}with bid amount of ${highest_bid}")
continue_bid=True
while continue_bid :
    name = input("What is your name ?: ")
    bid = int(input("What is your bid ?: "))
    data[name] = bid
    should_continue = input("Are there any other bidders ? Type yes or no.\n").lower()
    if should_continue=="no":
        continue_bid=False
        find_highest_bid()
    elif should_continue=="yes":
        print("\n"*1000)



