
'''
Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

Chef's video has
N frames initially. The value of the 
i 
th
  frame is
A i
 . Chef can do the following type of operation any number of times:'''

# cook your dish here

T=int(input())
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    s=1
    for x in range(0,N-1):
        if a[x]!=a[x+1]:
            s+=1
    print(s)  