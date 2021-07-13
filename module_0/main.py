import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать скорость работы'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_3(number):
    '''Решим задачу бинарным поиском'''
    count = 1
    '''Задаем левую и правую границы'''
    left = 1
    right = 100
    predict = (left + right) // 2
    while number != predict:
        count += 1
        if number > predict:
            # Если нужно число больше предсказанного, нет смысла смотреть числа слева
            left = predict + 1
        elif number < predict:
            right = predict - 1
        predict = (left + right) // 2
    return (count)


if __name__ == '__main__':
    score_game(game_core_3)



