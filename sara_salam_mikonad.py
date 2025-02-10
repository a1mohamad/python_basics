vorodi = input()
h = vorodi.find('h')
e = vorodi.find('e' , h + 1)
l_1 = vorodi.find('l' , e + 1)
l_2 = vorodi.find('l' , l_1 + 1)
o = vorodi.find('o' , l_2 + 1)


if o > l_2 > l_1 > e > h :
    print('YES')
else :
    print('NO')