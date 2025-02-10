
n = int(input())
my_input =[]
sum_data = []
for i in range(0 , n):
    my_input =[int(item) for item in input().split()]
    my_data = [my_input]
    sum_data = sum_data + my_data


classify = 0
for i in range(0 , n):
    for j in range(0 , n):
        if sum_data[i][0] > sum_data[j][0] and sum_data[i][1] < sum_data[j][1] :
            classify = 1

if classify == 1 :
    print('happy irsa')
elif classify == 0 :
    print('poor irsa')
