# Here we are going to find number of accurence of an digit / value from one list to another

# --- Using Brute Force Approch but get an error of TLE(Time Limit Exceed) and Time Complexity is O(N^2)


'''
Constraints 
1 <= n[i] <= 10;
n can have 10^8 elements but from 1 to 10 
m can have 10^8 elements
''' 

lst = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
lst2 = [10, 111, 1, 9, 5, 67, 2]


for i in lst2:
    count = 0
    for x in lst:
        if i == x:
            count += 1
    print(count)


# Here we are using Hashing technique to solve this question so that our complexity is O(N+M) ~ O(N)

hash_map = [0] * 11
for i in lst:
    hash_map[i] += 1

print(hash_map)

for j in lst2:
    if j <= len(hash_map):
        print(hash_map[j])
    else:
        print(0)



            