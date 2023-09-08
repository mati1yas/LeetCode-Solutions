class OrderedStream:

    def __init__(self, n: int):
        
        self.stream = {}
        self.currentPos=1
        self.maxPos=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.stream[idKey] = value
        self.maxPos=max(self.maxPos,idKey)
        ans=[]
        for pos in range(self.currentPos,self.maxPos+1):
            
            if pos not in self.stream:
                return ans

            if pos>=idKey :
                ans.append(self.stream[pos])
                
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)