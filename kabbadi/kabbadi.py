


n = int(input())
l = []
l = [int(item) for item in input().split()]




tedad_vajed_sharayet = 0
for i in range(0 , len(l)) :
    if l[i] == 0 or l[i] == 1 or l [i] == 2 :
        tedad_vajed_sharayet += 1

print (tedad_vajed_sharayet // 3)