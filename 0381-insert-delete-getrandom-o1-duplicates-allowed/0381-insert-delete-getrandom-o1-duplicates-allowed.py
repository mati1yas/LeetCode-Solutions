class RandomizedCollection:

    def __init__(self):
        
        self.indexes=defaultdict(set)
        
        self.arr=[]
        
        

    def insert(self, val: int) -> bool:
        
        
        if val not in self.indexes:
            self.indexes[val].add(len(self.arr))
            self.arr.append(val)
            
            return True
        
        self.indexes[val].add(len(self.arr))
        self.arr.append(val)
        return False
    
       

    def remove(self, val: int) -> bool:
        
        if val in self.indexes:
            
            lastElement=self.arr[-1]
            
            if lastElement==val:
                self.indexes[val].remove(len(self.arr)-1)
                self.arr.pop()
            else:
                
                idx=self.indexes[val].pop()
                self.arr[idx]=lastElement
                self.indexes[lastElement].remove(len(self.arr)-1)
                self.indexes[lastElement].add(idx)
                self.arr.pop()
                
            
            
            if len(self.indexes[val])<=0:
                self.indexes.pop(val)
            
            return True
        return False
                


    def getRandom(self) -> int:
        
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()