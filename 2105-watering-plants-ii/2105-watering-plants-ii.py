class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        
        left=0
        right=len(plants)-1
        refill=0
        A=capacityA
        B=capacityB
        while left<=right:
            
            
            if left==right:
                
                if max(A,B)<plants[right]:
                    refill+=1
                return refill
            if A<plants[left]:
                A=capacityA-plants[left]
                refill+=1
            else:
                A-=plants[left]
            left+=1
            
            if B<plants[right]:
                B=capacityB-plants[right]
                refill+=1
            else:
                B-=plants[right]
            right-=1
        
        return refill
            
            