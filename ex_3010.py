n = int(input())
check = True
for i in range(2, n):
    if n % i == 0:
        check = False

if check:
    print('{} is prime'.format(n))
else:
    print('{} is not prime'.format(n))
