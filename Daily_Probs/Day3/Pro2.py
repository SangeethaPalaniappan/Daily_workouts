'''
Given a positive integer 
N, MoEngage wants you to determine if it is possible 
to rearrange the digits of 
N (in decimal representation) and obtain a multiple of 
5'''

# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    count = 0
    # D = list(map(int, input().split())
    D = int(input())
    while D > 0:
        K = D % 10
        if K % 5 == 0:
            count += 1
        D //= 10
    if count == 0:
        print("No")
    elif count > 0:
        print("Yes")