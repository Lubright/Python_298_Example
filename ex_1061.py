def sum1(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


print(sum1(eval(input())))
