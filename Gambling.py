MAX_BET = 1000
MIN_BET = 0.50
MAX_LINES = 6

def Bet():
    while True:
        get_bet = input("How much would you like to bet? $")
        if get_bet.isdigit():
            get_bet = int(get_bet)
            if get_bet > MAX_BET:
                print("Your bet is too high. Max bet is $1000")
            elif get_bet < MIN_BET:
                print("Your bet is too low. Min bet is $0.50")
            else:
                return get_bet
        else:
            print("Please enter a valid number.")



Bet()


