class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        
        left=0
        
        freq=defaultdict(int)
        long=0
        for right in range(len(answerKey)):
            
            window=right-left+1
            freq[answerKey[right]]+=1
            while window-max(freq.values())>k:
                freq[answerKey[left]]-=1
                left+=1
                window=right-left+1
            long=max(long,window)
        return long
                