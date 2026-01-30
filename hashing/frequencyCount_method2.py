# method 2 for frequency count in hashing

nums = [1,2,3,2,3,4,2,1,4,2,1]
freq_count = {}
for i in range(0, len(nums)):
    if nums[i] in freq_count:
        freq_count[nums[i]] = freq_count.get(nums[i],0) + 1

    else:
        freq_count[nums[i]] = 1

print(freq_count)