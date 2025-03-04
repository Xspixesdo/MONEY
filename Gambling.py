import random

MAX_BET = 1000
MIN_BET = 0.50
MAX_LINES = 6
MIN_LINES = 1

symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
Input_List_payouts = {
    "Cherry": 180,
    "Bell": 100,
    "Lemon": 90,
    "Orange": 60,
    "Star": 20,
    "Skull": 2,
}

def Lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on ({MIN_LINES}-{MAX_LINES}): "))
            if MIN_LINES <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between {MIN_LINES} and {MAX_LINES}.")
        except ValueError:
            print("Please enter a valid number.")

def Bet():
    while True:
        try:
            bet = float(input(f"Enter your bet amount ({MIN_BET}-{MAX_BET}):$ "))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Please enter an amount between {MIN_BET} and {MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")

def randomizer():
    return random.choice([True, False])

def wins():
    cherry = random.choice(range(101))
    bell = random.choice(range(81))
    lemon = random.choice(range(41))
    orange = random.choice(range(21))
    star = random.choice(range(11))
    skull = random.choice(range(16))
    print(f"wins: {cherry} {bell} {lemon} {orange} {star} {skull}")

def main():
    get_bet = Bet()
    get_lines = Lines()
    total_bet = get_bet * get_lines
    print(f"Total bet: ${total_bet}")
    print("Good luck!")
    print("Spinning...")
    print({wins()})
    

    if randomizer():
        wins()

if __name__ == "__main__":
    main()
