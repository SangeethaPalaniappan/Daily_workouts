'''Write a program 
to find the factorial value of any number entered by the user'''
#Changed the mistakes

# cook your dish here
T=int(input("T:"))
for i in range(T):
    N=int(input("N:"))
    s=1
    for x in range(1,N+1):
        s*=x
    print(s)
