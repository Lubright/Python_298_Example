import math

score = eval(input())

result = math.sqrt(score)*10

print('Original: {:.2f}'.format(score))
print('Adjusted: {:.2f}({:+d})'.format(result, int(round(result-score))))
