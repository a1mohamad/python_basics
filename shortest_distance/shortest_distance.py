
loc =[0 , 0 , 0]
for i in range(0 , 3):
    loc[i] = float(input())
    
loc.sort()
d_max = loc.pop()
d_vasati = loc.pop()
d_min = loc.pop()
q = int(d_max - d_min)
print(q)