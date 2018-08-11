def sum1(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def return2num(n=0):

    return fact(n), sum1(n)


result1, result2 = return2num(int(input()))
print(result1)
print(result2)
