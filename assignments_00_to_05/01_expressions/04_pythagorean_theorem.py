import math
bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

def main():
    ab = float(input(f"{bold_start}{italic_start}Enter the length of AB:{italic_end}{bold_end}"))
    ac = float(input(f"{bold_start}{italic_start}Enter the length of AC:{italic_end}{bold_end}"))
    # Calculate the hypotenuse using the two sides and print it out
    print(f"The length of BC (the hypotenuse) is: {math.sqrt(ab**2 + ac**2)}")  
if __name__ == '__main__':
    main()
3