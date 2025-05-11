import random
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    roll1: int = random.randint(1, NUM_SIDES)
    roll2: int = random.randint(1, NUM_SIDES)
    total: int = roll1 + roll2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print(f"die1 in main() starts as: {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is: {die1}")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()