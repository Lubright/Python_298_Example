while True:
    line = input()
    if line.isdigit():
        n = int(line)
        print('n={}'.format(n))
        break
    else:
        print('is not a number')
