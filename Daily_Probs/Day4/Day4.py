#Factorial
a=int(input(""))
s=1
for i in range(1,a+1):
    s=s*i
print(s)

#work on it
def fact(val):
    fact(val)*fact(val-1)
    return

fact(10)