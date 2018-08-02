
def isFloat(num):
    try:
        float(num)
    except:
        return False
    else:
        return True


def isInt(num):
    try:
        int(num)
    except:
        return False
    else:
        return True


result = []

while True:
    line = input()
    if isInt(line):
        result.append(int(line))
    elif isFloat(line):
        result.append(float(line))

    elif line == 'q':
        break
    else:
        print('Please Enter Numbers Only')


result2 = sorted(result)
result3 = sorted(result, reverse=True)


print(result)
print(result2)
print(result3)
print(result)
