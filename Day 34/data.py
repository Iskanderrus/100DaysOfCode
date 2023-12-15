# בס״ד

import html

import requests

from models import Question


def get_questions() -> list:
    """
    Function to get questions from the server using API,
    clean the encoding and convert questions into the Question classes
    :return: List of Question objects
    """
    url = 'https://opentdb.com/api.php?'

    parameters = {
        'amount': 10,
        'type': 'boolean'
    }

    response = requests.get(url=url, params=parameters)
    response.raise_for_status()

    questions = response.json()['results']
    # cleaning data
    for question in questions:
        question['question'] = html.unescape(question['question'])

    # creating list of Question objects
    questions_bank = [Question(question=question['question'],
                               correct_answer=question['correct_answer'])
                      for question in questions]

    return questions_bank
