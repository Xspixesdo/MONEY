import random

MAX_BALANCE = 1000
MIN_BALANCE = 0.50
MAX_LINES = 3
MIN_LINES = 1

def amount():
    while True:
        try:
            get_amount = float(input(f"How much money would you like to play with? ({MIN_BALANCE}-{MAX_BALANCE}): "))
            if get_amount < MIN_BALANCE:
                print("You must enter at least 0.50 to play.")
            elif get_amount > MAX_BALANCE:
                print("You must enter less than 1000 to play.")
            else:
                print("You have entered: ", get_amount)
                return get_amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def lines():
    while True:
        try:
            get_lines = int(input(f"Enter the number of lines to bet on ({MIN_LINES}-{MAX_LINES}): "))
            if get_lines < MIN_LINES or get_lines > MAX_LINES:
                print("Enter a valid number of lines.")
            else:
                print("You have entered: ", get_lines)
                return get_lines
        except ValueError:
            print("Invalid input. Please enter a number.")

def bet(lines):
    while True:
        try:
            get_bet = float(input(f"What would you like to bet on each line? ({MIN_BALANCE}-{MAX_BALANCE}): "))
            if MIN_BALANCE <= get_bet <= MAX_BALANCE:
                total_bet = get_bet * lines
                print(f"Total bet is: {total_bet}")
                return total_bet
            else:
                print(f"Amount must be between ${MIN_BALANCE} - ${MAX_BALANCE}.")
        except ValueError:
            print("Please enter a number.")

def spin(balance, total_bet):
    while True:
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            break
        else:
            balance -= total_bet
            print(f"Your balance is now: ${balance}")

            for i in range(3):
                print(random.randint(1, 9), end=" ")
            print()
