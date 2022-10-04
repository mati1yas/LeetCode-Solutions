class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        r=[-1]*len(nums2)
        validx=defaultdict(int)
        stack=[]
        for i,val in enumerate(nums2):
            
            while stack and val>stack[-1][1]:
                
                idx,vl=stack.pop()
                r[idx]=val
                
            stack.append((i,val))
            
        for i, num in enumerate(nums2):
            validx[num]=r[i]
        return [validx[x] for x in nums1]