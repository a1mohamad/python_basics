
string = input()
output = ''
for i in range(0 , len(string)):
        if vorodi[i] == '1' :
            output = output + string[i] + '+'

for j in range(0 , len(string)):
        if string[j] == '2':
            output += string[j] + '+'

for k in range(0 , len(string)):
        if string[k] == '3' :
            output += string[k] + '+'

output = output[:-1]

print(output)