bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

def main():
    num: float = float(input(f"{bold_start}{italic_start} Type a number to see its square: {italic_end}{bold_end}")) 
    print(f"{num} squared is {num**2}")
if __name__ == '__main__':
    main()
