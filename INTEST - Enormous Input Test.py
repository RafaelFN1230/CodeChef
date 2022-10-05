'''
Problem
The purpose of this problem is to verify whether the method you are using to read input data is 
sufficiently fast to handle problems branded with the enormous Input/Output warning. 
You are expected to be able to process at least 2.5MB of input data per second at runtime.

Input
The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one 
positive integer ti, not greater than 109, each.

Output
Write a single integer to output, denoting how many integers ti are divisible by k.
'''

(a, b) = map(int, input().split(' '))

cont = 0

for i in range(a):
	x = int(input())
	if x % b == 0:
		cont += 1

print(cont)	