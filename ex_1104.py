
# coding: utf-8

# In[39]:

number_en='one two three four five six seven eight nine'
number_en=number_en.split(' ')
number_en=[ e for e in number_en if e!='' ]
number_en_2=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
number_en_3={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}


# In[40]:

import math
def group(list1,g=3):
    result=[]
    len1=len(list1)
    n=math.ceil(len1/3)
    
    for i in range(n):
        start=len1-(3*(i+1))
        end=len1-3*i
        if start<0:
            start=0
        temp=list1[start:end]
        result.append((temp,i))
    return result

def show_money_en(str1):
    len1=len(str1)
    temp=0
    
    for v in str1:
        if v=='0':
            len1-=1
            continue
        if len1==3:
            print('{} hundred '.format(number_en[int(v)-1]),end='')
        elif len1==2:
            if int(v)>1:
                print('{} '.format(number_en_2[int(v)-1]),end='')
            else:
                temp=(int(v))*10
        elif len1==1:
            if temp==0:
                print('{} '.format(number_en[int(v)-1]),end='')
            else:
                temp=temp+int(v)
                print('{} '.format(number_en_3[temp]),end='')
        len1-=1
    
#         print(temp)
# group([1,2,3,4,5,6,7])
# result=group('1234567')
# print(result)
# show_money_en('111')


# In[41]:

m=input()

if 1<=eval(m)<=9999999:
    len_m=len(m)
    result_g=group(m,3)
    len1=len(result_g)
    result_g.reverse()
#     print(result_g)
    for g in result_g:
        if g[1]==2:
            show_money_en(g[0])
            print('million ',end='')
        elif g[1]==1:
            show_money_en(g[0])
            print('thousand ',end='')
        elif g[1]==0:
            show_money_en(g[0])
            if int(m)>1:
                print('dollars',end='')
            else:
                print('dollar',end='')
    
else:
    print('out of range')


# In[ ]:



