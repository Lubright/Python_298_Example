n = eval(input())

for i in range(1, n+1):
    for j in range(1, n+i):
        if j < (n-i+1):
            print(' ', end='')
        else:
            print('*', end='')
    print()
