class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        letters = []
        for x in range(ord('A'), ord('Z')+1):
            letters.append(chr(x))
        result = []
        
        
        while columnNumber > 0:
            result.append(letters[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)