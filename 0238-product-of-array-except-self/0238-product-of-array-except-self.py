class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        pre=[nums[0]]
        post=[nums[len(nums)-1]]
        
        product=[0]*len(nums)
        
        for i in range(1,len(nums)):
            
            pre.append(pre[-1]*nums[i])
            
            post.insert(0,post[0]*nums[-i-1])
        
        for i in range(len(nums)):
            preP=1
            posP=1
            if i-1 >=0:
                preP=pre[i-1]
            if i+1<len(nums):
                posP=post[i+1]
            product[i]=preP*posP
            
                       
        return product