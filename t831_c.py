# t831_c.py

def determinant_generator(n):
    if n >= 1:
        d_minus_2 = 1
        d_minus_1 = 2
        yield d_minus_1

        if n >= 2:
            d_current = 2 * d_minus_1 - 3 * d_minus_2
            yield d_current

            for _ in range(3, n + 1):
                d_minus_2 = d_minus_1
                d_minus_1 = d_current
                d_current = 2 * d_minus_1 - 3 * d_minus_2
                yield d_current


if __name__ == "__main__":
    n = int(input("Введіть порядок matrix n: "))
    if n >= 1:
        gen = determinant_generator(n)
        result = None
        for det in gen:
            result = det
        print(f"Визначник матриці порядку {n} дорівнює: {result}")
