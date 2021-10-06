"Game guess the number"

import numpy as np
from numpy.random.mtrand import f

number = np.random.randint(1, 101)  # guess the number

count = 0  # number of attempts

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: "))
    if predict_number > number:
        print("Число должно быть меньше!")
    elif predict_number < number:
        print("Число должно быть больше!")
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break  # end of the game, exit from the cycle
