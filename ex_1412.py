dic = {'A': 10, 'J': 18, 'S': 26,
       'B': 11, 'K': 19, 'T': 27,
       'C': 12, 'L': 20, 'U': 28,
       'D': 13, 'M': 21, 'V': 29,
       'E': 14, 'N': 22, 'W': 32,
       'F': 15, 'O': 35, 'X': 30,
       'G': 16, 'P': 23, 'Y': 31,
       'H': 17, 'Q': 24, 'Z': 33,
       'I': 34, 'R': 25}


def ID_Checker(n):
    # 因為有20分的輸入是小寫的，請自行在程式中修改成可以讀取小寫字母也能讓字典索引到。
    # 如果沒有改的話，輸入小寫會runtime error，只會拿到80分。
    if len(n) == 10:
        n = str(dic[n[0]]) + n[1:]
        LIST = []
        for i in range(0, len(n)):
            if i == 0:
                LIST.append(int(n[i]) * 1)
            elif i == 10:
                LIST.append(int(n[i]) * 1)

            else:
                LIST.append(int(n[i]) * (10-i))
        Total = sum(LIST)
        return Total
    else:
        return 1  # 身分證不足10碼回傳1


# list_input_line=[]
result = []

while True:
    line = input()
    if line == '-1':
        break

    check = ID_Checker(line.upper())
    if check == 1:
        result.append('fake')
    elif check % 10 == 0:
        result.append('real')
    else:
        result.append('fake')

for e in result:
    print(e)
