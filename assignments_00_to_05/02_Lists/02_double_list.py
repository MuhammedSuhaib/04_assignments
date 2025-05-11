def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers
    print(numbers)  # Prints the list of numbers
    new_list = [num + num for num in numbers] #List Comprehension
    print(new_list)
if __name__ == '__main__':
    main()
