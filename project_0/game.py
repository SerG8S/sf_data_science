"Game guess the number"

import numpy as np
from numpy.random.mtrand import f

number = np.random.randint(1, 101)  # guess the number

count = 0  # number of attempts

while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100 "))
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must be larger!")
    else:
        print(f"You guessed the number! This number = {number}, in {count} attempts :0")
        break  # end of the game, exit from the cycle
