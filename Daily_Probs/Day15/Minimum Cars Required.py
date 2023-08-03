# cook your dish here
t=int(input())
for x in range(t):
    # a car have 4 seats
    # to get the count of the car, no.of people / 4[seats of each car]
    
    
    y=int(input())
    h=y/4 # this will have the float value
    
    # if the count of the people is multiple of 4 , then we can print the multiplier of the product 
    if y%4==0:
        # the value of h is float, so int(h) will give the integer value without decimal
        print(int(h))
        
    
    #if not add 1 to the multiplier
    else:
        print(int(h)+1)