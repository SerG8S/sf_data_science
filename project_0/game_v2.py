"Automation of the game 'Guess the number'"

import numpy as np


def random_predict(number: int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    count = 0  #  counter number of attempts

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  #  estimated number
        if number == predict_number:
            break  #  end of the cycle if it guess
        elif count >= 20:  #  condition no more than 20 attempts
            break
    return(count)


def score_game(random_predict) -> int:
    """For how many attempts, on average, per 1000 approaches, our algorithm guesses

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []  #  list to save the number of attempts
    np.random.seed(1)  #  fix the value for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  #  made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  #  find the average number of attempts
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(random_predict)
