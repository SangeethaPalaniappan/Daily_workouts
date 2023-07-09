# cook your dish here
#Not completed yet
T=int(input())
f=[]
for i in range(T):
    N=list(map(int,input().split()))
    if N[0]>N[1]:
        s=N[0]-N[1]
        
    else:
        s=N[1]-N[0]
    
    f.append(s)
    if f[0]==s:
        pass
    else:
        
        if f[0]>f[i]:
             
            if N[0]>N[1]:
                m=1,f[0]
                
            else:
                m=2,f[0]
                
        else:
            e=f[0]
            f[0]=f[i]
            f[i]=e
            if N[0]>N[1]:
                m=1,f[0]
                
            else:
                m=2,f[0]
                
        
for x in m:
    print(x,end=" ")
    
        