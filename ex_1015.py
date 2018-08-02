c = input()

list1 = []
while c[0] != 'q':
    # print(c)

    if c[0] == ' ' or c[0] == '\t' or c[0] == '\n':
        c = input()

        continue
    list1.append(c[0])
    c = input()

list1.append(c[0])

for e in list1:
    print(e)
