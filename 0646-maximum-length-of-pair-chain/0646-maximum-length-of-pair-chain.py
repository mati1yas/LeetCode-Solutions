class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
      
        chain = defaultdict(int)
        
        
        pairs.sort()
        longest_chain=1
        
        for first,sec in pairs:
            
            chain[sec]=1
            for key in chain:
                
                if first>key:
                    
                    chain[sec]=max( chain[sec] , chain[key]+1)
                    longest_chain=max(longest_chain,chain[sec])
        
        return longest_chain