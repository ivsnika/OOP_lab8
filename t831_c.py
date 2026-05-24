# t831_c.py
import numpy as np

def calculate_determinant(n):
    if n <= 0:
        return 0
    matrix = np.zeros((n, n))

    for i in range(n):
        matrix[i, i] = 2
        if i < n - 1:
            matrix[i, i + 1] = 3
        if i > 0:
            matrix[i - 1, i] = 1

    det = np.linalg.det(matrix)
    return round(det)

if __name__ == "__main__":
    try:
        n = int(input("Введіть порядок матриці n: "))
        if n < 1:
            print("Порядок матриці має бути >= 1")
        else:
            result = calculate_determinant(n)
            print(f"Визначник матриці порядку {n} дорівнює: {result}")
    except ValueError:
        print("Помилка: введіть ціле число.")