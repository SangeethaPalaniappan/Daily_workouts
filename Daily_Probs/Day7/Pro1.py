# cook your dish here
T=int(input("n:"))
for i in range(T):
    N,K=map(int,input().split())
    N=list(map(int,input().split()))
    count=0
    for i in N:
        if i>K:
            count+=1
    print(count)  