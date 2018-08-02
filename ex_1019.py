h = eval(input())
weight = eval(input())

result = weight/((h/100)**2)
print(round(result, 2))

if result < 18.5:
    print('Underweight')
elif result < 24:
    print('Normal')
elif result < 27:
    print('Overweight')
elif result < 30:
    print('Obese Class I')
elif result < 35:
    print('Obese Class II')
else:
    print('Obese Class III')
