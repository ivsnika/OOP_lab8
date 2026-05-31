# t831_a.py

def sequence_generator(x):
    k = 1
    current = x
    while True:
        yield current
        k += 1
        current = current * x * (k - 1) / k


if __name__ == "__main__":
    x = float(input("Введіть значення x: "))
    k = int(input("Введіть значення k (k >= 1): "))

    if k >= 1:
        gen = sequence_generator(x)
        result = None
        for _ in range(k):
            result = next(gen)
        print(f"Результат x_{k} = {result}")
