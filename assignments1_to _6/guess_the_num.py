blue_start = '\033[34m'
blue_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'


import random
def main():
    guess_count: int = 0
    secret : int = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess: int = int(input(f"{blue_start}Enter a guess{blue_end}"))
        except ValueError:
            print(f"{red_start}Invalid input. Enter a number.{red_end}")
            continue

        guess_count += 1
        if guess == secret:
            break
        print("Your guess is too low" if guess < secret else "Your guess is too high")

    print(f"Congrats! The number was: {secret}")
    print(f"it took you {guess_count} guesses")

if __name__ == '__main__':
    main()
