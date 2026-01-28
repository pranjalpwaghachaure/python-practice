import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("👋 Thanks for playing!")
            break

main()
