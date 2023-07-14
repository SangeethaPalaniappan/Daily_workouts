# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    def vowels(s):
        if "a"==s or "e"==s or "i"==s or "o"==s or "u"==s:
            return 0
        else:
            return 1
    count=0
    sent=0
    for i in range(N-3):
        s=vowels(S[i])+vowels(S[i+1])+vowels(S[i+2])+vowels(S[i+3])
    
        if s>=4:
            print("NO")
            break
            
    else:
        print("YES")
        