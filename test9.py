import time

with open('./test_123.txt', 'rt', encoding='utf-8') as fin:
    line=fin.read()

line_list=[ e for e in line.split('\n') if e!='']
# print(len(line_list))
start=time.clock()
# print(line_list[0])
# money_list=[ int(e) for e in line_list[1].split(' ') if e!='' and 0<int(e)<=10000 ]
# print(len(money_list))
# end=time.clock()
# print((end-start)*1000)


N=int(line_list[0])

if 0<N<100000:
    line=line_list[1]
    num_list=[ int(e) for e in line.split(' ') if e!='' and 0<int(e)<=100000 ]
    num_list.sort()
    print(len(num_list))
    # print(num_list)
    if N%2==0: # N為偶數
        index1=N//2
        import math
        # print(num_list[8610])
        # print(num_list[8611])
        result=math.ceil((num_list[index1-1]+num_list[index1])/2)
    else: # N為基數
        index1=(N+1)//2
        result=num_list[index1-1]
    print(result)
else:
    pass

end=time.clock()
print((end-start)*1000)