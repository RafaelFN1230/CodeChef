'''
Problem
Most programmers will tell you that one of the ways to improve your performance in 
competitive programming is to practice a lot of problems.

Our Chef took the above advice very seriously and decided to set a target for himself.

Chef decides to solve at least 1010 problems every week for 44 weeks.
Given the number of problems he actually solved in each week over 44 weeks as P_1, P_2, P_3,P_4,
output the number of weeks in which Chef met his target.

Input Format
There is a single line of input, with 44 integers P_1, P_2, P_3,P_4. 
These are the number of problems solved by Chef in each of the 44 weeks.

Output Format
Output a single integer in a single line - the number of weeks in which Chef solved at least 1010 problems.

Constraints
1 ≤ P_1, P_2, P_3, P_4 ≤ 100 
'''

(a, b, c, d) = map(int, input().split(' '))
cont=0

if (a>=10):
    cont+=1
if (b>=10):
    cont+=1
if (c>=10):
    cont+=1
if (d>=10):
    cont+=1

print(cont)