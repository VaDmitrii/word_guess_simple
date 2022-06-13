import random


def get_word(filename: str) -> list[str]:
    """ Получает список слов из файла words.txt"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def shuffle_letters(word: str) -> str:
    """ Получает слово из функции get_word()
    Перемешивает буквы и отправляет слово в цикл"""
    letters_list = list(word)
    random.shuffle(letters_list)
    return ''.join(letters_list)


def save_results(filename: str, user_name: str, count_score: int) -> None:
    """ Запоминает результаты игры и записывает их в history.txt"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{user_name} {count_score}\n')


def get_record_result(filename: str) -> dict:
    """ Вычисляет общее количество игр и
    лучший результат и возвращает их"""
    with open(filename, 'r', encoding='utf-8') as file:
        record = file.read().splitlines()
    count_games = 0
    record_result = 0
    for result in record:
        user_name, score = result.split()
        score = int(score)
        if record_result < score:
            record_result = score
        count_games += 1
    return {'count_games': count_games, 'record': record_result}



