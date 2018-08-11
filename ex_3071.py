def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def P(n, m):

    return fact(n)//fact(n-m)


n = int(input())
m = int(input())

result = P(n, m)

print(result)
