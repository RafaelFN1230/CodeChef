'''
Chef has a binary string SS of length NN.

In one operation, Chef can:

Select two indices i and j and flip S_i and S_j. 
(i.e. change 0 to 1 and 1 to 0)
For example, if S = 10010 and chef applys operation on i = 1 and j = 3 then:
10010 => 00110

Find if it is possible to convert S to a palindrome by applying the above operation any number of times.

Note: A string is called a palindrome if it reads the same backwards and forwards,
for e.g. 10001 and 0110 are palindromic strings.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the length of the binary string S.
The second line of each test case contains a binary string S of length N containing 0s and 1s only.
Output Format
For each test case, output YES if it is possible to convert S to a palindrome. Otherwise, output NO.

You can print each character of the string in uppercase or lowercase. 
For example, the strings YES, yes, Yes, and yEs are all considered the same.
'''
T=int(input())

for a in range (T):
    N=int(input())
    S=list()
    S=list(int(input()))

    for b in range(N):
        if (b>1):
            while (S[b]!=S[N-1]):
                ref=0
                ref=S[N-b]
                S[N-b]=S[b+1]
                S[b+1]=ref
                print(S)
        else:
            while (S[b]!=S[N-1]):
                ref=0
                ref=S[N-b]
                S[N-b]=S[b+1]
                S[b+1]=ref
                print(S)

