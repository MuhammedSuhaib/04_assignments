blue_start = '\033[34m'
blue_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'
cyan_start = '\033[96m'
cyan_end = '\033[0m'
green_start = '\033[92m'
green_end = '\033[0m'

def main():
    low, high = 1, 99
    guess_count = 0

    print(f"{cyan_start}{'⋰⋱' * 70}")
    print(f" \t \t \t \t Welcome to the Guess the Number Game!")
    print('⋱⋰' * 70)
    print(f"\t \t  Think of a number between 1 and 99, and I will try to guess it! \n \n {cyan_end}")

    while True:
        guess = (low + high) // 2
        guess_count += 1
        response = input(
            f"Is your number {guess}? (h = too high, l = too low, c = correct)").lower()

        if response == 'c':
            print(f"{green_start} \t \t  Yay! I guessed it in {guess_count} tries.{green_end}")
            break
        elif response == 'h':
            if guess == low:
                print(f"{red_start}Hmm, can't go lower than this!{red_end}")
            else:
                high = guess - 1
        elif response == 'l':
            if guess == high:
                print(f"{red_start}Hmm, can't go higher than this!{red_end}")
            else:
                low = guess + 1
        else:
            print(f"{red_start}Invalid input, please enter h, l, or c.{red_end}")

if __name__ == '__main__':
    main()
