class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        answer=0
        self.memo={}
        def helper(half):
            
            states=set()
            states.add((0,0))
            
            for rod in half:
                
                updated_states=set()
                
                for left,right in states:
                    
                    updated_states.add((left+rod,right))
                    updated_states.add((left,right+rod))
                
                states|=updated_states
                
            
            tallest={}
            
            for left,right in states:
                
                tallest[left-right]=max(tallest.get(left - right, 0), left)
                
            return tallest
        
            
        
        
        n=len(rods)
        left_half=helper(rods[:n//2])
        right_half=helper(rods[n//2:])
        
        
        
        for diff in left_half:
            
            if -diff in right_half:
                answer=max(answer,left_half[diff]+right_half[-diff])
                
        return answer
        
        