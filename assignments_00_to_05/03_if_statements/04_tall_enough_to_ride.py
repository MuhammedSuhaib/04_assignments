bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

MINIMUM_HEIGHT: int = 50  # arbitrary units :)


def main():
    print(f"You're tall enough to ride!" if float(input(f"{bold_start}{italic_start}How tall are you?{italic_end} {bold_end}")) >= MINIMUM_HEIGHT else "You're not tall enough to ride, but maybe next year!")

# There is no need to edit code beyond this point


if __name__ == '__main__':
    main()
