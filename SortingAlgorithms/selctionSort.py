

# Here we are going to learn about selection sort 

def selection_sort(nums):
    nums_len = len(nums)
    for i in range(0, nums_len):
        nums_min = i
        for j in range(i+1, nums_len):
            if nums[j] < nums[nums_min]:
                nums_min = j
            
        nums[i], nums[nums_min] = nums[nums_min], nums[i]






lst = [9,0,4,2,5,6,1,6,8,7]
print(selection_sort(lst))