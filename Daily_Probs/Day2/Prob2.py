'''On breaking, the string 

S gives A=abc and B=abc. Thus, joining it in either way
(AB or BA), would give the same string S'''
# cook your dish here
def string(N,S):
    d=N//2   
    m=len(S)
    if N!=m:
        print("Given length and the string lenght is not equal")
    else:
        if N==0:
            print("No string is given")
            return 0
        m=""
        for i in S:
            s=ord(i)
        
        #If the character is in uppercase and it need to be converted it into lower
            if s>=65 and s<=90:
                r=chr(s+32)
                m=m+r
            else:
                r=i
                m=m+r
        
        #If the character is in lowercase and it need to be converted it into upper
        #if s>=97 and s<=122:
        #   r=chr(s-32)
        #else:
            #r=i
            #m=m+r'''
         
        S=m
        if N%2==0:
            e=S[0:d]
            f=S[d:N]
            for x in range(d): 
                if e[x]==f[x]:
                    pass
                else:
                    return 0
                    
            return 1    
        else:
            e=S[0:d]
            f=S[d+1:N]
            for x in range(d): 
                if e[x]==f[x]:
                    pass
                else:
                    return 0
                
        return 1
        
            
    
T=int(input("T:"))
for i in range(T):
    N=int(input("N:"))
    S=str(input("S:"))
    if string(N,S)==1:
        print("YES")
    else:
        print("NO")
