nums=[0,0,3,3,5,6]
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1
    
obje1= Solution()
ans= obje1.removeDuplicates(nums)
print(ans)