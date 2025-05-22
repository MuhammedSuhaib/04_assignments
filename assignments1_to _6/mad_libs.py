SENTENCE_START: str = "Out of nowhere"

bold_start = '\033[1m'
bold_end = '\033[0m'
italic_start = '\033[3m'
italic_end = '\033[0m'

def main():
    # Get the three inputs from the user
    adjective: str = input(f"{bold_start}{italic_start}Please type an adjective and press enter.{italic_end}{bold_end}")
    noun: str = input(f"{bold_start}{italic_start}Please type a noun and press enter.{italic_end}{bold_end}")
    verb: str = input(f"{bold_start}{italic_start}Please type a verb and press enter.{italic_end}{bold_end}")

    print(f'{SENTENCE_START} the  {adjective} {noun} {verb}!')

if __name__ == '__main__':
    main()
