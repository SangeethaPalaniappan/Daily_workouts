# cook your dish here
t=int(input())
for x in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    k=int(input())
    # the position is on the 1-indexed basis [index position is starting with 1]
    # but the list will be in the 0-indexed, so reduce the position number by 1
    v=lis[k-1] 
    lis.sort()
    for m in range(n):
        if lis[m]==v:
            print(m+1)
            break