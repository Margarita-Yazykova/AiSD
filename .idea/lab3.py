def read_matrix(filename):
    with open(filename, "r") as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def print_matrix(name, m):
    print(f"{name}:")
    for row in m:
        print(row)
    print()

K = int(input("Введите значение K: "))
N = int(input("Введите размерность матрицы N: "))

filename = "matrix.txt"

A = read_matrix(filename)
print_matrix("Матрица А", A)

F = [row[:] for row in A]
# Количество чисел > K в нечетных столбцах области 4
kol = 0
for i in range(N // 2, N):
    for j in range(i):
        if j % 2 != 0 and F[i][j] > K:
            kol += 1
# Произведение чисел в нечетных строках области 2
proizvedenie = 1
for i in range(N // 2):
    for j in range(N - i, N):
        if i % 2 != 0:
            proizvedenie *= F[i][j]

if kol > proizvedenie:
    print("kol > proizvedenie. Перестановка симметрично областей 1 и 3: ")
    for i in range(N):
        for j in range(0, N - i):
            if (j != N - i - 1) and (j != i):
                F[i][j], F[i][N - j - 1] = F[i][N - j - 1], F[i][j]
else:
    print("kol <= proizvedenie. Перестановка несимметрично областей 1 и 2: ")
for i in range(0, N - 1):
    for j in range(0, i):
        if i + j < N - 1:
                F[i][j], F[j][j - i + ( N - j - 1)] = F[j][j - i + ( N - j - 1)], F[i][j]
print_matrix("Матрица F", F)
# K * A
ka = [[K * A[i][j] for j in range(N)] for i in range(N)]
print_matrix("K * A", ka)
# (K * A) * F
ka_f = [[sum(ka[i][m] * F[m][j] for m in range(N)) for j in range(N)] for i in range(N)]
print_matrix("(K * A) * F", ka_f)
# F^T
f_t = [[F[j][i] for j in range(N)] for i in range(N)]
print_matrix("F^T", f_t)
# K * F^T
kf_t = [[K * f_t[i][j] for j in range(N)] for i in range(N)]
print_matrix("K * F^T", kf_t)
# ((K * A) * F) + (K * F^T)
result = [[ka_f[i][j] + kf_t[i][j] for j in range(N)] for i in range(N)]
print_matrix("((K * A) * F) + (K * F^T)", result)