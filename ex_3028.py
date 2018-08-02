a = eval(input())
b = eval(input())
c = eval(input())

list1 = [a, b, c]

list1.sort()

if list1[0]+list1[1] > list1[2]:
    print('True')
    if list1[2] ** 2 == (list1[0]**2)+(list1[1]**2):
        print('Right Triangle')
    else:
        print('Non-Right Triangle')
else:
    print('False')
