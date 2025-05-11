def add_many_numbers(numbers)-> int:
    sum(numbers)  # Find the sum of the list
    return sum(numbers)  # Return the sum of the list
# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()