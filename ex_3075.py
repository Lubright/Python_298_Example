def inputList(lst):
    while True:
        num = int(input())
        if num == -1:
            break
        lst.append(num)


def Find3rdMax(lst):
    lst.sort()
    print('sorted =', lst)
    return lst[-3]


list1 = []
inputList(list1)
print('input =', list1)
print('max 3rd =', Find3rdMax(list1.copy()))
print('list =', list1)
