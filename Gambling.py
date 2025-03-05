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
    for line in range(1, MAX_LINES + 1):
       while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on ({MIN_LINES}-{MAX_LINES}): "))
            if MIN_LINES <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between {MIN_LINES} and {MAX_LINES}.")
        except ValueError:
            print("Please enter a valid number.")
       
        break

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
            break

def balance(get_bet, total_wins):
   balance = (get_bet - total_wins)
   if balance > 0:
       return balance
    
  
                
          

def randomizer():
    return random.choice([True, False])

def wins():
    cherry = random.choice(range(101))
    bell = random.choice(range(81))
    lemon = random.choice(range(41))
    orange = random.choice(range(21))
    star = random.choice(range(11))
    skull = random.choice(range(16))
    total_wins = cherry + bell + lemon + orange + star + skull
    return total_wins

def game():
    get_bet = Bet() 
    while True:
        get_lines = Lines()
        total_bet = get_bet * get_lines
        
        print(f"Total bet: ${total_bet}")
        print("Good luck!")
        print("Spinning...")
        total_wins = wins()
        print(f"Total wins: {total_wins}")
        
        if total_wins > 0.5:
            print("Congratulations! You won!")
            payout = get_bet * Input_List_payouts[symbols[total_wins % len(symbols)]] * get_lines
            print(f"Total payout: ${payout}")
           
        continue
        balance = get_bet - total_wins
        print(f"Balance: ${get_bet-total_wins}")
           
        
    
       

def main():

    

 if __name__ == "__main__":
    game()
