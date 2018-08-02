dic = {4: '鼠', 5: '牛', 6: '虎', 7: '兔', 8: '龍', 9: '蛇',
       10: '馬', 11: '羊', 0: '猴', 1: '雞', 2: '狗', 3: '豬'}


def Year_Checker(n, minguo=False):  # 預設西元年(minguo)
    # n必須是整數(int)
    # minguo(代表民國年)
    if minguo == False:
        index = n % 12
        return dic[index]
    elif minguo == True:
        index = (n+1911) % 12
        return dic[index]


op = input()
result = []

while True:
    line = input()
    if line == '-1':
        break
    if op == 'AD':
        result.append(Year_Checker(int(line)))
    elif op == 'Minguo':
        result.append(Year_Checker(int(line), True))


for e in result:
    print(e)
