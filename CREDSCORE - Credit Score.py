'''
Problem
To access CRED programs, one needs to have a credit score of 750750 or more.
Given that the present credit score is XX, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output YES, otherwise output NO.

Input Format
The first and only line of input contains a single integer XX, the credit score.

Output Format
Print YES if it is possible to access CRED programs. Otherwise, print NO.

You may print each character of the string in uppercase or lowercase (for example, 
the strings YeS, yEs,yes and YES will all be treated as identical).

Constraints
0 \leq X \leq 10000≤X≤1000
Subtasks
Subtask 1 (100 points): Original constraints.
'''

cred=int(input())

if (cred>=750):
    print("YES")
elif (cred<750):
    print("NO")