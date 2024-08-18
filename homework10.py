def get_matrix(n, m ,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix
    print(matrix)
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество стоблцов матрицы: "))
value = int(input("Введите значение матрицы: "))

if n <= 0:
    print("Матрица где то рядом")
elif m <= 0:
    print("Матрица где то рядом")
else:
    matrix = get_matrix(n, m, value)
    print(matrix)




