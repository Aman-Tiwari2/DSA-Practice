# Leetcode 128: Longest Consecutive Sequence 
# Brute Force Approach

nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

'''
max_count = 0
for i in range(0, len(nums)):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num = num + 1
    max_count = max(max_count, count)
'''

# Better Approach 

'''
nums.sort()
last_smaller = float('-inf')
count = 1
longest = 0

for i in range(0, len(nums)):
    num = nums[i]
    if num - 1 == last_smaller:
        count += 1
        last_smaller = num
    elif nums != last_smaller:
        count = 1
        last_smaller = num
        
    longest = max(longest, count) 
'''



unique_val = set(nums) 
longest= 0

for num in unique_val:
    if num - 1 not in unique_val:
        x = num
        count = 1
        while x+1 in unique_val:
            count += 1
            x += 1
        longest = max(longest, count)




print(longest)
      