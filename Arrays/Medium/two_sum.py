class Solution:
    def twoSum(self, nums, target):
        result=[]

        left=0
        right=(len(nums)-1)
        for right in nums:
            if nums[left]+nums[right]== target:
                result.append(left,right)
            right-=1    


                    

nums = [1,3,5,-7,6,-3]
target=0
obj=Solution()
print(obj.twoSum(nums, target))