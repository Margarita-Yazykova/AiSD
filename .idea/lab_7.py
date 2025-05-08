import tkinter as tk
from tkinter import ttk
import itertools
import time
from tkinter import messagebox

def generate_parts():
    try:
        n = int(entry_n.get())
        if n % 2 != 0:
            messagebox.showerror("Ошибка", "Количество людей должно быть кратно 2.")
            return
        group_size = n // 2
        people = list(range(1, n + 1))
        start = time.time()

        res = []  # Генерация всех разбиений
        for groups_count in range(1, n // group_size + 1):
            for comb in itertools.combinations(itertools.combinations(people, group_size), groups_count):
                flat_comb = [item for group in comb for item in group]
                if set(flat_comb) == set(people):
                    res.append([list(group) for group in comb])

        unique = []
        seen = set()
        for part in res:
            key = tuple(sorted([tuple(sorted(group)) for group in part]))
            if key not in seen:
                seen.add(key)
                unique.append(part)

        end = time.time()
        output_text.delete(1.0, tk.END)# Очистка текстового поля и вывод результатов
        if not unique:
            output_text.insert(tk.END, "Не найдено подходящих разбиений.\n")
        else:
            output_text.insert(tk.END, f"Количество возможных разбиений для группы из {n} человек: {len(unique)}\n\n")
            for part in unique:
                output_text.insert(tk.END, f"{part}\n")
            output_text.insert(tk.END, f"\nВремя выполнения: {end - start:.5f} секунд\n")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное целое число.")

root = tk.Tk()
root.title("Генерация разбиений группы")  #главное окно с заголовком
style = ttk.Style()
style.theme_use('clam')

frame_input = ttk.Frame(root, padding="10 10 10 10")
frame_input.pack(pady=15, padx=20)

label_n = ttk.Label(frame_input, text="Введите количество человек (N):", font=("Arial", 12))
label_n.pack(side=tk.LEFT, padx=5)

entry_n = ttk.Entry(frame_input, width=10, font=("Arial", 12))  #поле ввода
entry_n.pack(side=tk.LEFT, padx=5)

button_generate = ttk.Button(frame_input, text="Сгенерировать", command=generate_parts)  #кнопка, при нажатии вызывается функция generate_parts
button_generate.pack(side=tk.LEFT, padx=5)

frame_output = ttk.Frame(root, padding="10 10 10 10")
frame_output.pack(pady=15, padx=20)

scrollbar = ttk.Scrollbar(frame_output)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(frame_output, wrap=tk.WORD, height=20, width=60, bg="lightyellow", font=("Courier", 10), yscrollcommand=scrollbar.set) #текстовое поле жля вывода
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=output_text.yview)

# Запуск программы
root.mainloop()