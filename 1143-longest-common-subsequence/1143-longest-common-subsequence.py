class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        @lru_cache (maxsize=None)
        
        def longestCommon(index1,index2):
            
            if index1==len(text1) or index2==len(text2):
                return 0
            
            
            case1=longestCommon(index1+1,index2)
            case2=0
            firstOccurrence=text2.find(text1[index1],index2)
            if firstOccurrence!=-1:
                
                case2=1+longestCommon(index1+1,firstOccurrence+1)
            
            return max(case1,case2)
        
        return longestCommon(0,0)