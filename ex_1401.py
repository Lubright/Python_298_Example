
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


line = input()
result_int = 1
result_float = 1
cnt_int = 0
cnt_float = 0


while line != 'q':
    if isInt(line):
        result_int *= int(line)
        cnt_int += 1
    elif isFloat(line):
        result_float *= float(line)
        cnt_float += 1
    elif line == 'q':
        break

    line = input()

if cnt_float == 0:
    result_float = 0
elif cnt_int == 0:
    result_int = 0

print('{:.2f}'.format(result_float))
print(result_int)

if result_float > result_int:
    print('Float > Int')
elif result_float < result_int:
    print('Float < Int')
else:
    print('Float = Int')
