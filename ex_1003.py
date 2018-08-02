a = int(input())
b = int(input())
c = int(input())

sum1 = a+b+c
ave1 = sum1/3
mul1 = a*b*c
min1 = min((a, b, c))
max1 = max((a, b, c))

print('sum is', sum1)
print('average is %.2f' % (ave1))
print('product is', mul1)
print('smallest is', min1)
print('largest is', max1)
