import random

a = int(input('введите число оприделяющее размер матрицы: '))
b = int(input('введите число оприделяющее размер матрицы: '))
q1 = []
matrix_1 = [[(random.randint(-100, 100)) for i in range(a)] for j in range(b)]
matrix_2 = [[(random.randint(-100, 100)) for e in range(a)] for f in range(b)]

print('matrix_1 размер ', a, '*', b, ':')
for i in matrix_1:
    print(*i)

print('matrix_2 размер ', a, '*', b, ':')
for i in matrix_2:
    print(*i)

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(a)] for i in range(b)]
print('matrix_3 результат сложения матриц:')
for i in matrix_3:
    print(*i)

# for i in range(a):
# for w in range(b):
# print(matrix_3,end=' ')
# print()
