#17.	F(0) = 1, F(1) = 1, F(n) = (-1)n*(F(n–1)/n! - F(n-2) /(2n)!), при n > 1
import timeit
import matplotlib.pyplot as plt
import math
def F_recursive(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        factorial_n = 1
        for i in range(2, n + 1):
            factorial_n *= i
        factorial_2n = factorial_n * (n + 1) * (n + 2)
        memo[n] = (-1 if n % 2 else 1) * (F_recursive(n - 1, memo) / factorial_n - F_recursive(n - 2, memo) / factorial_2n)
    return memo[n]

def F_iterative(n):
    if n == 0 or n == 1:
        return 1
    F0, F1 = 1, 1
    factorial_n = 1
    for i in range(2, n + 1):
        factorial_n *= i
        sign = (-1 if i % 2 else 1)
        F_next = sign * (F1 / factorial_n - F0 / (factorial_n * (2 * i - 1) * (2 * i)))
        F0, F1 = F1, F_next
    return F1

def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    results = []

    n = 0
    while n <= max_n:
        recursive_timer = timeit.Timer(lambda: F_recursive(n))
        recursive_time = recursive_timer.timeit(number=1)
        recursive_times.append(recursive_time)

        iterative_timer = timeit.Timer(lambda: F_iterative(n))
        iterative_time = iterative_timer.timeit(number=1)
        iterative_times.append(iterative_time)

        recursive_result = F_recursive(n)
        iterative_result = F_iterative(n)
        results.append((n, recursive_result, iterative_result))
        n += 1
    return recursive_times, iterative_times, results

def main():
    try:
        n = int(input("Введите значение n: "))
        if n < 0:
            raise ValueError("Число должно быть неотрицательным.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return
    recursive_times, iterative_times, results = compare_methods(n)

    print("Таблица результатов:")
    header = f"{'n':<3} | {'Рекурсивное значение':<25} | {'Итеративное значение':<25} | {'Время рекурсии (с)':<20} | {'Время итерации (с)':<20}"
    print(header)
    print("-" * len(header))
    for n, recursive_result, iterative_result in results:
        print(f"{n:<3} | {str(recursive_result):<25} | {str(iterative_result):<25} | {recursive_times[n]:<20.6f} | {iterative_times[n]:<20.6f}")

    plt.figure(figsize=(10, 5))
    plt.plot(range(n + 1), recursive_times, label='Рекурсивный метод')
    plt.plot(range(n + 1), iterative_times, label='Итеративный метод')
    plt.xlabel('n')
    plt.ylabel('Время выполнения (с)')
    plt.title('Сравнение времени выполнения рекурсивного и итеративного методов')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
