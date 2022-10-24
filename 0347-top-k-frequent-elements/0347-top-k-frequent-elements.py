import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq[1]=3
        freq[2]=2
        freq[3]=1
        
        arr= [,(-2,2),(-1,3)]  (freq,num)
        
        
        """
        
        freq=defaultdict(int)
        
        for number in nums:
            freq[number]+=1
        
        freq_array=[(-freq[num],num) for num in freq]
        answer=[]
        h.heapify(freq_array)
        
        while len(answer)<k:
            freq,num=h.heappop(freq_array)
            answer.append(num)
        
        return answer
        
        
        
        
            
        