n = eval(input())

sum1 = 0
max1 = 0
max_index = 0
cnt1 = 0

while n != -1:
    sum1 += n
    cnt1 += 1
    if n > max1:
        max1 = n
        max_index = cnt1

    n = eval(input())

print(sum1)
print('{:.1f}'.format(sum1/cnt1))
print(max1)
print(max_index)
