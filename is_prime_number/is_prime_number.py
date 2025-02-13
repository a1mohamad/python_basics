number = int(input())
c = 0
for d in range(1 , number) :
    if number % d == 0 :
        c = c + 1

if c == 1 :
    print('prime')  
else :
    print('not prime')      