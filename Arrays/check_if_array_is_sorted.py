arr=[1,2,3,4,6]
class Solution:
    def isSorted(self,nums):
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                return False
        return True
    
obj1=Solution()
print(obj1.isSorted(arr))