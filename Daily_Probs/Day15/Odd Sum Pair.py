# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
        
    #Out of three numbers, the sum of two numbers should be odd
    #so add two numbers and check whether it is odd or even
    #if the value is odd print("YES") else print("NO")
    if (a+b)%2!=0 or (b+c)%2!=0 or (c+a)%2!=0:
        print("YES")
    else:
        print("NO")