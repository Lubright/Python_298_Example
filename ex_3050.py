n = eval(input())
cnt1 = 1
for i in range(1, n+1):
    for j in range(i):
        print(cnt1, end=' ')
        cnt1 += 1
    print()
