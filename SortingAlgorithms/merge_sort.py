nums = [9,6,7,8,4,5,3,2,1]

# Here we are going to write the merge_array concept so that we can easily use it in our sorting also.

def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < n:
        result.append(left[i])
        i += 1
    
    while j < m:
        result.append(right[j])
        j += 1
        
    return result


# now we are going to write the apprach of merge_sort array concept.
 
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_sort = merge_sort(left_arr)
    right_sort = merge_sort(right_arr)
    
    return merge_array(left_sort, right_sort)


print(merge_sort(nums))