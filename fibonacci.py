def fibonacci(n):
    if n <= 0:
        return "Введіть число більше за 0"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    n = int(input("Введіть кількість чисел Фібоначчі: "))
    print(f"Перші {n} чисел Фібоначчі: {fibonacci(n)}")
