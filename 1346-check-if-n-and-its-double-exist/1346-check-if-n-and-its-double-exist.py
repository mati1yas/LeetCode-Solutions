class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        visited=set()
        
        for elem in arr:
            
            if 2*elem in visited or elem/2 in visited:
                return True
            
            visited.add( elem)
            
        
            