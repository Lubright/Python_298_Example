
input_str = input()
input_list = input_str.split(' ')
L = eval(input_list[0])
S = eval(input_list[1])

cnt1 = 0

while True:
    temp = L-S
    if temp == 0:
        break
    elif temp > 0:
        S += 5
        cnt1 += 1
    else:
        S -= 2
        cnt1 += 1

print(cnt1)
