class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        
        for word in strs:
            if "".join(sorted(list(word)) )not in anagrams:
                anagrams["".join(sorted(list(word)) )]=[word]
            else:
                anagrams["".join(sorted(list(word)) )].append(word)
        
        return anagrams.values()