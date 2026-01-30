def removeDuplicates(nums) -> int:
    i = 0 # This is used for the count of the number of times uniqe element appears.
    for j in range (1, len(nums)):
        if nums[i] != nums[j]: # check the conditions where first element value is not equal to second element value 
            i += 1 # Increment i to 1 for the uniqe. element finding
            nums[i] = nums[j] # Make first element the second one
                
    return i+1 #returns number of uniqe elements