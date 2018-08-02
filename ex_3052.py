n = eval(input())
k = 0
check = n//2+1
for i in range(1, n+1):
    for j in range(1, check+k+1):
        if j < (check-k):
            print(' ', end='')
        else:
            print('*', end='')

    print()

    if i < check:
        k += 1
    else:
        k -= 1
