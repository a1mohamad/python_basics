vorodi = int(input())
c = 0
for maghsom in range(1 , vorodi) :
    if vorodi % maghsom == 0 :
        c = c + 1

if c == 1 :
    print('prime')  
else :
    print('not prime')      