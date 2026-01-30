# -------- Here we are going to learn about how we can achive functional recursion ---------

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:    
        return num * fact(num - 1)


x = fact(5)
print(x)

# ------> Time Complexity O(n)
# ------> Space Complexity O(n) stack space 