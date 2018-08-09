
score_data = []
temp_list = []

for i in range(5):
    line = input()
    temp_list = [eval(e) for e in line.split(' ') if e != '']
    score_data.append(temp_list[:])


# print(score_data)

sum_list = []
avg_list = []

for i, score_list in enumerate(score_data, 1):
    print('student', i)
    temp_sum = 0
    for j, score in enumerate(score_list, 1):
        print(' {}: {}'.format(j, score))
        temp_sum += score
    sum_list.append(temp_sum)
    avg_list.append(temp_sum/len(score_list))
    print(' sum: {}'.format(temp_sum))
    print(' avg: {:.2f}'.format(avg_list[i-1]))

total_score = sum(sum_list)
avg = sum(avg_list)/len(avg_list)


def findMaxIndex(list1):
    temp_list = list(enumerate(list1, 1))

    temp_list.sort(key=lambda x: x[1], reverse=True)

    return temp_list[0][0], temp_list[0][1]


print('total: {}, avg: {:.2f}'.format(total_score, avg))
print('highest avg: student {}: {:.2f}'.format(*findMaxIndex(avg_list)))
