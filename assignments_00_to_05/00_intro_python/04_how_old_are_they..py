def main():
    anton: int = 21  # Anton's age is given as 21 years old
    # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    beth: int = 6 + anton
    # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    chen: int = 20 + beth
    # Drew is as old as Chen's age plus Anton's age, so add them together
    drew: int = chen + anton
    ethan: int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # Print out all of the ages!
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
