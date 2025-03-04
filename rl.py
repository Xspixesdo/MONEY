import random

def randomizer():
    while True:
      try:
        user_input = input("Enter the maximum range (integer) or comma-separated options: ")
        if user_input.isdigit():
            max_range = int(user_input)
            result = random.randint(1, max_range)
            print(f"Random number between 1 and {max_range}: {result}")
            break
        elif "," in user_input:
            options = [option.strip() for option in user_input.split(",")]
            result = random.choice(options)
            print(f"Randomly selected option: {result}")
            break
        else:
            print("Invalid input. Please enter an integer or comma-separated options.")
      except ValueError:
          print("Invalid input. Please enter an integer or comma-separated options.")

randomizer()
