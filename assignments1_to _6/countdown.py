import time
user_input: int = input("Enter a number: ")
if user_input.isdigit():
    # it was giving error 
    # SyntaxError: did you forget parentheses around the comprehension target?   
    #  so i added ()
    [(time.sleep(1) , print(i, end='\r') ) for i in range(int(user_input), 0, -1)]
    print("Done!")
else:
    print("Please enter a valid number.")
