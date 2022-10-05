'''
Problem
Ezio can manipulate at most XX number of guards with the apple of eden.

Given that there are YY number of guards, predict if he can safely manipulate all of them.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers XX and YY.
Output Format
For each test case, print YES if it is possible for Ezio to manipulate all the guards. Otherwise, print NO.

You may print each character of the string in uppercase or lowercase (for example, 
the strings YeS, yEs, yes and YES will all be treated as identical).
'''

t=int(input())

for a in range (t):
    (x, y) = map(int, input().split(' '))
    if (x>=y):
        print("YES")
    elif (x<y):
        print("NO")