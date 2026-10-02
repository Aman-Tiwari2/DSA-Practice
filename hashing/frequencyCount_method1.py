# mehtod 1 for frequency count in hashing

lst = [1, 2, 3, 3, 2, 1]
x = 2
hash_map = {}
for i in range(0, len(lst)):
    if lst[i] in hash_map:
        hash_map[lst[i]] += 1

    else:
        hash_map[lst[i]] = 1


for i in hash_map:
    if i == x:
        print(hash_map[i])
            

# for i in hash_map:
#     print(i)
    # if hash_map[i] >= 2:
    #     print(True)
    # else:
    #     print(False)
    
# Method 2 

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
dist = {}

for i in range(0, len(nums)):
    dist[nums[i]] = dist.get(nums[i], 0) + 1
    
print(dist)

