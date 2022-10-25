import heapq as h
class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_set=set({i for i in range(1,1000+1)})
        self.heap=[i for i in range(1,1000+1)]
        

    def popSmallest(self) -> int:
        
        pop=h.heappop(self.heap)
        self.infinite_set.remove(pop)
        return pop
    def addBack(self, num: int) -> None:
        if num not in self.infinite_set:
            
            h.heappush(self.heap,num)
            self.infinite_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)