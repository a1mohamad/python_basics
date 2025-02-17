string = input()
string = string.upper()
AB = string.find('AB')
if AB != -1 :
    string = string.replace('AB' , '')
    BA = string.find('BA')
    if BA != -1 :
        print('YES')
    else :
        print('NO')
else :
    print('NO')


