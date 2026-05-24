# t831_d.py

def get_a_sequence(n):
    a = [0] * (max(n, 2) + 1)
    a[1] = 0
    a[2] = 1
    for k in range(3, n + 1):
        a[k] = a[k - 1] + k * a[k - 2]
    return a

def calculate_sum_sn(n):
    if n < 1:
        return 0

    a = get_a_sequence(n)
    total_sum = 0
    for k in range(1, n + 1):
        total_sum += (2**k) * a[k]
    return total_sum

if __name__ == "__main__":
    try:
        n = int(input("Введіть значення n: "))
        if n < 1:
            print("n повинно бути >= 1")
        else:
            result = calculate_sum_sn(n)
            print(f"Сума S_{n} = {result}")
    except ValueError:
        print("Помилка: введіть ціле число.")