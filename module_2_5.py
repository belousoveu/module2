# method 1. использование вложенных циклов
def get_matrix(row, col, value):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(value)
    return matrix


# method 2. использование list comprehension
def get_matrix_new(row, col, value):
    return [[value for j in range(col)] for i in range(row)]


m_1 = get_matrix(2, 2, 10)
print(m_1)
print(get_matrix_new(2, 2, 10))

m_2 = get_matrix(3, 5, 42)
print(m_2)
print(get_matrix_new(3, 5, 42))

m_3 = get_matrix(4, 2, 13)
print(m_3)
print(get_matrix_new(4, 2, 13))

print(get_matrix(10, 0, 55))
print(get_matrix_new(10, 0, 55))
