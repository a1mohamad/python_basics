string = input().lower()
palindrome = 0
for i in range(0 , len(string)) :
    if string[i] == string[-i-1] :
        palindrome += 1

if palindrome == len(string) :
    print('palindrome')
else :
    print('not palindrome')
    