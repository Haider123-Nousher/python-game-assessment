# I acknowledge the use of ChatGPT (OpenAI) to assist in creating this code.

import random


def get_player_name():
    """Prompt the player for their name."""
    name = input("What is your name? ").strip()
    return name if name else "Player"


def ask_for_guess():
    """Prompt the player for a valid guess between 1 and 100."""
    while True:
        guess_text = input("Enter your guess (1–100): ").strip()

        if not guess_text:
            print("Please enter a number.")
            continue

        if not guess_text.isdigit():
            print("Invalid input. Please enter a whole number.")
            continue

        guess = int(guess_text)

        if 1 <= guess <= 100:
            return guess
        else:
            print("Number must be between 1 and 100.")


def play_round(secret_number, max_attempts=10):
    """
    Play one round of the game.
    Returns True if the player wins, otherwise False.
    """
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        guess = ask_for_guess()

        if guess == secret_number:
            print("Correct! You guessed the number.")
            return True
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    print("\nOut of attempts.")
    print(f"The secret number was: {secret_number}")
    return False


def want_to_play_again():
    """Ask the player if they want to play again."""
    while True:
        answer = input("\nDo you want to play again? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")


def display_summary(player_name, total_games, games_won):
    """Display final game statistics."""
    print("\n==============================")
    print("        GAME SUMMARY")
    print("==============================")
    print(f"Player: {player_name}")
    print(f"Games Played: {total_games}")
    print(f"Games Won: {games_won}")
    print("Thanks for playing. Goodbye.")


def main():
    """Main game function."""
    print("\n==============================")
    print("     NUMBER GUESSING GAME     ")
    print("==============================\n")

    player_name = get_player_name()

    total_games = 0
    games_won = 0

    print(f"\nHello, {player_name}. I am thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly.\n")

    while True:
        secret_number = random.randint(1, 100)

        if play_round(secret_number):
            games_won += 1
            print(f"Well done, {player_name}.")
        else:
            print(f"Good attempt, {player_name}. Try again next time.")

        total_games += 1

        if not want_to_play_again():
            display_summary(player_name, total_games, games_won)
            break


if __name__ == "__main__":
    main()