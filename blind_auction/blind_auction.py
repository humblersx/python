
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

keep_going = "yes"
bidders = {}

while keep_going == "yes":
    name = input("What is your name?: ")
    price = input("What is your bid?: ")



    bidders[name] = price


    keep_going = input("Type 'yes' to continue adding bids or else type 'no'.: ").lower()
    print("\n" * 20)


top_bid = 0
top_bidder = ""

for each in bidders:
    if int(bidders[each]) > top_bid:
        top_bid = int(bidders[each])
        top_bidder = each

print(f"The winner is {top_bidder} with a bid of ${top_bid}.")


