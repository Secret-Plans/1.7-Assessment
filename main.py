"""
91883 Te Reo Quiz
v0.1 - Boilerplate Code
Damon Jones

Updates:
Just implemented the basics required for the test to work and some debug stuff
to help me later. This includes a function that loads the test questions in
from a json file. I'm choosing to use a json file as I find it's easier to
navigate and edit than having it as a constant dictionary in the main file. All
questions for the test have been added at this point (25), unless more are
added down the line, which likely won't be necessary. Status messages will be
removed for the final version. For the sake of debugging, the program runs in a
loop that creates a quiz of ten randomly selected questions and prints them out
every time the user presses enter.
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
DEBUG_TOOLS_ON = True


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


def check_translation(question : dict, english_input : str) -> bool:
    """Shorthand for checking the English input is the correct translation.

    Args:
        question (dict): The question containing the word/phrase.
        english_input (str): The translated input entered by the user.

    Returns:
        bool: Whether or not the English input was the correct translation.
    """
    return english_input == question["eng"]


# Main Code
def main() -> int:
    """Function containing main code of program.

    See C, C++, C#, Java etc. This function is the beginning of the program's
    execution. It also returns status messages based on what caused the end of
    the program's execution. See bottom of this file for the list of status
    messages.

    Returns:
        int: A status message representing what caused the program to end
        execution.
    """
    # File Loading
    try:
        questions = load_questions()
    except:
        print("Fatal error! Questions could not be loaded")
        input("Press enter to continue...")
        return
    
    
    playing = True
    while playing:
        # Shuffle the questions into a random order and selects the top ten.
        random.shuffle(questions)
        quiz = questions[:10]
        questions_correct = 0
        responses = []


        # Start Quiz
        for question in quiz:
            # Show user maori word and get the user's english translation
            print(question["mao"])
            user_input = input("Enter English Translation: ").lower()
            while not user_input.isalpha() and user_input != "":
                print("Please enter alphabetic characters only...")
                user_input = input("Enter English Translation: ").lower()
            print()

            # Add user input to list to display stats later
            responses.append(user_input)

            # Check if question is correct
            correct = check_translation(question, user_input)
            if correct:
                questions_correct += 1
                print("Correct!")
            else:
                print("Incorrect!")
                print(f"The correct answer is {question['eng']}")
            print()
        
        # Print Results
        print(f"You got {questions_correct}/10 questions correct!")
        
        input("Press Enter to Continue...")


if __name__ == '__main__':
    main()