cypher_map = {}

for i in range(65, 65+26):
    cypher_map[chr(i)] = i-64

# print(cypher_map)
N = int(input())
line_list = []

if N > 10:
    exit()
else:
    result = []

    for i in range(N):
        temp = input()
        line_list.append(temp.upper())

    for e in line_list:
        temp = 0
        for v in e:
            temp += cypher_map[v]
        result.append((e, temp))
        print('{} = {}'.format(e, temp))

    result.sort(key=lambda x: x[1], reverse=True)
    print(result[0][0], 'is the key.')
