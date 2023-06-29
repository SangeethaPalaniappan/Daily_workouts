'''S -hiiden letter
T-guess letter
if the guess letter is correct print("G)
else print("B)
Ex:ABCDE
BACED
here the letter c is correct so print("G")
the output will be : BBGBB'''

# cook your dish here
E=int(input("E"))
for i in range(E):
    S=str(input("S:"))
    T=str(input("T:"))
    for i in range(5):
        if S[i]==T[i]:
            print("G",end="")
        else:
            print("B",end="")

    print("")
    print("")
