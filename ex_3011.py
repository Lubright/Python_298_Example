n = input()

if n.isnumeric():
    n = int(n)
    if n > 0:
        print('n={}'.format(n))
else:
    print('is not a number')
