'''S -hiiden letter
T-guess letter
if the guess letter is correct print("G)
else print("B)
Ex:ABCDE
BACED
here the letter c is correct so print("G")
the output will be : BBGBB'''
#need to work on use cases - worked 
# cook your dish here

E=int(input("E"))
for i in range(E):
    print("\n")
    S=str(input("S:"))
    T=str(input("T:"))
  
    m=""
    for i in S:
        s=ord(i)
        
        #If the character is uppercase and it need to be converted it into lower
        if s>=65 and s<=90:
            r=chr(s+32)
            m=m+r
        else:
            r=i
            m=m+r
    
    S=m
        #If the character is lowercase and it need to be converted it into upper
        #if s>=97 and s<=122:
         #   print(chr(s-32),end="")
        #else:
         #   print(i,end="")'''

    n=""
    for j in T:
        sd=ord(j)
        #If the character is uppercase and it need to be converted it into lower
        if sd>=65 and sd<=90:
            t=chr(sd+32)
            n=n+t
        else:
            t=j
            n=n+t
    T=n        

        #If the character is lowercase and it need to be converted it into upper    
        #if s>=97 and s<=122:
         #   print(chr(s-32),end="")
        #else:
         #   print(j,end="")'''
    if len(S)==len(T):
        for i in range(len(S)):  
        
            if S[i]==T[i]:
                print("G",end="")
            else:
                print("B",end="")
    
        
    else:
        #print("Length of the strings are not equal")
        for i in range(len(S)):# use the length of the original string
            print("B",end="")
    

    
