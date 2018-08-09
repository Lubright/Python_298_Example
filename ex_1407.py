line = input()
N, K = [eval(e) for e in line.split(' ') if e != '']

# print(N, K)

line = input()
item = [eval(e) for e in line.split(' ') if e != '']

# print(item)

sum1 = 0
cnt1 = 0

for e in item:
    if e <= K:
        cnt1 += 1
        sum1 += e

print(cnt1, sum1)
