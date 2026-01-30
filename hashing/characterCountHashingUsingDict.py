# We can solve this question using character ascii value like in this 97 to 122 and 
# when we substract we get 27 as value that can use to make hash of list 27 (O)s like lst = [0] * 27
# Constraints are 'a' <= s[i] <= 'z' 


originalChar = "azyxyyzaaaa" 
compareChar = ['d', 'a', 'y', 'z']

freq_count = {}

for i in originalChar:
    if i in freq_count:
        freq_count[i] += 1
    else:
        freq_count[i] = 1

for i in compareChar:
    if i in freq_count:
        print(i, freq_count[i])
    else:
        print(i, 0)


# using character ascci value



hash_lst = [0] * 26

for ch in originalChar:
    ascii_order = ord(ch)
    index = ascii_order - 97
    hash_lst[index] += 1

for ch2 in compareChar:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_lst[index])


print(hash_lst)




# check valid anagram 

s = "anagram"
t = "nagarmaaaatr"

hash_lst = [0] * 27



for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_lst[index] += 1

for ch2 in t:
    ascii_value = ord(ch2)
    index = ascii_value - 97
    hash_lst[index] -= 1

for i in range(0, len(hash_lst)):
    if hash_lst[i] != 0:
        print("False")

print("True")

     

