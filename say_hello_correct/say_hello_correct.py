string = input()
h = string.find('h')
e = string.find('e' , h + 1)
l_1 = string.find('l' , e + 1)
l_2 = string.find('l' , l_1 + 1)
o = string.find('o' , l_2 + 1)


if o > l_2 > l_1 > e > h :
    print('YES')
else :
    print('NO')