import random



def number_guessing_game():
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("welcome to the number guessing game.")
    print(f"i am thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        player_guess = int(input("Enter a number."))
        attempts +=1

        if player_guess < target_number:
            print("Too low, Try again.")
        elif player_guess > target_number:
            print("Too high, Try again")
        else:
            print(f"congratulation! you guessed the number {target_number} in {attempts} attempts")



number_guessing_game()