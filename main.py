"""
91883 Te Reo Quiz
v1.0 - Final Version
Damon Jones

Updates:
Original quiz plan removed from source file. All questions have been checked
for assurance. Quiz prints a number of newlines when restarted to prevent user
from seeing answers from previous quiz. Newlines are printed where it's useful
for readability. All inputs are tested for expected and unexpected cases (I
don't have any boundary cases as I haven't been working with inputs that would
have any). For safety reasons I also decided to move the questions dictionary
from the json file into the main source file as a constant. This is due to some
ide's treating the file's root directory differently and therefore causing
issues with loading files. I don't really need to worry about the convenience
of using a separate json file anymore so I'd rather the program is guaranteed
to work. This caused the load_questions() function to become deprecated.
"""


# Imports
import json
import random


# Constants
TITLE = """\
=======================
      Te Reo Quiz
=======================
""" #Text displayed for the quiz's title screen

QUIZ_INSTRUCTIONS = """\
Welcome to the Te Reo Maori language quiz!
You will be quizzed on the english translations to ten randomly
selected Maori words. Enter the correct translation and you get the
question correct. If you get it wrong, you'll receive the correct 
answer so you can learn it for the next try!
""" #Text displayed for the quiz's instructions

#Whitespace displayed between menu/restart prompt and the quiz
# Newlines are grouped in fives (30 newlines)
BEGINNING_OF_QUIZ_WHITESPACE = "\n\n\n\n\n \n\n\n\n\n \n\n\n\n\n \n\n\n\n\n \n\n\n\n\n \n\n\n\n\n"

QUESTIONS = [
    {
        "eng": "love",
        "mao": "aroha"
    },
    {
        "eng": "river",
        "mao": "awa"
    },
    {
        "eng": "food",
        "mao": "kai"
    },
    {
        "eng": "tribe",
        "mao": "iwi"
    },
    {
        "eng": "prayer",
        "mao": "karakia"
    },
    {
        "eng": "elder",
        "mao": "kaumatua"
    },
    {
        "eng": "walk",
        "mao": "hikoi"
    },
    {
        "eng": "mountain",
        "mao": "maunga"
    },
    {
        "eng": "sea",
        "mao": "moana"
    },
    {
        "eng": "island",
        "mao": "motu"
    },
    {
        "eng": "children",
        "mao": "tamariki"
    },
    {
        "eng": "lake",
        "mao": "roto"
    },
    {
        "eng": "family",
        "mao": "whanau"
    },
    {
        "eng": "hello",
        "mao": "kia ora"
    },
    {
        "eng": "welcome",
        "mao": "nau mai"
    },
    {
        "eng": "visitors",
        "mao": "manuhiri"
    },
    {
        "eng": "gift",
        "mao": "koha"
    },
    {
        "eng": "son",
        "mao": "tama"
    },
    {
        "eng": "daughter",
        "mao": "tamahine"
    },
    {
        "eng": "heart",
        "mao": "manawa"
    },
    {
        "eng": "relatives",
        "mao": "whanaunga"
    },
    {
        "eng": "canoe",
        "mao": "waka"
    },
    {
        "eng": "water",
        "mao": "wai"
    },
    {
        "eng": "small",
        "mao": "iti"
    },
    {
        "eng": "large",
        "mao": "nui"
    }
]


# Functions
def create_quiz(questions : list, size : int = 10) -> list:
    """Shuffles the list of questions and returns the amount that the quiz should have (ten generally).

    Args:
        questions (list): The pool of questions to select from for the quiz.
        size (int, optional): The size of the quiz. Defaults to 10.

    Returns:
        list: The list of questions to be used in the quiz.
    """
    random.shuffle(questions)
    quiz = questions[:size]
    return quiz


def check_translation(question : dict, english_input : str) -> bool:
    """Shorthand for checking the English input is the correct translation.

    Args:
        question (dict): The question containing the word/phrase.
        english_input (str): The translated input entered by the user.

    Returns:
        bool: Whether or not the English input was the correct translation.
    """
    return english_input == question["eng"]


def play_quiz(questions : list) -> int:
    """Plays through the quiz.

    Args:
        questions (list): List of questions in the quiz.

    Returns:
        int: Amount of questions gotten correctly.
    """
    questions_correct = 0
    count = 1

    # Iterate over every question in the test
    for question in questions:
        # Show user maori word and get the user's english translation
        print(f"Question {count}: {question['mao'].capitalize()}")
        user_input = input("Enter English Translation: ").lower()

        # Ensure user input is valid
        while not user_input.isalpha() and user_input != "":
            print("Please enter alphabetic characters only...")
            user_input = input("Enter English Translation: ").lower()
        print()

        # Check if question is correct
        correct = check_translation(question, user_input)
        if correct:
            questions_correct += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is {question['eng']}")
        print()
        count += 1
    
    return questions_correct


def restart_prompt() -> bool:
    """Gets user input for whether or not they want to play again.

    Returns:
        bool: Whether or not the player wants to play again.
    """
    # Ask user if they want to play again
    user_in = input("Would you like to play again? [Y/N] ").lower()
    while user_in not in ["y", "n"]:
        print("Please only enter 'y' or 'n'...")
        user_in = input("Would you like to play again? [Y/N] ").lower()
    
    if user_in == "y":
        return True
    return False


# Main Code
def main() -> None:
    """Function containing main code of program."""
    # Title Screen
    print(TITLE)
    input("Press enter to start...")
    print()


    # Instructions Screen
    print(QUIZ_INSTRUCTIONS)
    input("Press enter to continue...")
    print()
    

    # The actual quiz part
    playing = True
    while playing:
        # Print whitespace between previous quiz and now for readibility
        print(BEGINNING_OF_QUIZ_WHITESPACE)

        # Create a list of questions and play them
        quiz = create_quiz(QUESTIONS)
        questions_correct = play_quiz(quiz)
        
        # Print Results
        print(f"You got {questions_correct}/{len(quiz)} questions correct!")
        print("=======================")
        
        # If player chooses to continue playing, loop will continue.
        # Otherwise, loop closes and main() returns.
        playing = restart_prompt()

        print()


if __name__ == '__main__':
    main()