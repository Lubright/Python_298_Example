n = eval(input())
number_ch = '壹,貳,參,肆,伍,陸,柒,捌,玖'
number_ch = number_ch.split(',')
# print(number_ch)

if 1 <= n <= 99999:
    n_str = str(n)
    len1 = len(n_str)
    for v in n_str:
        if v == '0':
            len1 -= 1
            continue
        if len1 == 5:
            print('{}萬'.format(number_ch[int(v)-1]), end='')
        elif len1 == 4:
            print('{}仟'.format(number_ch[int(v)-1]), end='')
        elif len1 == 3:
            print('{}佰'.format(number_ch[int(v)-1]), end='')
        elif len1 == 2:
            print('{}拾'.format(number_ch[int(v)-1]), end='')
        elif len1 == 1:
            print('{}'.format(number_ch[int(v)-1]), end='')

        len1 -= 1
    print('元整')
else:
    print('out of range')
