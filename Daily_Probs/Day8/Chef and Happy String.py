'''Chef has a string S with him. Chef is happy if the string contains a contiguous substring of length
strictly greater than 2 in which all its characters are vowels

1.S=abcdeeafg
Since the string eea is a contiguous substring and consists of all vowels and has a length>2,chef is happy
2.S=aebcdefghij
Since none of the contiguous substrings of the string consist of all vowels and have a length >2, Chef is sad.'''

# cook your dish here
T=int(input("T:"))
for i in range(T):
    S=input("S:")

    e=len(S)
    def vowels(s):
        if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
            return 1
        else:
            return 0
    if e>2:
        
        for i in range(e-2):
            if vowels(S[i])+vowels(S[i+1])+vowels(S[i+2])==3:
                print("Happy")
                break
        else:
            print("Sad")
    else:
        print("Sad")

        
            