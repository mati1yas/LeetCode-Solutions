class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        memo={}
        
        
        def change(amount,index):
            
            if amount == 0:
                
                return 1
            if index>=len(coins):
                return 0
            
            ans=[]
            
            
            if (amount,index) in memo:
                
                return memo[(amount,index)]
            
            
            not_take= change(amount,index+1)
            take=0
            if amount-coins[index]>=0:
                
                take=change(amount-coins[index],index)
                
            
            memo[(amount,index)]=take+not_take
            return memo[(amount,index)]
                    
                    
        
        return change(amount,0)
        
        
                