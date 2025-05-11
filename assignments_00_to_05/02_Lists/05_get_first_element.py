def get_first_element(lst):
    """
    Prints the first element of the provided list.
    If the list is empty, raises a ValueError.
    """
    try:
        print(lst.pop(0))  # Print the first element of the list
    except IndexError:
        print("Error: The list is empty.")

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "": # while element is not empty
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()
