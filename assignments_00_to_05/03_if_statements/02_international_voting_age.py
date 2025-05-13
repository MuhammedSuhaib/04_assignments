def main():

    voting_ages = {"Peturksbouipo": 16, "Stanlau": 25, "Mayengua": 48}
    user_age = int(input("How old are you? "))

    for country, age in voting_ages.items():
        print(f"You {'can' if user_age >= age else 'cannot'} vote in {country} where the voting age is {age}.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
