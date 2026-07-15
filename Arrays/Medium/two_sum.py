class Solution:
    def twoSum(self, nums, target):
        result=[]

        for i in range (0, len(nums)):
            first=nums[i]
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    break
            result.append([i,j])
            return result
                    

nums = [1,3,5,-7,6,-3]
target=0
obj=Solution()
print(obj.twoSum(nums, target))