import random
def main():
    guess_count = 0
    secret = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess"))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        guess_count += 1
        if guess == secret:
            break
        print("Your guess is too low" if guess < secret else "Your guess is too high")

    print(f"Congrats! The number was: {secret}")
    print(f"it took you {guess_count} guesses")

if __name__ == '__main__':
    main()
