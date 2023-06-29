#Palindrome Problem
# cook your dish here
T=int(input())
for i in range(T):
    N=input()
    if N[::-1]==N:
        print("wins")
    else:
        print("loses")
        