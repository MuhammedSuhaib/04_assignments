def main():
    year = int(input('Please input a year: '))
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print("That's a leap year!" if is_leap else "That's not a leap year.")
if __name__ == '__main__':
    main()
