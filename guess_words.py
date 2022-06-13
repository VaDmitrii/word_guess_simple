from hw6_Dmitrii_Vasilevich.defs import shuffle_letters, get_word, save_results, get_record_result


def main():
    count_score = 0
    user_name = input("Введите Ваше имя: ")
    words: list[str] = get_word('words.txt')
    for word in words:
        shuffled_word: str = shuffle_letters(word)
        print(f"Угадайте слово: {shuffled_word}")
        user_answer = input()
        if user_answer == word:
            count_score += 10
            print("Верно! Вы получаете 10 очков.")
        else:
            print(f'Неверно! Верный ответ - {word}')
    save_results(filename='history.txt', user_name=user_name, count_score=count_score)
    games_result = get_record_result('history.txt')
    print(f'Всего сыграно игр: {games_result["count_games"]}')
    print(f'Максимальный рекорд: {games_result["record"]}')


if __name__ == '__main__':
    main()