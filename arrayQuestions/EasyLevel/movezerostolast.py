nums = [0,0,1]

# best optimal approch for moving values to the end zeros

i = 0
for j in range(1, len(nums)):
    if nums[i] == 0:
        e = nums.pop(i)
        nums.append(e)
    else:
        i += 1


# best another optimal approch

 
if len(nums) == 1:
    print(1)
    
left = 0 
while left < len(nums):
    if nums[left] == 0:
            break
    left += 1

if left == len(nums):
    print(left)

j = left + 1
while j < len(nums):
    if nums[j] != 0:
        nums[left], nums[j] = nums[j], nums[left]
        left += 1
    j += 1
    
    
    
# one more optimal approch 

j = 0
for i in range(0, len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

        
print(nums)

