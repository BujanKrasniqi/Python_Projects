import random

while True:
    print("Welcome to the Guess the Number game!")
    secret_number = random.randint(0, 100)

    while True:
        guess = input("Guess a number between 0 and 100: ")

        if guess == 'exit':
            print('Thanks for playing! Goodbye!')
            exit()
        elif not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
            print("Invalid input! Guess a number between 0 and 100.")
        elif int(guess) < secret_number:
            print("Your guess is too low. Try again!")
        elif int(guess) > secret_number:
            print("Your guess is too high. Try again!")
        else:
            play_again = input("You guessed correctly. Press Enter to play again. Type 'exit' to exit the program.")
            if play_again == 'exit':
                print('Thanks for playing! Goodbye!')
                exit()
            else:
                break
