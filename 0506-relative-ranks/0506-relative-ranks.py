
import heapq as h
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer=[0]*len(score)
        placements={
            0:"Gold Medal",
            1:"Silver Medal",
            2:"Bronze Medal",
        }
        index={}
        arr=[]
        for i,s in enumerate(score):
            arr.append(-s)
            index[s]=i
        h.heapify(arr)
        
        count=0
        while arr:
            x=h.heappop(arr)
            
            if count in placements:
                answer[index[abs(x)] ]=placements[count]
            else:
                 answer[index[abs(x)] ]=str(count+1)
            count+=1
        return answer