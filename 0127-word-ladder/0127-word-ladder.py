class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited=set({beginWord})
        
        queue=collections.deque()
        queue.append((beginWord,1))
        wordList=set(wordList)
        
        while queue:
            
            curWord,steps=queue.popleft()
            if curWord==endWord:
                return steps
            for idx in range(len(curWord)):
                
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    
                    newWord=curWord[0:idx]+char+curWord[idx+1:]
                    if newWord in wordList and newWord not in  visited:
                        queue.append((newWord,steps+1))
                        visited.add(newWord)
        return 0