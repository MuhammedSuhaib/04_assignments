blue_start = '\033[34m'
blue_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'
AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    while input(f"{blue_start}Please type the following affirmation: {AFFIRMATION}{blue_end}\n") != AFFIRMATION:
        print(f"{red_start}That was not the affirmation.{red_end}")
    print("That's right! :)")

if __name__ == '__main__':
    main()
