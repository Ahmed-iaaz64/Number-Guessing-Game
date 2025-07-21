import random
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_integer_between_range(prompt, start, end):
    """Get an integer from the user between a range.
    
    Args:
        prompt (str): Input prompt given to the user.
        start (int): Start range for integer (inclusive)
        end (int): End range for integer (inclusive)

    Returns:
        int: The validated integer.

    Raises:
        None: Loops until valid input is provided.
    """
    valid = False
    
    while not valid:
        integer = input(prompt).strip()

        # Validate input
        try:
            integer = int(integer)
        except ValueError:
            logging.warning("Input must be an integer. Try again.\n")
            continue

        if integer < start or integer > end:
            logging.warning(f"Invalid choice. Input must be between {str(start)} and {str(end)}. Try again.\n")  
            continue
        
        valid = True
    
    return integer
    

def select_difficulty():
    """Ask user to select the difficulty level and returns chance based on difficulty.
    
    Returns:
        int: Chances based on difficulty level.
    """

    print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")


    difficulty = get_integer_between_range("Enter your choice: ", 1, 3)

    match difficulty:
        case 1:
            print("Great! You have chosen the Easy difficulty level.\n")
            return 10
        case 2:
            print("Great! You have chosen the Medium difficulty level\n.")
            return 5
        case 3:
            print("Great! You have chosen the Hard difficulty level.\n")
            return 3


def compare_choices(computer_choice, user_choice):
    """Compare two integers and tell the user if they are above or below the correct choice.
    
    Args:
        computer_choice(int): The choice that has to be matched to.
        user_choice(int): The choice that is compared against the one to match.

    Returns:
        boolean: True if the two choices match else False
    """

    if computer_choice == user_choice:
        return True
    elif computer_choice > user_choice:
        print(f"Incorrect! The number is greater than {str(user_choice)}\n")
        return False
    elif computer_choice < user_choice:
        print(f"Incorrect! The number is less than {str(user_choice)}\n")
        return False


def main():
    """Handle the main game loop and checks win or lose conditions."""

    # welcome message
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n""")

    # Get the total guesses based on difficulty
    total_guesses = select_difficulty()
    times_guessed = 0
    computer_choice = random.randint(1, 100)
    won = False

    print("Let's start the game!\n")

    # Main game loop
    while not won:

        user_guess = get_integer_between_range("Enter your guess: ", 1, 100)

        won = compare_choices(computer_choice, user_guess)

        # Check win or lose conditions
        if not won:
            times_guessed += 1
        else:
            print(f"Congratulations! You guessed the right number in {str(times_guessed)} attempts.\n")

        if times_guessed >= total_guesses:
            print(f"You failed! The right number was {str(computer_choice)}\n")
            break


if __name__ == "__main__":
    main()