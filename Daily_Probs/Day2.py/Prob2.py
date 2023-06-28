'''On breaking, the string 
S gives A=abc and B=abc. Thus, joining it in either way
(AB or BA), would give the same string S
'''

# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    S=str(input())
    e=S[0:N//2]
    f=S[N//2:N]

    if e==f:
        print("YES")
    else:
        print("NO")
