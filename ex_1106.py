ans = input()


def check_func(ans, guess):
    cntA = 0
    cntB = 0
    if len(guess) != len(ans):
        return 0, 0
    else:
        for i, val in enumerate(guess):
            if val in ans:
                if guess[i] == ans[i]:
                    cntA += 1
                else:
                    cntB += 1
    return cntA, cntB


while True:
    guess = input()
    if guess == ans:
        print('4A0B\nYou Win!')
        break
    result = check_func(ans, guess)
    print('{}A{}B'.format(*result))
