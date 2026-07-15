class Solution:
    def hashing(self,nums):
        temp={}
        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num]=1
                
        result=[]
        for key in temp:
            val=temp[key]
            result.append([key,val])

        return result
