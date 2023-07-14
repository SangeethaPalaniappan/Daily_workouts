'''Given a positive integer N, MoEngage wants you to determine 
if it is possible to rearrange the digits of N (in decimal representation) and 
obtain a multiple of 5.

For example, when N=108, we can rearrange its digits to construct 
180/5=36
180=36 which is a multiple of 5'''


# cook your dish here
T=int(input("T:"))
for i in range(T):
    D=int(input("D:"))
    N=input("N:")
    for x in range(D):
        if int(N[x])==0 or int(N[x])==5:
            print("YES")
            break
            
            
    else:
        print("NO")


# Rearranging the digits
'''a=input("a:")
b=[]
for i in a:
    b.append(i)
n=len(b)
for x in range(n):
   if int(b[x])==5 or int(b[x])==0:
       temp=b[n-1]
        b[n-1]=b[x]
       b[x]=temp
        break       
for x in b:
    print(x,end="")'''


'''
Given a positive integer 
N, MoEngage wants you to determine if it is possible 
to rearrange the digits of 
N (in decimal representation) and obtain a multiple of 
5'''











#Actual solution 
# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    count = 0
    # D = list(map(int, input().split())
    D = int(input())
    while D > 0:
        K = D % 10
        if K % 5 == 0:
            count += 1
        D //= 10
    if count == 0:
        print("No")
    elif count > 0:
        print("Yes")