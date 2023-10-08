'''
Напишите функцию для транспонирования матрицы
'''
def transpose_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    return new_matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(*transpose_matrix(matrix), sep='\n')