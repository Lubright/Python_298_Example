
result = []

while True:
    score = eval(input())
    check = input()

    if score >= 60:
        result.append('pass')
    else:
        result.append('fail')

    if check != 'y':
        break

for e in result:
    print(e)
