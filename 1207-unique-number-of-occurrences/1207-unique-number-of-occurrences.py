class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency=Counter(arr)
        visited=set()
        
        for freq in frequency.values():
            
            if freq not in visited:
                visited.add(freq)
            else:
                return False
        
        return True