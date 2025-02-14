
        #define function start

def divisor_counter(number) :
    c= 0
    for i in range(1 , number) :
        if (number % i == 0) :
         c += 1
    count = c + 1
    return count

        #define function end

        #insert two simple input start
number_1 = int (input())
number_2 = int (input())
        #insert two simple function end

        #compring inputs for perpuse start
if divisor_counter(number_1) > divisor_counter(number_2) :
    most_one = number_1
elif divisor_counter(number_2) > divisor_counter(number_1) :
    most_one = number_2
elif divisor_counter(number_1) == divisor_counter(number_2) and number_1 > number_2 :
    most_one = number_1
elif divisor_counter(number_1) == divisor_counter(number_2) and number_2 > number_1 :
    most_one = number_2
        #comparing inputs for perpuse end


        #loop to continue comparing start
for number_3 in range(1 , 18) :
    number_3 = int (input())
    if divisor_counter(number_3) > divisor_counter(most_one) :
        most_one = number_3
    elif divisor_counter(vorodi_3) == divisor_counter(most_one) and number_3 > most_one :
        most_one = number_3
        #loop to continue comparing start

                        #result

print(most_one,divisor_counter(most_one))

