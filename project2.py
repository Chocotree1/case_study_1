a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('Triangle does not exist')
elif (a != b) and (a != c) and (b != c):
    print('versatile triangle')
elif a == b == c:
    print('equilateral triangle')
else:
    print('isosceles triangle')