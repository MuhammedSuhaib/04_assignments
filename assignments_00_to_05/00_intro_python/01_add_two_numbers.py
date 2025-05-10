def main():
    """
    Program: add2numbers
    --------------------
    This program asks the user for two
    integers and prints their sum.
    """
    print("This program adds two numbers.")
    num1 : int = int(input("Enter first number: "))
    num2 : int = int(input("Enter second number: "))
    total: int = num1 + num2
    print(f'The total is {total} .')
if __name__ == '__main__':
    main()
