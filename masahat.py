from random import randint
name = str (input('what is your name? '))
print('hello' , name)
computer_number = int (randint(1 , 99))
print('I selected his number')
my_guess = int (input('what is your guess? '))
while my_guess != computer_number :
    if my_guess > computer_number :
        print('Mine is smaller')
    elif my_guess < computer_number :
        print('Mine is larger')
    my_guess = int (input('what is your guess? '))

    
print('wooooow!!!you did it' , name)
