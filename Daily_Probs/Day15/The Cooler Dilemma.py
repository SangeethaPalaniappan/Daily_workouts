# cook your dish here
t=int(input())
for p in range(t):
    x,y,m=map(int,input().split())
    # to check whether renting or purchasing  a machine is efficient
    # total months the cooler needed - m 
    # x - the cost for per month
    # y - the cost for purchasing
    # s=multiple the cost of per month(x) and the total months
    # if s < y (purchasing cost) print("YES") else print("NO") 
    r=x*m
    if r<y:
        print("YES")
    else:
        print("NO")
        