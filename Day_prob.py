s = "Let's take LeetCode contest"
print(len(s))
d =list(s)
print(d)
l = 0
k = []
while l != len(s): 
    if d[l] != " ":
        k.append(d[l])
    if d[l] == " ":
        k[::-1]    
        print(k)
    l += 1    