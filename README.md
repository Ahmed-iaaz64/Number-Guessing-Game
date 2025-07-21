## Number Guessing Game

A command-line game built in Python where players guess a number between 1 and 100 with limited chances based on difficulty (Easy: 10, Medium: 5, Hard: 3). Built to meet [roadmap.sh](https://roadmap.sh/projects/number-guessing-game) project requirements.

## Features

- Random number generation (1-100).

- Three difficulty levels with varying chances.

- Input validation with clear feedback for invalid guesses.

- Logging for debugging invalid inputs.

## Requirements

- Python 3.10 or higher (for match statement support).

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

2. Navigate to the project directory:

```bash
cd number-guessing-game
```

## Usage

Run the game:

```bash
python number_guessing_game.py
```

- Select a difficulty level (1: Easy, 2: Medium, 3: Hard).

- Guess a number between 1 and 100 until you win or run out of chances.

## Example

```plain
We lcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:

1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You have chosen the Medium difficulty level.

Let's start the game!

Enter your guess: 50
Incorrect! The number is greater than 50
```

License

MIT License
