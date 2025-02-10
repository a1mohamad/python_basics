
vorodi = input()
output = ''
for i in range(0 , len(vorodi)):
        if vorodi[i] == '1' :
            output = output + vorodi[i] + '+'

for j in range(0 , len(vorodi)):
        if vorodi[j] == '2':
            output += vorodi[j] + '+'

for k in range(0 , len(vorodi)):
        if vorodi[k] == '3' :
            output += vorodi[k] + '+'

output = output[:-1]

print(output)