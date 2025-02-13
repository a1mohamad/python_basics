win_number = 0
points = 0
for point in range(1 , 31) :
    point = int(input())
    points += point
    if point == 3 :
        win_number += 1

print (points ,'', win_number)
   
    
