class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        
        
        
        memo={}
        
        self.mod=10**9+7
        def takeQuestion(index,target):
            
            if target==0:
                return 1
            if index>=len(types):
                return 0
            
            
            if (index,target) in memo:
                
                return memo[(index,target)]
            
            ways=0
            question,point = types[index]
            ways=takeQuestion(index+1,target)
            for i in range(1,question+1):
                if target-(i*point)>=0:
                    newTarget=target-(i*point)
                    ways+=takeQuestion(index+1,target-(i*point))
            memo[(index,target)]=ways%self.mod
            return memo[(index,target)]
        return takeQuestion(0,target)