blue_start = '\033[34m'
blue_end = '\033[0m'


def main():
    lst = []
    while (val := input(f"{blue_start}Enter a value: {blue_end}")): lst.append(val)
    print("Here's the list:", lst)
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
