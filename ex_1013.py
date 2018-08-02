line = input()
check = line.find(' ')
# print(check)

if check == -1:  # 沒有空白，繼續輸入
    num2 = eval(input())
    op = input()
    num1 = eval(line)
else:
    list_line = line.split(' ')
    num1 = eval(list_line[0])
    num2 = eval(list_line[2])
    op = list_line[1]

result = 0

if op == '+':
    result = num1+num2
elif op == '-':
    result = num1-num2
elif op == '*':
    result = num1*num2
elif op == '/':
    result = num1/num2

print('{:.2f} {} {:.2f} = {:.2f}'.format(num1, op, num2, result))
