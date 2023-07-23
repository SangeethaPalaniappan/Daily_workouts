#Math Problem

'''In Chefland, a tax of rupees 10 is deducted if the total income is strictly greater than rupees 
100.

Given that total income is X rupees, find out how much money you get.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of each test case contains a single integer 
X — your total income.'''

# cook your dish here
T=int(input("T"))
for x in range(T):
    X=int(input("X"))
    if X>100:
        print(X-10)
    else:
        print(X)