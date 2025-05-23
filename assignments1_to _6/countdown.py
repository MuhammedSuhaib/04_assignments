import time
user_input: int = input("Enter a number: ")
if user_input.isdigit():
    for i in range(int(user_input), -1, -1):
        print(i , end='\r')
        time.sleep(1)
    print("Done!")
else:
    print("Please enter a valid number.")