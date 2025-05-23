import random

choices: dict[str, str] = {"r": "rock", "p": "paper", "s": "scissors"}
user: str = input("Choose rock = r , paper = p 📃, or scissors = s ✂: ").lower()

if user not in choices:
    print("Invalid choice. Please Choose rock = r , paper = p 📃, or scissors = s ✂:.")
else:
    computer: str = random.choice(list(choices.values()))
    user_choice: str = choices[user]
    print(f"You: {user_choice} vs Computer: {computer}")

    if user_choice == computer:
        print("It's a tie!")
    elif (user_choice == "rock" and computer == "scissors") or \
        (user_choice == "paper" and computer == "rock") or \
        (user_choice == "scissors" and computer == "paper"):
        print("You win!🎉")
    else:
        print("You lose!😢")
