line = input()

if line.isdigit():
    print('{} is a number.'.format(line))
elif line.isupper():
    print('{} is a capital letter.'.format(line))
elif line.islower():
    print('{} is a lowercase letter.'.format(line))
else:
    print('{} is a punctuation.'.format(line))
