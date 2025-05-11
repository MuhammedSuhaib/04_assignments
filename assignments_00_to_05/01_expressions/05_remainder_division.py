def main():
    num1: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))  
    num2: int = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))  
    print(f"The result of this division is {num1 // num2} with a remainder of {num1 % num2}")
if __name__ == '__main__':
    main()