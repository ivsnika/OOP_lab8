# t831_b.py


def calculate_product(n):
    product = 1.0
    for i in range(1, n + 1):
        product *= 1 / (i + 1)
    return product


if __name__ == "__main__":
    try:
        n = int(input("Введіть значення n (n >= 1): "))
        if n < 1:
            print("Параметр n має бути більшим або рівним 1.")
        else:
            result = calculate_product(n)
            print(f"Результат P_{n} = {result}")
    except ValueError:
        print("Помилка: введіть ціле число.")