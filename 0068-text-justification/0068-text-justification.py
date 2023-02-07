class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        
        
        countChars = 0         
        lineOfWord = []         
        answer = []          

        for word in words:

            if countChars + len(lineOfWord) + len(word) <= maxWidth:    
                lineOfWord.append(word)
                countChars += len(word)

            else:                                  
                gaps = len(lineOfWord) - 1          
                spaces = maxWidth - countChars    
                curBuiltLine = [lineOfWord[0]]   
                
                if gaps == 0:                       
                    curBuiltLine.append(" " * spaces)

                for w in lineOfWord[1:]:    
                    avSpace = spaces//gaps
                    
                    if spaces % gaps != 0:          
                        avSpace += 1
                    curBuiltLine.append(" " * avSpace)   
                    curBuiltLine.append(w)
                    spaces -= avSpace                 
                    gaps -= 1
                    

                answer.append("".join(curBuiltLine))

                lineOfWord = [word]                 
                countChars = len(word)

        line = " ".join(lineOfWord)           
        line += " " * (maxWidth - len(line))
        answer.append(line)
        return answer