nums=[0,1,4,0,5,2]
class Solution:
    def move_zeros_to_end(self, nums):
        count=0
        for num in nums:
            if num==0:
                nums.remove(num)
                count+=1
        while count:
            nums.append(0)
            count-=1
        print(nums)

obj= Solution()
obj.move_zeros_to_end(nums)