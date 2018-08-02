n = eval(input())

if n > 1 and n % 2 == 1:
    print(' '*(n-1), '*', sep='')  # 頂部
    check = n-2

    m = 0
    len_base = n  # 5
    len_base2 = (n-2)//2

    for i in range(check):
        # print(i)
        # input()
        m = 0
        for j in range(1, 4):
            for k in range(1, n+m+1+i):
                if k < n-j+1-i:
                    print(' ', end='')
                else:
                    print('^', end='')
            print()
            m += 1

    for i in range(1, len_base2*2+2):
        for j in range(1, n+len_base2+1):
            if j < n-len_base2:
                print(' ', end='')
            else:
                print('#', end='')
        print()
