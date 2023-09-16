import math
while True:
    print("Выберите действие")
    print("1. Сложение")
    print("2. Вычетание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возедение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")
    
    choice = input("Выберите номер действие: ")
    if choice == '0':
        break

    if choice in('1','2','3','4','5','6','7','8','9','10'):
        try:
            num1=float(input("Введите первое число: "))
            if choice != '6' or '7' or '8' or '9' or '10':
                num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Неверный формат числа")
            continue 
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Делить на ноль нельзя")
                continue
            result = num1 / num2
        elif choice == '5':
            result = num1 ** num2
        elif choice == '6':
            if num1 < 0:
                print("Ошибка: Корень из отрицательного числа")
                continue
            result = math.sqrt(num1)
        elif choice == '7':
            if num1 < 0:
                print("Ошибка: Факториал отрицательного числа")
                continue
            result = math.factorial(int(num1))
        elif choice == '8':
            result = math.sin(num1)
        elif choice == '9':
            result = math.cos(num1)
        elif choice == '10':
            result = math.tan(num1)
        
        print("Результат:", result)
    else:
        print("Неверная операция")