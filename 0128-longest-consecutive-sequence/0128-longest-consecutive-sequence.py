class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        # large=max(nums)
        member = set(nums)
        # parent={x:x+1 for x in range(min(nums),large+1) if x in member}
        nums.sort()
        parent={}
        
        for x in nums:
            
            parent[x]=x+1
        
        
        
        
        
        visited = set()
        
        def union(start,end):
            
            if end in member:
                visited.add(end)
                return union(end,parent[end])
            return start
            
        
            
        longest=0
        for node in parent:
            
            if node not in visited:
                nodeParent=union(node,parent[node])
                longest=max(longest,nodeParent-node+1)
        return longest
                
                