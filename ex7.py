import math


def circum(r):
    return 2*r*math.pi


def area(r):
    return (r**2)*math.pi


r = 100

print('圓周率', math.pi)
print('半徑', r)
print('圓周長', circum(r))
print('圓面積', area(r))
