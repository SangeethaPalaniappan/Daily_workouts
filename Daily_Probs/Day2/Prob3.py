#Palindrome Problem
# cook your dish here

# cook your dish here
T=int(input())
for i in range(T):
    N=input()
    d=len(N)
    e=""
    for i in range(d):
        e=e+N[d-1]
        d-=1
    if N==e:
        print("wins")
    else:
        print("loses")


'''s=input("s:")
d=len(s)
e=""
for i in range(d):
    if s[i]==s[d-1]:
        d-=1
        pass
    else:
        s="loses"
        print(s)
        break
if s!="loses":
    print("wins")'''
        
