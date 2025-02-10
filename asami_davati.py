def capitalization(x) :
    capitalized = x.capitalize()
    return capitalized

my_input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(my_input)):
    my_input[i] = input()
    my_input[i] = capitalization(my_input[i])

for word in my_input:
    print (word)

