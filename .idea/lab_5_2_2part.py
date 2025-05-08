import itertools
import time

n = int(input("Введите количество человек в группе (N): "))
group_size = n//2
if n % 2 != 0:
    print("Не найдено подходящих разбиений: количество людей должно быть кратно 2.")
    exit()

people = list(range(1, n + 1))
start = time.time()

res = []  # Генерация всех разбиений
for groups_count in range(1, n // group_size + 1):
    for comb in itertools.combinations(itertools.combinations(people, group_size), groups_count):
        flat_comb = [item for group in comb for item in group]
        if set(flat_comb) == set(people):
            res.append([list(group) for group in comb])

unique = []  # Удаление дубликатов
seen = set()
for part in res:
    key = tuple(sorted([tuple(sorted(group)) for group in part]))
    if key not in seen:
        seen.add(key)
        unique.append(part)

end = time.time()
if not unique:
    print("Не найдено подходящих разбиений.")
    exit()
print(f"Количество возможных разбиений для группы из {n} человек: {len(unique)}\n")
for part in unique:
    print(part)
print(f"\nВремя выполнения: {end - start:.5f} секунд")