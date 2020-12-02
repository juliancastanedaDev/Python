'''
program calculates the least common multiple of two numbers x and y.

'''
count = True
x = int(input('ingrese primer numero para calcular m.c.m\n'))
y = int(input('ingrese segundo numero para calcular m.c.m\n'))
z = 1
while count:
    if (z % x == 0) and (z % y == 0):
        print('{} es el l.c.m de los numero {} y {}'.format(z, x, y))
        break
    z += 1