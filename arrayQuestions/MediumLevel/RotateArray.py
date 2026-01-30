# Here we learn about 3 ways to do rotate array questions brute, better and optimal

# for brute force methead


'''
def rotatearray(nums, k):
    # for some multiples of two's approach
    n = len(nums)
    nooftimesrotate = k % n

    # used for rotations
    for _ in range(0, nooftimesrotate):
        addinfront = nums.pop()
        nums.insert(0, addinfront)

    return nums
'''

# using slicing method to obtain our result 

'''
def rotatearray(nums, k):
    n = len(nums)
    nooftimesrotate = k % n

    return nums[nooftimesrotate - k: ] + nums[ : nooftimesrotate - k]

'''


# By using two pointers approch in this question

'''
class Solution:
    def reverse(self, nums: list[int], l: int, r: int) -> None:
        """
        Reverse the portion of nums starting at index l up to index r in-place.
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  
        k = k % n
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n - k -1)
        self.reverse(nums, 0, n-1)

'''