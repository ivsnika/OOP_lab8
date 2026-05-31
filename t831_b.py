# t831_b.py


def product_generator(n):
    product = 1.0
    for i in range(1, n + 1):
        product *= 1 / (i + 1)
        yield product


if __name__ == "__main__":
    n = int(input("Введіть значення n (n >= 1): "))
    if n >= 1:
        gen = product_generator(n)
        result = None
        for val in gen:
            result = val
        print(f"Результат P_{n} = {result}")
