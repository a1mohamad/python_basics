person1 = int (input())
person2 = int (input())
if person1 > person2 :
    older = person1
    co_older = person2
else :
    older = person2
    co_older = person1
person3 = int (input())
while person3 != -1 :
    person3 = int(input())
    if person3 > older :
        older = person3
    elif co_older < person3 < older :
        co_older = person3

print(older ,'', co_older)                
