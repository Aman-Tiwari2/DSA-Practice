# Rearange Element by Sign 
# Brute Force Approach 

nums = [3,1,-2,-5,2,-4]



neg_nums = []
pos_nums = []
new_lst = []

for i in range(0, len(nums)):
    if nums[i] < 0:
        neg_nums.append(nums[i])
    else:
        pos_nums.append(nums[i])
              
for i in range(0, len(pos_nums)):
    nums[2*i] = new_lst.append(pos_nums[i])
    nums[(2*i)+1] = new_lst.append(neg_nums[i])
        
print(new_lst)



result = [0]*len(nums)
left, right = 0, 1

for i in range(0, len(nums)):
    if nums[i] >= 0:
        result[left] = nums[i]
        left += 2
    else:
        result[right] = nums[i]
        right += 2
        
print(result)




        
     
        



    


