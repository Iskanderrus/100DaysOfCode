# בס״ד

import requests


def get_questions() -> list:
    """
    Function to get questions from the server using API
    :return: List of dictionaries
    """
    url = 'https://opentdb.com/api.php?'

    parameters = {
        'amount': 10,
        'type': 'boolean'
    }

    response = requests.get(url=url, params=parameters)
    response.raise_for_status()

    questions = response.json()['results']
    for question in questions:
        question['question'] = question['question'].replace('&quot;', '"')
        question['question'] = question['question'].replace('&#039;', '\'')
    return questions
