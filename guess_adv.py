import random

lower_limit = 1
upper_limit = 100
ans = random.randint(lower_limit+1, upper_limit-1)
cnt1 = 0

print('ans:', ans)

while True:
    guess = eval(input('猜數字範圍{} < ? < {} :'.format(lower_limit, upper_limit)))
    cnt1 += 1
    if guess == ans:
        print('賓果! 猜對了，答案是 {}'.format(guess))
        print('\n總共猜了', cnt1, '次!')
        break
    elif guess > upper_limit or guess < lower_limit:
        print('超過範圍!', end='')
        print('您猜了', cnt1, '次')

    elif guess < ans:
        lower_limit = guess
        print('再大一點!! 您猜了', cnt1, '次')
    elif guess > ans:
        upper_limit = guess
        print('再小一點!! 您猜了', cnt1, '次')
    print()
