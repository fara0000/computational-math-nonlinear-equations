import math
from Equation import Equation
from methods.NewtonsMethod import NewtonsMethod
from methods.SimpleIterationsMethod import SimpleIterationsMethod

import ConsoleFunctionality

methods = {
    2: NewtonsMethod,
    3: SimpleIterationsMethod
}

predefined_functions = {
    1: Equation(lambda x: (x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38), 'x ^ 3 + 4.81 * x ^ 2 - 17.37 * x + 5.38'),
    2: Equation(lambda x: (math.sin(x) + 0.7 - math.cos(x) ** 2), 'sin(x) + 0.7 - cos(x) ^ 2'),
    3: Equation(lambda x: (x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76), 'x ^ 3 - 1.89 * x ^ 2 - 2 * x + 1.76'),
}

ENABLE_LOGGING = True

while True:
    # Выбор функции
    function = ConsoleFunctionality.choose_equation(predefined_functions)

    # Выбор метода
    method_number = ConsoleFunctionality.choose_method_number(methods)

    while True:
        # Ввод исходных данных
        left, right, epsilon, decimal_places = ConsoleFunctionality.read_initial_data()

        # Верификация исходных данных
        method = methods[method_number](function, left, right, epsilon, decimal_places, ENABLE_LOGGING)
        try:
            verified, reason = method.check()
        except TypeError as te:
            print('(!) Ошибка при вычислении значения функции, возможно она не определена на всем интервале.')
            continue
        if verified:
            break
        else:
            print('(!) Введенные исходные данные для метода некорректны: ', reason)

    # Вывод графика функции
    try:
        function.draw(left, right)
    except Exception as e:
        print('(!) Не удалось построить график функции, ', e)

    # Выбор места вывода результата
    output_file_name = input("Введите имя файла для вывода результата или пустую строку, чтобы вывести в консоль: ")

    # Решение
    try:
        if ENABLE_LOGGING:
            print('Процесс решения: ')
        result = method.solve()
    except Exception as e:
        print(e)
        print('(!) Что-то пошло не так при решении: ', e)
        continue

    # Вывод
    ConsoleFunctionality.print_result(result, output_file_name)

    if input('\nЕще раз? [y/n] ') != 'y':
        break
