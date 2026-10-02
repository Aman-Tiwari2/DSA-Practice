arr1 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]

# using brute force approach using extra space i am solving this question.

n = len(arr1)
result_arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(0, n):
        for j in range(0, n):
                result_arr[j][(n-1)-i] = arr1[i][j]

print(result_arr)

# using optimal approach
# Firstly i am going to transpose the matrix

for i in range(0, n-1):
        for j in range(i+1, n):
                arr1[i][j], arr1[j][i] = arr1[j][i], arr1[i][j] 
                
print(arr1)

# Now going to make it reverse the each row in the matrix

for i in range(0, n):
        arr1[i].reverse()
        
print(arr1)
        