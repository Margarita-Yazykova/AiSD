import itertools
import time
n = int(input("Введите количество человек в группе (N): "))
def gen_parts_func(n, max_size=10):
    people = list(range(1, n + 1))
    res = []
    for size in range(1, n):
        for comb in itertools.combinations(people, size):
            remain = set(people) - set(comb) # определяем оставшихся людей
            if len(remain) > 0:  # Проверяем, что остаются люди для формирования другой группы
                res.append([list(comb), list(remain)])
    unique = []
    for part in res:
        sorted_part = sorted([sorted(group) for group in part])
        if sorted_part not in unique:
            unique.append(sorted_part)
    return unique
start = time.time()
parts = gen_parts_func(n, max_size=10)
end = time.time()
print(f"Количество возможных разбиений для группы из {n} человек: {len(parts)}")
for part in parts:
    print(part)
print(f"Время выполнения: {end - start:.5f} секунд")