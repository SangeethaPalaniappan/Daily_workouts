#Math Problem
#Messi vs Ronaldo

# cook your dish here
A,B,C,D=map(int,input().split())
s=A*2+B*1
e=C*2+D*1
if s>e:
    print("Messi")
elif s<e:
    print("Ronaldo")
else:
    print("Equal")