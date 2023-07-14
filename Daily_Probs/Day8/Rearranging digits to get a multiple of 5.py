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