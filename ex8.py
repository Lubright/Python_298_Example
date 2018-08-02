import math


def circum(r):
    return 2*r*math.pi


def area(r):
    return (r**2)*math.pi


r = float(input())

print('圓周率', math.pi)
print('半徑', int(r))
print('圓周長', circum(r))
print('圓面積', area(r))
