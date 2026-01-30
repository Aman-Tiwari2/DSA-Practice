arr = [12, 34, 67, 90]
n = 2

low2 = max(arr)
low = low2

high2 = sum(arr)
high = high2



# print(low)
# print(high)


# count number of pages

def countpages(arr, mid):
    stu = 1
    stupages = 0
    for i in range(0, len(arr)):
        if stupages + arr[i] <= mid:
            stupages += arr[i]
        else:
            stu += 1
            stupages = arr[i]
    return stu


# Binary search implementation

while low <= high:
    mid = (low+high) // 2
    noStud = countpages(arr, mid)
    if noStud > n:
        low = mid + 1
    else:
        high = mid - 1

print(low)










# -------------------------- Linear Search Array ---------------------------

# def booklist(arr, pages):
#     stu = 1
#     stupages = 0
#     for j in range(0,n):
#         if stupages + arr[j] <= pages:
#             stupages += arr[j]
#         else:
#             stu += 1
#             stupages = arr[j]

#     print(stu)

# booklist(arr, pages)

# for i in range(low, high):
#     Stucount = booklist(arr, pages)
#     if Stucount == n:
#         print(pages)
    

