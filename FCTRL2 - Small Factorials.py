'''
You are asked to calculate factorials of some small positive integers.

Input
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, 
each containing a single integer n, 1<=n<=100.

Output
For each integer n given at input, display a line with the value of n!
'''

t=int(input())
a=0
total=0
for x in range(t):
    fac=int(input())
    total=fac
    for y in range(1,fac):
        total*=fac-y
    print(total)
    