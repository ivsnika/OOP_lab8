# t831_a.py


def calculate_sequence_element(x, k):
    if k < 1:
        return "k повинно бути >= 1"
    return (x**k) / k


if __name__ == "__main__":
    try:
        x = float(input("Введіть значення x: "))
        k = int(input("Введіть значення k (k >= 1): "))

        result = calculate_sequence_element(x, k)
        print(f"Результат x_{k} = {result}")
    except ValueError:
        print("Помилка: введіть коректні числа.")