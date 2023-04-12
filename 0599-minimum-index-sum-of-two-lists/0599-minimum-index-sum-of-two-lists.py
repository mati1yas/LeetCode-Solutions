class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        
        
        ans=[]  # (word,indexSum)
        
        for i, str1 in enumerate(list1):
            for j , str2 in enumerate(list2):
                
                if str1==str2:
                    
                    if ans:
                    
                        if i+j<ans[-1][1]:
                            ans=[(str1,i+j)]
                        elif i+j==ans[-1][1]:
                            ans.append(((str1,i+j)))
                    
                    else:
                        ans=[(str1,i+j)]
                        
        
        return [x for x,y in ans]