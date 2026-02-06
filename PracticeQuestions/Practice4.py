nums = [3,4,5]

j = 0
for i in range(1, len(nums)):
    if nums[j] > nums[i]:
        print(False)
    else:
        j += 1

print(True)
    