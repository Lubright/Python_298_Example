n = int(input())

list1 = list(range(2, n+1))

result = list1[:]

for e in list1:
    m = 2
    while e*m <= n:
        temp = e*m
        if temp in result:
            result.remove(e*m)
        m += 1

for e in result:
    print('{} is prime'.format(e))
