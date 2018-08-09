line = input()
keyword = input()

index = 0

for i in range(line.count(keyword)):
    index = line.find(keyword, index)
    print(index)
    index += 1
