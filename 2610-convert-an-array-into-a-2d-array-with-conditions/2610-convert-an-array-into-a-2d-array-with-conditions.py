class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        
        
        arrRows= [[]]
        
        
        for num in nums:
            foundRow= False
            for row in arrRows:
                
                if num not in row:
                    
                    row.append(num)
                    foundRow=True
                    break
            
            if not foundRow:
                arrRows.append([num])
                
                
        return arrRows
                    