# Using brute force we are solving this question

nums = [1, 99, 101, 98, 2, 5, 3, 100]
max_count = 0 # Here we take an initial zero for the count longest subsequence value

for i in range(0, len(nums)):
    num = nums[i] # take first value of array for comaprison 
    count = 1 # Take initial count with one so that we can easily update in max_count using this count in below loop
    while num + 1 in nums:
        count += 1 # Updating count value
        num = num + 1 # Know we are going to update our num for while loop checking 
    max_count = max(max_count, count)
    

print(max_count)


# Using
