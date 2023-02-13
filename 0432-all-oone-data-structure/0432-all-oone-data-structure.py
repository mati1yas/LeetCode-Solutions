class AllOne:

    def __init__(self):
        
        self.words={}   # "abcd": (freq,index)
        
        self.frequency=defaultdict(list)  # 1:["adk","dfak]   this stores words with some frequency together
        
        
        
        

    def inc(self, key: str) -> None:
        
        
        if key in self.words:
            
            loc,index=self.words[key]
        
            self.frequency[loc].remove(key)
            
            if len(self.frequency[loc])==0:
                self.frequency.pop(loc)
            
            self.words[key][0]+=1
            
            freq=self.words[key][0]
            
            
            
            
            self.frequency[freq].append(key)
        
        
        else:
            self.words[key]=[1,0]
            
            self.frequency[1].append(key)
            
            
        

    def dec(self, key: str) -> None:
        
        loc,index=self.words[key]
        
        self.frequency[loc].remove(key)

        if len(self.frequency[loc])==0:
            self.frequency.pop(loc)

        self.words[key][0]-=1

        if self.words[key][0]==0:
            self.words.pop(key)

        else:
            freq=self.words[key][0]



            self.frequency[freq].append(key)
        

    def getMaxKey(self) -> str:
        
        if not self.frequency.keys():
            return ""
        
        return self.frequency[max(self.frequency.keys())][0]
        

    def getMinKey(self) -> str:
        if not self.frequency.keys():
            return ""
        return self.frequency[min(self.frequency.keys())][0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()