#В группе N человек. Сформировать все возможные варианты разбиения группы на подгруппы при условии,
# что в подгруппу входит не более 10 человек
import time
n = int(input("Введите количество человек в группе (N): "))
def gen_parts(n, max_size=10):
    def split(remain, curr):
        if not remain:  # Если никого не осталось, добавляем разбиение
            if len(curr) > 1:  # Исключаем случаи с разбиением одной группой
                res.append(curr)
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
parts = gen_parts(n)
unique = []
for p in parts:
    sorted_p = sorted([sorted(group) for group in p])
    if sorted_p not in unique:
        unique.append(sorted_p)

end = time.time()
print(f"Количество возможных разбиений для группы из {n} человек: {len(unique)}")
for part in unique:
    print(part)
print(f"Время выполнения: {end - start:.5f} секунд")