input_str = input()
z1, z2 = input_str.split(' ')
z1 = int(z1)
z2 = int(z2)

List_para_1 = [1, 1, z1]
List_para_2 = [2, 4, z2]


def fun1(list1, list2):
    x, y = None, None
    temp1 = list1[:]
    temp2 = list2[:]
    m_x = temp2[0]/temp1[0]
    temp1 = [e*m_x for e in temp1]
    # print(temp1)
    if (temp2[2]-temp1[2]) % (temp2[1]-temp1[1]) == 0:
        y = int((temp2[2]-temp1[2])/(temp2[1]-temp1[1]))

    if y:
        x = list1[2]-(list1[1]*y)
    # x = x/m_x
    if x:
        if x < 0 or y < 0:
            x = None
            y = None
    # print(x)

    return x, y


x, y = fun1(List_para_1, List_para_2)
# print(x, y)

if x and y:
    print('YES')
    print(x, y)
else:
    print('NO')
