# t831_e.py
import math


def taylor_sin_generator(x):
    sum_sin = 0.0
    term = x
    n = 1
    while True:
        sum_sin += term
        yield sum_sin, term
        term = -term * (x**2) / ((2 * n) * (2 * n + 1))
        n += 1


if __name__ == "__main__":
    x = float(input("Введіть значення x (в радіанах): "))
    eps = float(input("Введіть точність eps (наприклад, 0.00001): "))

    if eps > 0:
        gen = taylor_sin_generator(x)
        taylor_res = 0.0

        for current_sum, current_term in gen:
            taylor_res = current_sum
            if abs(current_term) < eps:
                break

        math_res = math.sin(x)
        print(f"\nРезультат через ряд Тейлора: {taylor_res}")
        print(f"Результат з бібліотеки math:  {math_res}")
        print(f"Різниця (абсолютна похибка):  {abs(taylor_res - math_res)}")
