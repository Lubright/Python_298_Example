c = input()

if c[0].islower():
    print('{} is a lowercase letter.\nswap to capital letter {}.'.format(
        c[0], c[0].upper()))
elif c[0].isupper():
    print('{} is a capital letter.'.format(c[0]))
elif c[0].isdigit():
    print('{} is a number.'.format(c[0]))
else:
    print('{} is a punctuation.'.format(c[0]))
