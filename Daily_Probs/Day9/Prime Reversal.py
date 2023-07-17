'''You are given two binary strings A and B, each of length N.
You can perform the following operation on string A any number of times:

Select a prime number X.Choose any substring of string A having length X and reverse the substring.
Determine whether you can make the string A equal to B using any (possibly zero) number of operations.

A substring is obtained by deleting some (possibly zero) elements
from the beginning and some (possibly zero) elements from the end of the string.

2 -YES
00
00

4 -NO
1001
0111

5 - YES
11000
10010

5 -NO
11000
11010
'''



# cook your dish here
T=int(input("T:"))
for i in range(T):
    N=int(input("N:"))
    A=input("A:")
    B=input("B:")
    m=0
    for x in A:
       m+=int(x)
    n=0
    for y in B:
        n+=int(y)
    if m==n:
        print("YES")
    else:
        print("NO")
        