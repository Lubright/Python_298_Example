list1=[]

while True:
    line=input()
    if line=='-1':
        break
    list1.append(eval(line))

print(list1)
list1.sort()
print(list1)

sum1=0

for e in list1:
    if e>30:
        sum1+=e

print(sum1)