import re
id_zone_tw_map = {'A': 10, 'J': 18, 'S': 26,
                  'B': 11, 'K': 19, 'T': 27,
                  'C': 12, 'L': 20, 'U': 28,
                  'D': 13, 'M': 21, 'V': 29,
                  'E': 14, 'N': 22, 'W': 32,
                  'F': 15, 'O': 35, 'X': 30,
                  'G': 16, 'P': 23, 'Y': 31,
                  'H': 17, 'Q': 24, 'Z': 33,
                  'I': 34, 'R': 25}
list_m = list(range(8, 0, -1))
list_m.append(1)
pattern_id = re.compile('\w\d{9}')
# line = 'A123456789'
line = input()
if pattern_id.match(line):
    line2 = list(line)
    line2[0] = id_zone_tw_map[line2[0].upper()]

    # print(line2)

    result = (line2[0]//10)+(line2[0] % 10)*9
    for i in range(1, 10):
        # line2[i] = int(line2[i])
        result += int(line2[i])*list_m[i-1]
    # print(result)

    if result % 10 == 0:
        print('real')
    else:
        print('fake')

else:
    print('fake')
