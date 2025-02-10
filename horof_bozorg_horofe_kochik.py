alphabet_bozorg= ['A' , 'B' , 'C' , 'D' , 'E' , 'F' ,'G' , 'H' , 'I' , 'J' ,'K' ,'L'
'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
my_input = input()
count_bozorg = 0
count_kochik = 0
for i in range(0 , len(my_input)):
    if my_input[i] in alphabet_bozorg :
        count_bozorg += 1
    else :
        count_kochik += 1

if count_bozorg > count_kochik :
    print(my_input.upper())
else :
    print(my_input.lower())


