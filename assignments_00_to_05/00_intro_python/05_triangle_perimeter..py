bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'


def main():
    '''This program calculates the perimeter of a triangle.'''
    print("*"*70)
    print("\t \t This program calculates the perimeter of a triangle.")
    print("*"*70)
    print(' \t \t Perimeter of the triangle means the sum of all of the side lengths.')
    print("-"*70)
    side1: float = float(input(
        f"{bold_start}{italic_start} What is the length of side 1? {italic_end}{bold_end}"))
    side2: float = float(input(
        f"{bold_start}{italic_start} What is the length of side 2? {italic_end}{bold_end}"))
    side3: float = float(input(
        f"{bold_start}{italic_start} What is the length of side 3? {italic_end}{bold_end}"))
    sum_of_sides: float = side1 + side2 + side3
    # print(type(sum_of_sides))
    tri = str(sum_of_sides)
    # print(type(tri))
    print(f"The perimeter of the triangle is {tri}")


if __name__ == '__main__':
    main()
