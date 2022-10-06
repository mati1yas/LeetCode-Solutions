class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        self.arr=[]
        
        def addRow(arr,currow):
            
            if currow>rowIndex:
                self.arr=arr
                return 
            
            newarr=[0]+arr+[0]
            p1=0
            p2=1
            arr=[]
            
            while p2<len(newarr):
                arr.append(newarr[p1]+newarr[p2])
                p1+=1
                p2+=1
            
            addRow(arr,currow+1)
            
        addRow([1],1)
        return self.arr