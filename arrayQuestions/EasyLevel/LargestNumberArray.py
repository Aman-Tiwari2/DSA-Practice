# Here we are going to use first method for finding list largest number.

nums = [-55, -32, -97, -99, -3, -67]

largest = nums[0]
for i in range(0, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        # largest = max(largest, nums[i])
    

print(largest)
        

# Here we are going to use second method for finding list largest number.

largest = float("-inf")
for i in range(0, len(nums)):
    if nums[i] > largest:
        largest = nums[i]

print(largest)