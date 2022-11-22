import random
import time
def bet(b, g):
    print('Пожалуйста подождите...')
    time.sleep(2)
    choise = random.randint(1, 31)
    if choise == b:
        print(choise)
        print('поздравляю вы выиграли!')
        return g * 2

    else:
        print(choise)
        print(f'-{g}$')

        return 0