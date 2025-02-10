print ('Hello it is a number guess game')
print ('please pick ur number')
from random import randrange
karane_paeen = 1
karane_bala = 99
computer_guess = randrange (karane_paeen, karane_bala)
print (computer_guess)
moghayese = input('bzozrgtare ya kochiktare? ')
while moghayese != 'd' :
    if moghayese == 'b' :
        karane_paeen = computer_guess
        computer_guess = randrange (karane_paeen , karane_bala)
        print(computer_guess)
    elif moghayese == 'k' :
        karane_bala = computer_guess
        computer_guess = randrange (karane_paeen ,karane_bala)
        print(computer_guess)
    moghayese = input('bozorgtare ya kochiktare? ')

print("woooow!!!that's correct")            
