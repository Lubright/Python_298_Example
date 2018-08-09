tax_table_list = [[540000, 5, 0],
                  [1210000, 12, 37800],
                  [2420000, 20, 134600],
                  [4530000, 30, 376600],
                  [10310000, 40, 829600],
                  [10310001, 45, 1345100]]

len1 = len(tax_table_list)

m = eval(input())
index = 0

for i, val in enumerate(tax_table_list):
    if i == (len1-1):
        index = i
        break
    if m <= val[0]:
        index = i
        break


J = tax_table_list[index][1]
K = m*J//100
L = tax_table_list[index][2]
M = K-L

print('{}% {} {} {} '.format(J, K, L, M))
