class RandomizedSet:

    def __init__(self):
        self.map={}
        self.list=[]
        

    def insert(self, val: int) -> bool:
        
        if val not in self.map:
            self.list.append(val)
            self.map[val]=len(self.list)-1
            return True
        return False
       
    def remove(self, val: int) -> bool:
        
        if val in self.map:
            removeindex=self.map[val]
            lastElement=self.list[-1]
            
            
            self.list[removeindex]=lastElement
            self.map[lastElement]=removeindex
            
            self.list[-1]=val
            self.list.pop()
            self.map.pop(val)
            return True
        return False
        
       
        
       
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()