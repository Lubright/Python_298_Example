op = int(input())
threshold = 0


def isPass(score):
    if 0 <= score <= 100:
        if score >= threshold:
            print('pass')
        else:
            print('fail')
    else:
        print('score error')


if op == 1:
    threshold = 60
    score = int(input())
    isPass(score)

elif op == 2:
    threshold = 70
    score = int(input())
    isPass(score)
else:
    print('roll error')
