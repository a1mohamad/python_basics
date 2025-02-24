print ('Hello it is a number guess game')
print ('please pick your number')
from random import randrange
lower_b = 1
higher_b = 99
computer_guess = randrange (karane_paeen, karane_bala)
print (computer_guess)
compare_tool = input('bigger or smaller? ')
while compare_tool != 'd' :
    if compare_tool == 'b' :
        lower_b = computer_guess
        computer_guess = randrange (lower_b , higher_b)
        print(computer_guess)
    elif compare_tool == 's' :
        higher_b = computer_guess
        computer_guess = randrange (lower_b ,higher_b)
        print(computer_guess)
    compare_tool = input('bigger or smaller? ')

print("woooow!!!that's correct")            
