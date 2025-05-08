import numpy as np
import matplotlib.pyplot as plt
import random
sum = kol = diag_F = 0

def read_matrix(filename):
    with open(filename, "r") as file:
        matrix = [list(map(int, line.split())) for line in file]
    return np.array(matrix)
def print_matrix(name, m):
    print(f"{name}:")
    for row in m:
        print(row)
    print()

K = int(input("Введите значение K: "))
N = int(input("Введите размерность матрицы N: "))

filename = "matrix_1.txt"

A = read_matrix(filename)
print_matrix("Матрица А", A)

F = np.array([row[:] for row in A])

for i in range(N // 2, N):
    for j in range(N // 2, N):
        if j % 2 != 0 and F[i][j] == 0:
            kol += 1
print("Количество нулей в нечётных столбцах: ", kol)

for i in range(N // 2, N):
    for j in range(N // 2, N):
        if i % 2 != 0:
            sum += F[i][j]
print("Сумма чисел в нечетных строках: ", sum)

if (kol > sum):
    for i in range(N // 2):
        for j in range(N // 2):
            F[i][j], F[i + N // 2][j + N // 2] = F[i + N // 2][j + N // 2], F[i][j] # Замена B и Е симметрично
else:
    for i in range(N // 2):
        for j in range(N // 2, N):
            F[i][j], F[i + N // 2][j] = F[i + N // 2][j], F[i][j] # Замена C и E несимметрично

print_matrix("Матрица F", F)

# Вычисление нижней треугольной матрицы G
G = [[random.randint(0,0) for i in range(N)] for j in range(N)]
for i in range(N // 2 + 1, N):
    for j in range(N - i, i):
        G[i][j] = int(A[i][j])
print_matrix("Нижняя треугольная матрица G", G)

sum_diag_F = np.trace(F) # сумма диагональных элементов матрицы F
det_A = np.linalg.det(A) # определитель матрицы A

print("Определитель матрицы A:", det_A)
print("Сумма диагональных элементов F:", sum_diag_F)

if (det_A > sum_diag_F):
    print("det_A > sum_diag_F. Вычисление A * A.T - K * F.T")
    A_tr=[[A[j][i] for j in range(N)] for i in range(N)]
    A_np = np.array(A)
    F_np = np.array(F)
    A_tr_np = np.array(A_tr)
    result = np.matmul(np.linalg.pinv(A_np), A_tr_np) - np.matmul(K * np.linalg.pinv(F_np))
    result_r = np.round(result)
else:
    print("det_A < sum_diag_F. Вычисление A.T + G⁻¹ - F⁻¹")
    A_tr=[[A[j][i] for j in range(N)] for i in range(N)]
    F_tr=[[F[j][i] for j in range(N)] for i in range(N)]
    G = [[random.randint(0,0) for i in range(N)] for j in range(N)]
    for i in range(N // 2 + 1, N):
        for j in range(N - i, i):
            G[i][j] = A[i][j]
    A_np = np.array(A)
    F_np = np.array(F)
    G_np = np.array(G)
    result = (np.linalg.pinv(A_np) + G_np - np.linalg.pinv(F_np)) * K
    result_r = np.round(result)
print("\nВычисление по формуле: \n")
for A in result_r:
    print(A)

plt.figure(figsize=(N, N))

plt.subplot(1, 3, 1)
plt.imshow(F, cmap='coolwarm')

plt.subplot(1, 3, 2)
row_means = np.mean(F, axis=1) #среднее значение для каждой строки матрицы F
plt.plot(row_means, marker='o', color='red')

plt.subplot(1, 3, 3) #гистограмма
plt.hist(F_np.flatten(), bins=N, color='green', edgecolor='black') #метод flatten() преобразует матрицу в одномерный массив

plt.tight_layout()
plt.show()