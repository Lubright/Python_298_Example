import random

ans = random.choice(range(1, 6))
print('ans:', ans)

val = eval(input('請猜一1~5的號碼:'))

if val == ans:
    print('你猜對了!答案正是', val)
else:
    print('你猜錯了喔~其實是', ans)
