from collections import defaultdict


def cnt_dict(str1):
    dict1 = defaultdict(int)
    for e in str1:
        dict1[e] += 1
    return dict1


line = input()


def check_func(ans, guess, dict1):
    cntA = 0
    cntB = 0
    # set_ans = set(ans)
    if len(guess) != len(ans):
        return 0, 0
    else:
        for i, val in enumerate(guess):
            if val in ans:
                if guess[i] == ans[i]:
                    cntA += 1
                    dict1[val] -= 1
                elif dict1[val] > 0:
                    cntB += 1
                    dict1[val] -= 1
    return cntA, cntB


ans, guess = [e for e in line.split(' ') if e != '']
dict1 = cnt_dict(ans)
if guess == ans:
    print('4A0B\nYou Win!')
else:
    result = check_func(ans, guess, dict1)
    print('{}A{}B'.format(*result))
