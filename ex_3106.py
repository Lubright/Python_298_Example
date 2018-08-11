def matrixMultiPly(a, b):
    result = []
    temp_result = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        temp_result.clear()
        for j in range(m):
            temp = 0
            for k in range(m):
                temp += (a[i][k]*b[k][j])
            temp_result.append(temp)
        result.append(temp_result[:])
    return result


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

a = []
b = []

for i in range(3):
    row = input()
    row = [int(e) for e in row.split(' ') if e != '']
    a.append(row)
for i in range(3):
    row = input()
    row = [int(e) for e in row.split(' ') if e != '']
    b.append(row)

result = matrixMultiPly(a, b)

for e in result:
    print(e)
