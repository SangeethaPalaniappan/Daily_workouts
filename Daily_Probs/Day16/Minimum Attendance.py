# cook your dish here
t=int(input())
for c in range(t):
    x=int(input())
    m=input()
    s=len(m)
    y=m.count("1")
    k=120-x
    f=(75/100)*120
    l=(y+k)
     
    if (l)>=f:
       
        print("YES")
    else:
        print("NO")