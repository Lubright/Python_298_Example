n = int(input())
result = 0


def fact1(n):
    if n == 0 or n == 1:
        return 1
    return n*fact1(n-1)


result = fact1(n)

print(result)
