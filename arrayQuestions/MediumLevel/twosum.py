# here we have two different approaches to solve this problem- one is brute force and optimal solutions


nums = [3,3]
target = 6

for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])


# using hash map we do this questions 
hash_map = {}

for i in range(0, len(nums)):
    remaining = target - nums[i]
    if remaining in hash_map:
        print([hash_map[remaining], i]) 
    else:
        hash_map[nums[i]] = i 
        
        