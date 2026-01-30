# ================== Here we are going to perform list reversial using recursion
def reverseArr(nums, left, right):
    if left <= right:
        nums[left-1], nums[right-1] = nums[right-1], nums[left-1]
        return reverseArr(nums, left + 1, right - 1)



nums = [1, 6, 7, 4]
print(reverseArr(nums,1,4))

