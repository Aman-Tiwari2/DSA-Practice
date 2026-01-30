# brute force approch we are going to use first 


nums = [3,1,-2,-5,2,-4]
positive = []
negative = []
res = []

for i in range(0, len(nums)):
    if nums[i] >= 0:
        positive.append(nums[i])
    else:
        negative.append(nums[i])

i = 0
j = 0

while i < len(positive) or j < len(negative):
    res.append(positive[i])
    res.append(negative[j])
    i += 1
    j += 1

print(res)


# know we are going to make an optimal solution for our code of rearrange value of zeros


        
        
        
        