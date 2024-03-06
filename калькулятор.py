def calculate():
    while True:  # бесконечный цикл
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Ошибка! Введите корректный оператор.")
            continue  # возврат к началу цикла

        print("Результат:", result)

        choice = input("Хотите ли вы выполнить дополнительное вычисление? (да/нет): ")
        if choice.lower() == 'нет' or choice.lower() == 'н':
            break  # выход из цикла

    print("Программа завершена.")


calculate()
