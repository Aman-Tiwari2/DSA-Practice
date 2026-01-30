# it have two approches for counting maximum number of 1's

nums = [1,1,0,1,1,1]
max_ones = []
count = 0
max_ones = 0

for i in range(0, len(nums)):
    if nums[i] == 0:
        max_ones.append(count)
        count = 0
    else:
        count += 1
                
max_ones.append(count)
print(count)


# another approach for same question 


for i in range(0, len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        max_ones = max(count, max_ones)
        count = 0
        
print(max(count, max_ones))

