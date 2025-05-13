
bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

def add_three_copies(my_list, data):
    my_list.extend([data] * 3) #The `extend()` method in Python takes **1 parameter**: an iterable (like a list, tuple, or string). It appends each element of the iterable to the list.


########## No need to edit code past this point

def main():
    message = input(f"{bold_start}{italic_start}Enter a message to copy: {italic_end}{bold_end}")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()