# t831_e.py
import math

def taylor_sin(x, eps):
    sum_sin = 0.0
    term = x
    n = 1

    while abs(term) >= eps:
        sum_sin += term
        term = -term * (x**2) / ((2 * n) * (2 * n + 1))
        n += 1

    return sum_sin


if __name__ == "__main__":
    try:
        x = float(input("Введіть значення x (в радіанах): "))
        eps = float(input("Введіть точність eps (наприклад, 0.00001): "))

        if eps <= 0:
            print("Точність eps має бути більшою за 0.")
        else:
            taylor_res = taylor_sin(x, eps)
            math_res = math.sin(x)

            print(f"\nРезультат через ряд Тейлора: {taylor_res}")
            print(f"Результат з бібліотеки math:  {math_res}")
            print(f"Різниця (абсолютна похибка):  {abs(taylor_res - math_res)}")

    except ValueError:
        print("Помилка: введіть коректні дійсні числа.")