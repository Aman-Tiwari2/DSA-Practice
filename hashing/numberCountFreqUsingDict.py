# Here we are going to use dictionary to count frequency form one list element to another time Complexity is O(N)

'''
Constraints 
1 <= n[i] <= 10;
n can have 10^8 elements but from 1 to 10 
m can have 10^8 elements
''' 

lst = [5, 3, 2, 2, 1, 1, 1, 5, 5, 7, 5, 10]
lst2 = [10, 111, 1, 9, 5, 67, 2]

Freq_count = {} 
for num in lst:
    if num in Freq_count:
        Freq_count[num] += 1
    else:
        Freq_count[num] = 1

for key in lst2:
    # if key in Freq_count and key == Freq_count[key]:  Here we compare list value to dictionary value in Freq_count[key]
    if key in Freq_count:
        print(Freq_count[key])
    else:
        print(0)






    