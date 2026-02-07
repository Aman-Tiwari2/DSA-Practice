#  Maximum subarray problem 
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


max_sum = float('-inf')
total = 0



for i in range(0, len(nums) - 1):
    total = total + nums[i]
    max_sum = max(total, max_sum)
    if total < 0:
        total = 0




# for i in range(0, len(nums)):
#     total = 0
#     for j in range(i, len(nums)):    
#         total= total + nums[j]
#         max_sum = max(total, max_sum)
        
        
        
print(max_sum)