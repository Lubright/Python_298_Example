def pack(list1, dict1, c):
    max_len = max(dict1.values())
    # print(max_len)
    print(c*(max_len+2))

    for e in list1:
        print('{}{: <{max_len}s}{}'.format(c, e, c, max_len=max_len))

    print(c*(max_len+2))


dict1 = {}
list1 = []
while True:
    line = input()
    if line == '-1':
        break
    dict1[line] = len(line)
    list1.append(line)

c = input()


# print(dict1)

pack(list1, dict1, c[0])
