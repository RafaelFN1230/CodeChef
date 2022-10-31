'''
Problem
Chef has an array A of length N. In one operation, Chef can:

Choose any subarray [L,R] (1≤L≤R≤N);
Add 1 to A_L, subtract 1 from A_L+1, add 11 to A_L+2, subtract 1 from A_L+3 and so on, till A_R.
Chef performed Q such operations where the i^ith operation was performed on the subarray [L_i, R_i].
Determine the final sum of the array after these Q operations.

Note that a subarray is formed by deleting some (possibly zero) elements from the beginning and some 
(possibly zero) elements from the end of the array.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two integers N, Q, number of elements and the number of queries.
The next line contains NN space-separated integers A_1, A_2, ... A_NA - denoting the array AA.
The next Q lines contains two space-separated integers with i^ith line containing L_i, R_i.

Output Format
For each test case, output the final sum of the array after performing all the QQ operations.
'''