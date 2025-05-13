bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

def main():
    #  one liner bot :)
    print(f"My favorite animal is also {input(f"{bold_start}{italic_start} What's your favorite animal? {italic_end}{bold_end}")}! ")

if __name__ == '__main__':
    main()
