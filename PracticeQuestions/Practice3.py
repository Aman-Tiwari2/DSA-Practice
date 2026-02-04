# Find Largest


nums = [55, 32, -97, 99, 3, 67]
       
maxi = float('-inf')
second_max = float("-inf")

# for i in range(0, len(nums)):
#     if nums[i] > maxi:
#         maxi = nums[i]
    
# for i in range(0, len(nums)):
#     if nums[i] > second_max and nums[i] != maxi:
        # second_max = nums[i]
        
for i in range(0, len(nums)):
    if nums[i] > maxi:
        second_max = maxi
        maxi = nums[i] 
    elif nums[i] > second_max and nums[i] != maxi:
        second_max = nums[i]
        
print(maxi)
print(second_max)

 

    
        
        