class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2= nums2
        self.nums2Freq=Counter(nums2)
        
        

    def add(self, index: int, val: int) -> None:
        
        
#         we might consider keeping the data
        prevVal= self.nums2[index]
        newVal=val+prevVal
        self.nums2[index]+=val
        self.nums2Freq[newVal]+=1
        self.nums2Freq[prevVal]-=1
        
        
        

    def count(self, tot: int) -> int:
        
        ans=0
        for num in self.nums1:
            
            comp= tot-num
            
            
            ans+=self.nums2Freq[comp]
            
        return ans
            
            
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)