# cook your dish here
t=int(input("t:"))
for x in range(t):
    w,x,y,z=map(int,input().split())
    # w - current balance
    # x - monthly deposit
    # y - mothly deduction
    # z - months
    # to find the final after z months
    s=w+(x-y)*z
    print(s)