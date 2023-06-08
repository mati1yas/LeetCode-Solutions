class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        candy=[1 for i in range(len(ratings)+2)]
        candy[0]=0
        candy[-1]=0
        
        ratings.insert(0,float('inf'))
        ratings.append(float('inf'))
       
        for i in range(1,len(ratings)-1):
            if ratings[i]>ratings[i-1]:
                candy[i]=max(candy[i],candy[i-1]+1)
                
        for i in range(len(ratings)-2,0,-1):
            
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)
        
        return sum(candy)
            
            
            
            
        
                
                
            


            
            
            
            