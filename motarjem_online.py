from collections import OrderedDict
n = int(input())
source =[]
for i in range(n) :
    source.append(0)
for i in range(n) :
    source[i] = [item for item in input().split()]

source = OrderedDict(source)

string = str(input())
list1 = string.split()
list2=[]
for word in list1:
    if word in list(source.keys()) :
        word = source[word]
        list2.append(word)
    else :
        list2.append(word)

output = ' '.join(list2)
print(output)