One day, Katlin and Jennifer were discussing the price of laptops and their quality. Katlin guesses that 
the more expensive a laptop is, the better its quality. But Jennifer claims that she can find 2 laptops 
where the first one is cheaper than the second one but its quality is higher than the second one, and 
she can disprove Katlin's guess. Now you have to write a program to help Jennifer check her claim.

You are given the specifications of n laptops. The first line of input contains the number n, which 
indicates the number of laptops. Each of the next n lines contains two numbers, the first number 
indicating the price of the laptop and the second number indicating the quality of that laptop. If you 
can find two laptops that meet the conditions stated by Jennifer, print happy jennifer ; otherwise, print 
poor jennifer (please note that all letters are written in lowercase.)

for example:

input:

2
1 10
7 3

output:

happy jennifer

In the sample input, the first laptop has a price of 1 and a quality of 10 (the higher the number, the higher 
the quality). The second laptop has a price of 7 and a quality of 3. So, Jennifer has managed to find two 
laptops where, although the price of the second is higher than the price of the first, the quality of the second 
is lower than the quality of the first.

input:

5
1 5
7 9
5 6
20 30

output:

poor jennifer

