n = int(input())
bottle_cap = n
free_drink = 0
while bottle_cap >= 4:
    free_drink = 0
    free_drink = free_drink+bottle_cap//4
    bottle_cap %= 4
    bottle_cap += free_drink
    n += free_drink
    # print(bottle_cap, n, free_drink)
    # input()

if bottle_cap == 3:
    n += 1

# total = n+drink_free

print(n)
