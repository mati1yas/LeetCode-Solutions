class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
  
        self.arr=[[1]]
        
        def addRow(arr,currow):
            
            if currow>=numRows:
                return 
            newarr=[0]+arr+[0]
            
            p1,p2=0,1
            
            arr=[]
            while p2<len(newarr):
                arr.append(newarr[p1]+newarr[p2])
                p1+=1
                p2+=1
            self.arr.append(arr)
            addRow(arr,currow+1)
                
            
            
                
            
            
            
            
        
        
        addRow([1],1)
            
        return self.arr
        
        
        
        