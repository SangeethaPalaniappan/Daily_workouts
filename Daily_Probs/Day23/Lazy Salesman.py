# cook your dish here
t=int(input())
for x in range(t):
    n,w=map(int,input().split())
    lis=list(map(int,input().split()))
    s=lis.sort(reverse=True) # sort the given list
    count=0 # this is initialised to count the days
    d=0 # this adds the value
    for i in lis:
        if w>d: # if the adding rupees is less than the actual rupees add the rupee and increase the count by 1 
            d=d+i
            count+=1
        else: # if the added rupees is greater than or equal the acutal rupee then break the loop 
            break
    print(n-count)  # print the total no. of days - the counted days  