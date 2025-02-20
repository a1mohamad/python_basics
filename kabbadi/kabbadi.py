


n = int(input())
l = []
l = [int(item) for item in input().split()]




eligible_players = 0
for i in range(0 , len(l)) :
    if l[i] == 0 or l[i] == 1 or l [i] == 2 :
        eligible_players += 1

print (eligible_players // 3)