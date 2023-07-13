#Armstrong number
n=input("n:")
s=0
for i in n:
    i=int(i)**3
    s=s+i
print(s)    
if int(n)==s:
    #Here I put int(n) because i get the input not as an integer It will 
    #be like string
                    
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")