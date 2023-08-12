# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    lis=list(map(int,input().split())) # list 
    j=0 # initialise for the count
    for m in lis: # this loop is to check for every element in the list
        if m>=x:
            j+=1 #counting the greatest the element
    print(j)        