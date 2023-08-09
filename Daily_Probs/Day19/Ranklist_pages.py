# cook your dish here

#TIme complexity -O(1){If the test case loop not included}
t=int(input("t:"))
for i in range(t):
    x=int(input("x:"))
    s=x/25 # s will give the no.of pages
    t=x%25
    if t==0: # If the remainder is 0 , then print the s value
        print(int(s))
    else:    # if not 0 , then print s+1
        print(int(s)+1)