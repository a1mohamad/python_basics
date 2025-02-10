my_input = input().lower()
mosavi = 0
for i in range(0 , len(my_input)) :
    if my_input[i] == my_input[-i-1] :
        mosavi += 1

if mosavi == len(my_input) :
    print('palindrome')
else :
    print('not palindrome')
    