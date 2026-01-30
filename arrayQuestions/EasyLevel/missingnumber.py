n = [0,2,3,4,6,7,1]



# Brute force approach  with N(O^2) complexity

for i in range(0, len(n)+1):
    if i not in n:
        print(i)
        
        
# better approch for this question 


nums = [9,6,4,2,3,5,7,0,1]


hash_map = {x : 0 for x in range(0, len(nums)+ 1)}

for i in range(0, len(nums)):
    if i in hash_map:
        hash_map[nums[i]] += 1
    else:
        hash_map[nums[i]] = 0
        


for i in hash_map:
    if hash_map[i] == 0:
        print(i) 
        
        
        
# optimal approch 

n = len(nums)
print((n*(n+1))//2 - sum(nums))