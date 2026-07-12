nums= [1,2,3,4,5]
class Solution:
    def rotateArrayByOne(self, nums):
        first = nums[0]

        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]

        nums[-1] = first
obje1= Solution()
obje1.rotateArrayByOne(nums)