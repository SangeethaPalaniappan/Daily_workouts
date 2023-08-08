# cook your dish here
t=int(input("t:"))
for i in range(t):
    n=int(input("n:"))
    # N is even
    # Car needs 4 tyres so, if the gn. no. of tyres is divisible by 4 then , chef can manufacture cars only
    # since need to manufacture maximum no.of cars in the given tyres
    # If there is remainder using that chef can create bikes
    # if n%2==0, then the following conditions works
    # else maybe no cars or bikes can create
    s=n%4
    if s==0:
        print("NO")
    else:
        print("YES")