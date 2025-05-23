import random
import string

# list of words
words: list[str] = ['python', 'javascript', 'typescript', 'html', 'css']
word: str = random.choice(words)
guessed: list[str] = []
lives: int = 6

print('Welcome to Hangman!')
print('Available words:', words)

# game loop
while lives > 0:
    display: list[str] = []
    for letter in word:
        if letter in guessed:
            display.append(letter)
        else:
            display.append('_')
    print('Word:', ' '.join(display))
    print('Lives:', lives)

    guess: str = input('Guess a letter: ').lower()

    if guess in string.ascii_lowercase and guess not in guessed:
        guessed.append(guess)
        if guess not in word:
            lives -= 1
            print('Wrong guess.')
    elif guess in guessed:
        print('You already guessed that.')
    else:
        print('Invalid input.')

    # win check
    win = True
    for letter in word:
        if letter not in guessed:
            win = False
            break
    if win:
        print('You won! The word was:', word)
        break

if lives == 0:
    print('You lost. The word was:', word)
