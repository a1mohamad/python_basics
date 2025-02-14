


string = input()
changes = string.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
output = ''
for i in range(0 , len(changes)):
    output = output + '.' + changes[i]

print(output)