import math
def main():
    ab = float(input("\033[1m\033[3mEnter the length of AB:\033[0m "))
    ac = float(input("\033[1m\033[3mEnter the length of AC:\033[0m "))
    # Calculate the hypotenuse using the two sides and print it out
    print(f"The length of BC (the hypotenuse) is: {math.sqrt(ab**2 + ac**2)}")  
if __name__ == '__main__':
    main()
3