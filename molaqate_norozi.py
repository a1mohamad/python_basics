
vorodi =[0 , 0 , 0]
for i in range(0 , 3):
    vorodi[i] = float(input())
    
vorodi.sort()
a_max = vorodi.pop()
a_vasati = vorodi.pop()
a_min = vorodi.pop()
q = a_max - a_min

if q == int(q) :
    print(int(q))
else :
    print(q)