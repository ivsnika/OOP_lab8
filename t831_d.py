# t831_d.py


def sum_sn_generator(n):
    a1, a2 = 0, 1
    total_sum = 0.0

    total_sum += (2**1) * a1
    yield total_sum

    if n >= 2:
        total_sum += (2**2) * a2
        yield total_sum

        for k in range(3, n + 1):
            ak = a2 + k * a1
            total_sum += (2**k) * ak
            yield total_sum
            a1 = a2
            a2 = ak


if __name__ == "__main__":
    n = int(input("Введіть значення n: "))
    if n >= 1:
        gen = sum_sn_generator(n)
        result = None
        for current_sum in gen:
            result = current_sum
        print(f"Сума S_{n} = {result}")
