class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        self.memo={}
        def changeString (index1,index2):
            
            if index1==0:
                
                return index2
            if index2==0:
                return index1
            
            if (index1,index2) in self.memo:
                return self.memo[(index1,index2)]
        
            minOp=float('inf')
            if word1[index1-1]!=word2[index2-1]:
                
                delete=changeString(index1-1,index2)

                insert=changeString(index1,index2-1)

                replace=changeString(index1-1,index2-1)
                
                minOp=min(delete,insert,replace)+1
            
            else:
                minOp= changeString(index1-1,index2-1)
                
                
            self.memo[(index1,index2)]=minOp
            return minOp
        return changeString(len(word1),len(word2))