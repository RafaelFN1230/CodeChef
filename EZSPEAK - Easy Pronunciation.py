'''
Problem
Words that contain many consecutive consonants, like "schtschurowskia", are generally considered somewhat hard to pronounce.

We say that a word is hard to pronounce if it contains 44 or more consonants in a row; otherwise it is easy to pronounce. For example, "apple" and "polish" are easy to pronounce, but "schtschurowskia" is hard to pronounce.

You are given a string SS consisting of NN lowercase Latin characters. Determine whether it is easy to pronounce or not based on the rule above — print YES if it is easy to pronounce and NO otherwise.

For the purposes of this problem, the vowels are the characters \{a, e, i, o, u\}{a,e,i,o,u} and the consonants are the other 2121 characters.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains a single integer NN, the length of string SS.
The second line of each test case contains the string SS.
Output Format
For each test case, output on a new line the answer — YES if SS is easy to pronounce, and NO otherwise.

Each character of the output may be printed in either uppercase or lowercase. For example, the strings YES, yeS, yes, and YeS will all be treated as identical.

Constraints
1 \leq T \leq 1001≤T≤100
1 \leq N \leq 1001≤N≤100
SS contains only lowercase Latin characters, i.e, the characters \{a, b, c, \ldots, z\}{a,b,c,…,z}
Sample 1:
Input
Output
5
5
apple
15
schtschurowskia
6
polish
5
tryst
3
cry
YES
NO
YES
NO
YES
Explanation:
Test case 11: "\text{apple}apple" doesn't have 44 or move consecutive consonants, which makes it easy to pronounce.

Test case 22: "\text{\textcolor{red}{schtsch}urowskia}schtschurowskia" has 77 consecutive consonants, which makes it hard to pronounce.

Test case 33: \text{polish}polish doesn't contain 44 or more consecutive consonants, so it's easy to pronounce.

Test case 44: \text{\textcolor{red}{tryst}}tryst contains 55 consecutive consonants, making it hard to pronounce.

Test case 55: \text{cry}cry doesn't contain any vowels, but its length is less than 44 so it's still easy to pronounce.

'''

