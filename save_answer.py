import json
import os


def add_to_answer(task, answer_dict):
    """
    Добавление ответа на задание в файл с ответами.
    """
    filename = "answers.json"

    answers_data = {}
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            old_answers_data = json.load(f)
        answers_data.update(old_answers_data)

    answers_data[task] = answer_dict
    with open(filename, 'w') as f:
        json.dump(answers_data, f, indent=2)
