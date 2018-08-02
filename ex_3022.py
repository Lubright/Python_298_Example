input_str = input()
list1 = [eval(e) for e in input_str.split(',') if e != '']

# print(list1)
sum1_odd = 0
sum1_even = 0
sum1_all = 0

for e in list1:
    if e % 2 == 0:
        sum1_even += e
    else:
        sum1_odd += e
    sum1_all += e
    # cnt1 += 1

print(sum1_odd)
print(sum1_even)
print(sum1_all)
