my_input = input()
my_input = my_input.upper()
x = my_input.find('AB')
if x != -1 :
    my_input = my_input.replace('AB' , '')
    y = my_input.find('BA')
    if y != -1 :
        print('YES')
    else :
        print('NO')
else :
    print('NO')


