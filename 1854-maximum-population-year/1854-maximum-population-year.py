class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix=[0]*100

        for i in range(len(logs)):          

            for val in range(logs[i][0],logs[i][1]):
                prefix[val-1950]+=1
        maxPop=max(prefix)
        for idx,val in enumerate(prefix):
            if val==maxPop:
                return 1950+idx
                break