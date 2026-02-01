# count-pairs-whose-sum-is-less-than-target

nums = [-1,1,2,3,1]
target = 2
count = 0


left  = 0
for i in range(left+1, len(nums)):
    if nums[left] + nums[i] < target:
        left += 1
        count += 1
    
    
        
    


# for i in range(0, len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] < target:
#             count += 1
    
    
    
print(count)
    