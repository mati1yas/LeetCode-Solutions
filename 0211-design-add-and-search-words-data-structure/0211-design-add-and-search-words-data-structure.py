class TrieNode:
    
    def __init__(self):
        self.children={}
        self.endWord=False

class WordDictionary:

    def __init__(self):
        
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        
        cur=self.root
        
        for char in word:
            
            if char not in cur.children:
                cur.children[char]=TrieNode()
                cur=cur.children[char]
                continue
            
            cur=cur.children[char]
        cur.endWord=True
        
        
    def dfs(self,word,index,cur):
        
        
        if index==len(word):
            return cur.endWord
        
        
#          add base case here 
        
        
        if word[index]==".":
            
            for nbr in cur.children:
                
                if self.dfs(word,index+1,cur.children[nbr]):
                    return True
            
            
        
        if word[index] not in cur.children:
            return False
        
        if word[index] in cur.children:
            
            return self.dfs(word,index+1,cur.children[word[index]])
        
        
            
            
            
        
          
            
        
        

    def search(self, word: str) -> bool:
        
        return self.dfs(word,0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)