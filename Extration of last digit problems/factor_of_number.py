from math import sqrt
# by using brute force methed time complexity will be O(N^2)

'''

user_input = int(input("Enter your Number for factors :- "))
num = user_input
lst = []
for i in range(1, num+1):
    if num % i == 0:
        lst.append(i)

print(lst)

'''


# Better Solution have time complexity O(N/2)

'''

user_input = int(input("Enter your Number for factors :- "))
num = user_input
lst = []
for i in range(1, num//2 + 1):
    if num % i == 0:
        lst.append(i)

lst.append(num)

print(lst)

'''

# Optimal Approach time complexity O(sqrt N) if we sort then O(n log n)

user_input = int(input("Enter your Number for factors :- "))
num = user_input
lst = []
for i in range(1, int(sqrt(num))):
    if num % i == 0:
        lst.append(i)
        if num//i not in lst:
            lst.append(num//i)

lst.sort()
print(lst)