# Find Largest


nums = [55, 32, -97, 99, 3, 67]
       
maxi = float('-inf')
second_max = 0

for i in range(0, len(nums)):
    if nums[i] > maxi:
        second_max = maxi
        maxi = nums[i]
    
print(maxi)
print(second_max)

 

    
        
        