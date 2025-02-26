In this project, you need to write a program that reads the scores of different people from 
a csv file, performs the following calculations on the scores, and saves the resulting values ​​
in a file.
In this project, you have to implement 5 different tasks.

1-Calculate the average of each person and save it along with the name of each person, the 
output order of the names must be exactly the same as the order of the input file.

2-Save the averages in ascending order along with the name of each person.

3-Save the top three GPA's with each person's name.

4-Save the bottom three GPA's without each person's name.

5-Calculate and save the average of the GPA's.

-----------------------------------------------------------------------------------------------

Example of the content of a csv file:

mandana,5,7,3,15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina,19,10,19,6,8,14,3
sara,0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
ali,1,9
sarvin,0,16,16,13,19,2,17,8

-----------------------------------------------------------------------------------------------

Task output First:

mandana,7.5
hamid,6.0666666666666666
sina,11.285714285714286
sara,9.75
soheila,7.833333333333333
ali,5.0
sarvin,11.375

-----------------------------------------------------------------------------------------------
Output of the second task:

ali,5.0
hamid,6.06666666666666
mandana,7.5
soheila,7.83333333333333
sara,9.75
sina,11.285714285714286
sarvin,11.375

-----------------------------------------------------------------------------------------------

Output of the task Third:

sarvin,11.375

sina,11.285714285714286

sara,9.75

-----------------------------------------------------------------------------------------------

Output of the fourth task:

5.0
6.06666666666666
7.5

-----------------------------------------------------------------------------------------------

Output of the fifth task:

8.401530612244898

-----------------------------------------------------------------------------------------------

Note: Please note that in each stage, if several people have the same GPA, the output order 
should be based on the alphabet, for example:

hossein 16.5
mona 16.5