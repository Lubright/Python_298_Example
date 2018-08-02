n = eval(input())
m = eval(input())

for i in range(1, n+1):
    for j in range(1, m+1):
        print('{}*{}={:2d}'.format(i, j, i*j), end=' ')
    print()
