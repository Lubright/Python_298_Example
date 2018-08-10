import math
N=int(input())

if 0<N<100000:
    line=input()
    num_list=[ int(e) for e in line.split(' ') if e!='' and 0<int(e)<=100000 ]
    # print(num_list)
    if N%2==0: # N為偶數
        index1=N//2
        result=math.ceil((num_list[index1-1]+num_list[index1])/2)
    else: # N為基數
        index1=(N+1)//2
        result=num_list[index1-1]
    print(result)
else:
    pass