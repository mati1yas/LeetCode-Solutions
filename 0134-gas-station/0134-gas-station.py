class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        
        res_tank=0
        
        startIndex=0
        cur_tank=0
        for i in range(len(gas)):
            
            res_tank+=gas[i]-cost[i]           
            cur_tank+=gas[i]-cost[i]

            if cur_tank<0:
                startIndex=i+1
                cur_tank=0
            
        
        
        if res_tank>=0:
            return startIndex
        else:
            return -1
        