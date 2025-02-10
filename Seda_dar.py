


vorodi = input()
taghirat = vorodi.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
output = ''
for i in range(0 , len(taghirat)):
    output = output + '.' + taghirat[i]

print(output)