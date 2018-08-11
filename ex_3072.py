def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def C(n, m):

    return fact(n)//fact(n-m)//fact(m)


n = int(input())
m = int(input())

result = C(n, m)

print(result)
