import heapq as h
class MedianFinder:

    def __init__(self):
        
        self.left=[]
        self.right=[]
        
        h.heapify(self.left)
        h.heapify(self.right)
        

    def addNum(self, num: int) -> None:
        
        h.heappush(self.right,num)
        
        val = h.heappop(self.right)
        
        h.heappush(self.left,-val)
        
        if len(self.left) > len(self.right)+1:
            
            val=h.heappop(self.left)
            h.heappush(self.right,-val)
            
            

    def findMedian(self) -> float:
        
        if (len(self.right)+len(self.left))%2==0:
            return (-self.left[0]+self.right[0])/2
        else:
            return -self.left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()