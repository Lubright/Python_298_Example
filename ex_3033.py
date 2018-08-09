n0 = eval(input())
d = eval(input())
n = eval(input())

number_series = []

for i in range(n):
    number_series.append(n0+i*d)

# print(number_series)

for i, v in enumerate(number_series):
    if i == len(number_series)-1:
        if v < 0:
            print('({}) = '.format(v), end='')
        else:
            print(v, '= ', end='')
    else:
        if v < 0:
            print('({}) + '.format(v), end='')
        else:
            print(v, '+ ', end='')

print(sum(number_series))
