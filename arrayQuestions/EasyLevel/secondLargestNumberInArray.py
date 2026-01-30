# nums = [-55, -32, -97, -99, -3, -67]
nums = [55, 32,3, 67, 88, 99, 99, 88]

largest = float("-inf")
second_largest = float("-inf")

for i in range(0, len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > largest and nums[i] != largest:
        second_largest = nums[i]



print(largest)
print(second_largest)