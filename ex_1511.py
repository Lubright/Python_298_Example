input_str = input()
N, X, Y = input_str.split(' ')
N = int(N)
X = int(X)
Y = int(Y)

init_temperature = 20

# print(N, X, Y)


N -= 1
m = N//2
result = init_temperature

for i in range(m):
    result += (X-Y)
result += X

print(result)
