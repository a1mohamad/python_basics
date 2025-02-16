alphabet_capital= ['A' , 'B' , 'C' , 'D' , 'E' , 'F' ,'G' , 'H' , 'I' , 'J' ,'K' ,'L'
'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
string = str(input())
count_capital = 0
count_small = 0
for i in range(0 , len(string)):
    if string[i] in alphabet_capital :
        count_capital += 1
    else :
        count_small += 1

if count_capital > count_small :
    print(string.upper())
else :
    print(string.lower())


