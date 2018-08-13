def swap(list):
    list[0], list[1] = list[1], list[0]


list1 = []

for i in range(2):
    list1.append(int(input()))

swap(list1)

for e in list1:
    print(e)
