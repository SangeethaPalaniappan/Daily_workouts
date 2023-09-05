n = int(input("n:"))
m=n
i = 1
while i != m:
    s = n - 1 # the space is exactly less by 1 from n
    print(s * " " , i * "*") # Multiply the space by 1 
    i += 2 # Increment i by 2
    n -= 2 # to reduce the n