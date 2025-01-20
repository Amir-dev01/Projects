import random

from decouple import config

def play_game():

    min_number = config("min_number", cast=int,default = 1)
    max_number = config("max_number", cast=int,default = 50)
    attempts = config("attempts", cast=int,default =5)
    initial_capital = config("initial_capital", cast=int,default = 100)

    target_number = random.randint(min_number, max_number)
    capital = initial_capital

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: от {min_number} до {max_number}")
    print(f"Количество попыток: {attempts}, начальный капитал: {capital}\n")

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt} из {attempts}. Ваш текущий капитал: {capital}")

        while True:
            try:
                bet = int(input("Введите вашу ставку: "))
                if bet <= 0 or bet > capital:
                    raise ValueError
                break
            except ValueError:
                print("Ставка должна быть положительным числом и не превышать ваш текущий капитал.")


        while True:
            try:
                guess = int(input(f"Угадайте число (от {min_number} до {max_number}): "))
                if guess < min_number or guess > max_number:
                    raise ValueError
                break
            except ValueError:
                print(f"Введите число в диапазоне от {min_number} до {max_number}.")


        if guess == target_number:
            capital += bet
            print(f"Поздравляем! Вы угадали число {target_number} и удвоили ставку!")
            print(f"Ваш текущий капитал: {capital}")
            break
        else:
            capital -= bet
            print(f"Неверно! Осталось {attempts - attempt} попыток.")
            if attempt == attempts:
                print(f"Вы проиграли! Загаданное число было: {target_number}")
                break


        if capital <= 0:
            print("Ваш капитал закончился. Игра окончена!")
            break

    print(f"Игра завершена. Ваш итоговый капитал: {capital}. Спасибо за игру!")
