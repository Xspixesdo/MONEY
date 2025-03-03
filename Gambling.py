MAX_BET = 1000
MIN_BET = 0.50
MAX_LINES = 6
MIN_LINES = 1

symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
payouts = {
    "Cherry": 180,
    "Bell": 100,
    "Lemon": 90,
    "Orange": 60,
    "Star": 20,
    "Skull": 2,
}

def Lines():
    while True:
        get_lines = input("How many lines would you like to play? (1-6): ")
        if get_lines.isdigit():
            get_lines = int(get_lines)
            if 1 <= get_lines <= MAX_LINES:
                return get_lines
            elif get_lines < MIN_LINES:
                print("The minimum number of lines is 1")
            else:
                print("The maximum number of lines is 6")
        else:
            print("Please enter a valid number.")

def Bet():
    while True:
        get_bet = input("How much would you like to bet? $")
        try:
            get_bet = float(get_bet)
            if get_bet > MAX_BET:
                print("Your bet is too high. Max bet is $1000")
            elif get_bet < MIN_BET:
                print("Your bet is too low. Min bet is $0.50")
            else:
                return get_bet
        except ValueError:
            print("Please enter a valid number.")

def main():
    get_bet = Bet()
    get_lines = Lines()
    print(f"Total bet: ${get_bet * get_lines}")
    print("Good luck!")

if __name__ == "__main__":
    main()

