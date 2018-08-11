line = input()

word_list = [e for e in line.split(';') if e != '']

word_list.reverse()

for i, e in enumerate(word_list):
    if i == len(word_list)-1:
        print(e[::-1])
    else:
        print(e[::-1], end=' ')
