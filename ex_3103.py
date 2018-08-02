import random

lower_limit = 1
upper_limit = 100
ans = eval(input())
cnt1 = 0

# print('ans:', ans)

while True:
    guess = eval(input('{} < ? < {}\n'.format(lower_limit, upper_limit)))
    cnt1 += 1
    if guess == ans:
        print('bingo answer is {}'.format(guess))
        break

    elif guess < ans:
        lower_limit = guess
        print('wrong answer, guess larger')
    elif guess > ans:
        upper_limit = guess
        print('wrong answer, guess smaller')
