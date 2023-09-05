n = 10
i = 0
if n % 2 ==0:
    print("Cannot pattern in this scenario")
else:    
    while n != -1:
        s = n * " *"
        n -= 2 # Reduce two stars in each step
        print(i * "  ",s) # Leave two spaces [* the multiple of each iterations] in front
        i += 1 # Increment 1 in each iteration


# Constraints :
#           Only odd numbers
#           Non-negative numbers    