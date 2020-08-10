"""
91883 Te Reo Quiz
v0.1 - Boilerplate Code
Damon Jones
"""


# Imports
import json


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
def main():
    questions = load_questions()


if __name__ == '__main__':
    main()