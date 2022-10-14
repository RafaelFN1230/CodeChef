'''
You have N cards placed in front of you on the table. 
The i^{th} card has the number A_i written on it.

In one move, you can remove any one card from the remaining cards on the table.

Find the minimum number of moves required so that all the cards remaining 
on the table have the same number written on them.

Input Format
The first line contains a single integer T — the number of test cases. 
Then the test cases follow.
The first line of each test case contains an integer N — the number of cards on the table.
The second line of each test case contains N space-separated integers A_1, A_2,..., A_N

Output Format
For each test case, output the minimum number of moves required so that 
all the cards remaining on the table have the same number written on them.

Sample 1:
Input
3
5
1 1 2 2 3
4
8 8 8 8
6
5 6 7 8 9 10

Output
3
0
5
Explanation:
Test case 1: The minimum number of moves required such that 
all remaining cards have same values is 3:

Move 1: Remove a card with number 1. Remaining cards are [1, 2, 2, 3].
Move 2: Remove a card with number 1. Remaining cards are [2, 2, 3].
Move 3: Remove a card with number 3. Remaining cards are [2, 2].

Test case 2: All cards have the same number initially. Thus, no moves are required.

Test case 33: The minimum number of moves required such that all remaining cards have same values is 55:

Move 1: Remove a card with number 5. Remaining cards are [6, 7, 8, 9, 10].
Move 2: Remove a card with number 6. Remaining cards are [7, 8, 9, 10].
Move 3: Remove a card with number 7. Remaining cards are [8, 9, 10].
Move 4: Remove a card with number 8. Remaining cards are [9, 10].
Move 5: Remove a card with number 9. Remaining cards are [10].
'''

t=int(input())

for a in range (t):
    N=int(input())
    cards=[]
    cards=list(map(int,input().split()))
    cards.sort()
    n_card=0
    for b in cards:
        x=cards.count(b)
        if (x>n_card):
            n_card=x
    print(N-n_card)
