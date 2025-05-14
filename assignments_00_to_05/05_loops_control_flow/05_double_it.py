blue_start = '\033[34m'
blue_end = '\033[0m'
red_start = '\033[91m'
red_end = '\033[0m'
try:
    curr_value = int(input(f"{blue_start}Enter a number: {blue_end}"))
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)
except ValueError:
    print(f"{red_start}Error: Please enter a valid integer.{red_end}")
    