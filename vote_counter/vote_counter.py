from collections import OrderedDict

n = int(input())
country_names =[]
for i in range(n):
    country_names.append(input())
    country_names.sort()


counter = OrderedDict()
for country in country_names :
    counter[country] = counter.get(country, 0) + 1


for this_one in list(counter.keys()):
    print(this_one, counter[this_one])




    
    
