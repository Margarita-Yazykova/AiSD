#Ограничение на минимальный размер подгруппы
#оптимальное разбиение, где разница в размерах подгрупп минимальна

import time
n = int(input("Введите количество человек в группе (N): "))
min_size = int(input("Введите минимальный размер подгруппы (min_size): "))
max_size = 10
def gen_parts(n, min_size, max_size):
    def split(remain, curr):
        if not remain:  # Если никого не осталось, проверяем корректность разбиения
            if len(curr) > 1 and all(len(group) >= min_size for group in curr):
                res.append(curr) #если сходится, добавляем человека туда либо ниже создаем новую группу с этим человеком
            return
        person = remain[0]
        for i in range(len(curr)):
            if len(curr[i]) < max_size:  # Добавляем в существующую группу
                split(remain[1:], curr[:i] + [curr[i] + [person]] + curr[i + 1:])
        split(remain[1:], curr + [[person]])  # Создаем новую группу
    res = []
    split(list(range(1, n + 1)), [])
    return res

start = time.time()
parts = gen_parts(n, min_size, max_size)
unique = []
for p in parts:
    sorted_p = sorted([sorted(group) for group in p])
    if sorted_p not in unique:
        unique.append(sorted_p)

def calculate_difference(partition): # Нахождение оптимального разбиения
    sizes = [len(group) for group in partition]
    return max(sizes) - min(sizes)
optimal_partition = min(unique, key=calculate_difference)
end = time.time()
print(f"Количество возможных разбиений для группы из {n} человек: {len(unique)}")
print("\nВсе уникальные разбиения:")
for part in unique:
    print(part)
print("\nОптимальное разбиение:")
print(optimal_partition)
print(f"Время выполнения: {end - start:.5f} секунд")