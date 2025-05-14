blue_start = '\033[34m'
blue_end = '\033[0m'


def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total = sum(fruits[f] * int(input(f"{blue_start}How many ({f}) do you want to buy?: {blue_end}")) for f in fruits)
    print(f"Your total is ${total}")

if __name__ == '__main__':
    main()
