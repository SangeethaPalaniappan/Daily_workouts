# cook your dish here

T=int(input("T:"))
for x in range(T):
    S=input("S:")
    t=0
    s=0
    for i in S:
        if i=="0":
            t+=1
        elif i=="1":
            s+=1
    if s>t:
        print("WIN")
    else:
        print("LOSE")