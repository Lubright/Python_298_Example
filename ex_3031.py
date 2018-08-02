num = int(input())

result = num//12
result2 = num % 12

if result2:
    print('{} dozen and {}'.format(result, result2))
else:
    print('{} dozen'.format(result))
