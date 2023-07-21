#Math Problem

#Burgers
# cook your dish here
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    if N<=M:
        print(0)
    else:
        print(N-M)
    