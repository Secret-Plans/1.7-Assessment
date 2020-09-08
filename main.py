"""
91883 Te Reo Quiz
v0.3 - Adding a Title Screen and Polishing
Damon Jones

Updates:
Added a title screen, some instructions for the quiz displayed at the beginning
and a restart screen at the end, prompting the user if they want to play again.
Also just worked on some polishing, such as capitalizing questions, adding
question numbers and making things more readable overall. I fixed a duplicate
question that was present before too.
"""


# The Plan
"""
Maori word is presented and the English translation must be entered by the user
to get the question right. I'd like to shuffle the list of questions. My end
goal is to have twenty-five questions, with one quiz being ten questions long.
The user will receive a grade of how well they did (x/10 marks) afterwards.
Questions will probably be read from a json file to make them easier to edit.

If a user gets a question wrong, they should receive some feedback to their
answer. Probably just something along the lines of 'Wrong. Correct Answer is:'
and then say the correct answer so they can learn for next time.
"""


# Imports
import json
import random


# Constants
TITLE = """\
=======================
      Te Reo Quiz
=======================
"""

QUIZ_INSTRUCTIONS = """\
Welcome to the Te Reo Maori language quiz!
You will be quizzed on the english translations to ten randomly
selected Maori words. Enter the correct translation and you get the
question correct. If you get it wrong, you'll receive the correct 
answer so you can learn it for the next try!
"""


# Functions
def load_questions() -> list:
    """Loads list of questions from json file.

    The list is filled with questions, which are stored in the format of a
    dictionary with an English and Maori word/phrase of the same meaning.

    Returns:
        list: List of questions.
    """
    questions_dict = {}
    with open("questions.json", "r") as f:
        questions_dict = json.load(f)
    return questions_dict["questions"]


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
    # Load list of questions
    try:
        questions = load_questions()
    except:
        print("Fatal error! Questions could not be loaded")
        input("Press enter to continue...")
        return

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
        # Create a list of questions and play them
        quiz = create_quiz(questions)
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