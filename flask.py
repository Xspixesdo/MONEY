# filepath: /Users/jaysonasuncion/Money/MONEY-3/app.py
from flask import Flask, render_template, request # type: ignore
from Gambling import amount, lines, bet, spin

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Slot-machine.html')

@app.route('/play', methods=['POST'])
def play():
    # Example: Simulate a game using Gambling.py functions
    balance = 100  # Example starting balance
    total_bet = 10  # Example bet amount
    spin_result = spin(balance, total_bet)  # Call the spin function

    # Pass the result to the HTML
    return render_template('Slot-machine.html', result=spin_result)

if __name__ == '__main__':
    app.run(debug=True)
