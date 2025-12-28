import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"

def main():
    user_score = 0
    computer_score = 0

    print("=== Rock Paper Scissors Game ===")

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue

        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "win":
            print("🎉 You win!")
            user_score += 1
        elif result == "lose":
            print("😢 You lose!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"\nScore → You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()