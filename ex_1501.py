n = int(input(''))


def fun1(n):
    while(n):
        temp = n % 10
        # print(n)
        if temp == 7:
            return True
        n //= 10
    return False


if n % 7 == 0 or fun1(n):
    print('YES')
else:
    print('NO')
