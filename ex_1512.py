input_str = input()
N, K = [int(e) for e in input_str.split(' ') if e != '']

N_sub_str = input()
N_sub = [int(e) for e in N_sub_str.split(' ') if e != '']

# print(N, K)
# print(N_sub)

result = 0

for i in range(N):
    result += (N_sub[i]//K)

print(result*K)
