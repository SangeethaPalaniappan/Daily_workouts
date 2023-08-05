# cook your dish here
for X in range(int(input())):
    n,x,y=map(int,input().split())
    m=n*x
    if y!=0:
        if m==y:
            print("YES")
        elif m!=y:
            s=y//x
            if s*x==y:
                print("YES")
            else:    
                print("NO")
    else:
        if y==0:
            print("YES")
        else:
            print("NO")