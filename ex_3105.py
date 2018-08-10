set_math_pass={'柯南','灰原','步美','美環','光彦'}
set_english_pass={'柯南','灰原','丸尾','野口','步美'}

list1=list(set_math_pass-set_english_pass)
list1.sort()
list2=list(set_english_pass-set_math_pass)
list2.sort()
list3=list(set_english_pass&set_math_pass)
list3.sort()

print(list1)
print(list2)
print(list3)
