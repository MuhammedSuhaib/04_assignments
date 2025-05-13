bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'


def main():
    num1: int = int(input(
        f"{bold_start}{italic_start}Please enter an integer to be divided:{italic_end}{bold_end} "))
    num2: int = int(input(
        f"{bold_start}{italic_start}Please enter an integer to divide by:{italic_end}{bold_end} "))
    print(
        f"The result of this division is {num1 // num2} with a remainder of {num1 % num2}")


if __name__ == '__main__':
    main()
