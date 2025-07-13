import os

def assign_bidders():
    name = input("What is your name? ")
    bid = int(input("Enter your bid $: "))
    return [name, bid]


def auction(bidders): 
    players = assign_bidders()
    bidders[players[0]] = players[1] 


def highest_bid(bidders):
    winning_bid = max(bidders.values())
    winners = [name for name in bidders if bidders[name] == winning_bid]
    if len(winners) == 1:
        return winners[0], winning_bid
    else:
        
        return [winners, winning_bid]
    


def main():
    bidders = {}
    while True:
        auction(bidders)
        game_on = input("Are there any more bidders? Type 'yes' or 'no'").lower()
        
        if game_on == "no":
            winner_name, winning_bid = highest_bid(bidders)

            if isinstance(winner_name, list):
                print(f"Tie! Winners: {', '.join(winner_name)} with ${winning_bid}")
            else:
                print(f"The highest bidder is {winner_name} with ${winning_bid}")
            break

        elif game_on == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Please enter a valid answer")



if __name__ == "__main__":
    main()
