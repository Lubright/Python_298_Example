N=int(input())

if 0<N<100000:
    money_str=input()
    money_list=[ int(e) for e in money_str.split(' ') if e!='' and 0<int(e)<=10000 ]
    
    # print(money_list)
    
    K=int(input())
    person_index=input()
    person_list=[ int(e) for e in person_index.split(' ') if e!='' and 0<int(e)<=N ]
    
    # print(person_list)
    person_list.sort(reverse=True)
    money_list_copy=money_list.copy()
    for e in person_list:
        # money_list.remove(money_list_copy[e-1])
        del money_list[e-1]
    
    max_val=max(money_list)
    max_index=0
    while True:
        
        max_index=money_list_copy.index(max_val,max_index)
        if (max_index+1) not in person_list:
            break
        else:
            max_index+=1
    print(sum(money_list))
    print('{} {}'.format(max_index+1,max_val))

else:
    pass