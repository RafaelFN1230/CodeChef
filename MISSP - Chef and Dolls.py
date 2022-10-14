'''
Chef is fan of pairs and he likes all things that come in pairs. 
He even has a doll collection in which the dolls come in pairs. 
One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!!

Help chef find which type of doll is missing..

Input
The first line contains an integer T, the number of test cases.
The first line of each test case contains an integer N, the number of dolls.
The next N lines are the types of dolls that are left.

Output
For each test case, display the type of doll that doesn't have a pair, in a new line.
'''

t=int(input())

for a in range (t):
    x=[]
    N=int(input())
    cont=0
    for b in range (N):
        y=int(input())
        x.append(y)
    x.sort()
    if(x[0]!=x[1]):
        print(x[0])
    else:
        while (cont!=N):
            if (cont+1<N):
                if (x[cont]==x[cont+1]):
                    cont+=2
                elif (x[cont]!=x[cont+1]):
                    print(x[cont])
                    cont=N
            else:
                print(x[N-1])
                cont=N
'''
        if (x[0]!=x[1]):
            print(x[0])
        elif (x[c]!=x[c+1] and x[c+1]!=x[c+2]):
            print(c)

1,1,2,2,3

1,2,2,3,3

1,1,2,3,3
'''