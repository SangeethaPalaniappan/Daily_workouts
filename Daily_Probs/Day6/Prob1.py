#Air Conditioner Problem
#A,B,C wants to set AC temp
#A and C needs Atleast Temp where B needs atmost Temp
# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if B>=A and B>=C:
        print("Yes")
    else:
        print("No")