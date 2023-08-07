# cook your dish here
t=int(input())
for x in range(t):
    x,y,z=map(int,input().split())

    # multiply any two numbers and keep it as A and the remaining one element as B
    
    a=x*y
    b=z
    A=y*z
    B=x
    Aa=z*x
    Bb=y

    # Check whether it is divided by B or not 
    # If it is divided by B , then print that A and B

    if a%b==0:
        print(a,b)
    elif A%B==0:
        print(A,B)
    elif Aa%Bb==0:
        print(Aa,Bb)

    # else print -1    
    else:
        print(-1)