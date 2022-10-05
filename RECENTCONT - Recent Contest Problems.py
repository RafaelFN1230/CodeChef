'''
Problem
CodeChef recently revamped its practice page to make it easier for users to identify 
the next problems they should solve by introducing some new features:

Recent Contest Problems - Contains only problems from the last 2 contests
Separate Un-Attempted, Attempted, and All tabs
Problem Difficulty Rating - The Recommended dropdown menu has various difficulty ranges 
so that you can attempt the problems most suited to your experience
Popular Topics and Tags
Chef has been participating regularly in rated contests but missed the last two contests due 
to his college exams. He now wants to solve them and so he visits the practice page to view these problems.

Given a list of NN contest codes, where each contest code is either START38 or LTIME108, 
help Chef count how many problems were featured in each of the contests.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of two lines of input.
First line of input contains the total count of problems that appeared in the two recent contests - NN.
Second line of input contains the list of NN contest codes. Each code is either START38 or LTIME108, 
to which each problem belongs.

Output Format
For each test case, output two integers in a single new line - the first integer should be 
the number of problems in START38, and the second integer should be the number of problems in LTIME108.
'''

t=int(input())

for x in range(t):
    cont_x=0
    cont_y=0
    n=int(input())
    b=input()
    a=b.split()
    for y in a:
        if (y=="START38"):
            cont_x+=1
        elif (y=="LTIME108"):
            cont_y+=1
    print(cont_x, cont_y)
