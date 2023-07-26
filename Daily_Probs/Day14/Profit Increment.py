# cook your dish here
T=int(input("T:"))
for x in range(T):
    f,g=map(int,input().split())
    d=f//10
    print(g+d)